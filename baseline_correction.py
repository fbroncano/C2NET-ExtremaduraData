"""Reference bias correction for the C2NEx-22 dataset.

Fits the log-log baseline described in the data descriptor,

    log10(Chl_hat) = a * log10(P) + b,

for each C2-Net processor, plus a joint form that uses the three co-registered
retrievals together, and evaluates them under leave-one-reservoir-out
cross-validation. Reservoirs, not records, are the unit of resampling: the
94 pairs are unevenly distributed over 32 reservoirs, and record-level
resampling would let the best-sampled reservoirs appear in both folds.

This is a starting point and a sanity check, not a recommended retrieval. The
coefficients are fitted on one regional network and should be refitted before
being applied elsewhere.

Usage:  python baseline_correction.py [samples.csv]
Requires: numpy, pandas
"""

import sys

import numpy as np
import pandas as pd

PROCESSORS = ["C2RCC", "C2X", "C2XC"]


def fit(x, y):
    """Least-squares fit of y = a*x + b; x, y in log10 space."""
    a, b = np.polyfit(x, y, 1)
    return a, b


def loro_predict(df, cols):
    """Leave-one-reservoir-out predictions, in log10 space."""
    X = np.column_stack([np.log10(df[c].values) for c in cols] + [np.ones(len(df))])
    y = np.log10(df["In_situ"].values)
    pred = np.empty(len(df))
    for reservoir in df["Reservoir"].unique():
        test = (df["Reservoir"] == reservoir).values
        coef, *_ = np.linalg.lstsq(X[~test], y[~test], rcond=None)
        pred[test] = X[test] @ coef
    return 10.0 ** pred


def score(obs, pred):
    """Median absolute percentage difference and median ratio, linear space."""
    return 100 * np.median(np.abs(pred - obs) / obs), np.median(pred / obs)


def main(path="samples.csv"):
    df = pd.read_csv(path)
    obs = df["In_situ"].values

    print(f"{len(df)} pairs, {df['Reservoir'].nunique()} reservoirs\n")
    print(f"{'model':16s} {'a':>7s} {'b':>7s} {'MAPD raw':>9s} "
          f"{'MAPD corr':>10s} {'ratio raw':>10s} {'ratio corr':>11s}")

    for p in PROCESSORS:
        a, b = fit(np.log10(df[p].values), np.log10(obs))
        mapd_raw, ratio_raw = score(obs, df[p].values)
        mapd_cv, ratio_cv = score(obs, loro_predict(df, [p]))
        print(f"{p:16s} {a:7.3f} {b:7.3f} {mapd_raw:8.0f}% {mapd_cv:9.0f}% "
              f"{ratio_raw:10.2f} {ratio_cv:11.2f}")

    mapd_cv, ratio_cv = score(obs, loro_predict(df, PROCESSORS))
    coef, *_ = np.linalg.lstsq(
        np.column_stack([np.log10(df[c].values) for c in PROCESSORS]
                        + [np.ones(len(df))]),
        np.log10(obs), rcond=None)
    print(f"{'three jointly':16s} {'':>7s} {'':>7s} {'':>9s} {mapd_cv:9.0f}% "
          f"{'':>10s} {ratio_cv:11.2f}")
    print("\njoint coefficients [C2RCC, C2X, C2XC, intercept]:",
          np.round(coef, 3))


if __name__ == "__main__":
    main(*sys.argv[1:])
