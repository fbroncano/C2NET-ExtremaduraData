# C2NET-ExtremaduraData

Paired satellite–in-situ chlorophyll-a (Chl-a) dataset for **32 small inland reservoirs** in Extremadura, southwestern Spain (2017–2022). For each in-situ measurement, Chl-a was retrieved from Sentinel-2 MSI Level-1C imagery atmospherically corrected with three processors of the C2-Net family (C2RCC, C2X, C2XC) in ESA SNAP, using a 7×7-pixel maximum-value estimator.

This repository accompanies a data descriptor submitted to *Data in Brief*, associated with the related research article Torrecilla-Pinero et al. (2026), *Int. J. Appl. Earth Obs. Geoinf.* 152, 105415 (https://doi.org/10.1016/j.jag.2026.105415).

## Study area

![Location of the 32 study reservoirs in Extremadura, Spain](figures/reservoirs.png)

## Repository structure

```
C2NET-ExtremaduraData/
  README.md
  samples.csv      94 paired satellite–in-situ records (6 columns)
  metadata.csv     32 reservoirs, descriptors (15 columns)
  figures/
    reservoirs.pdf / reservoirs.png   study-area map
```

All files are UTF-8 encoded; dates use ISO 8601 (`YYYY-MM-DD`) and the decimal separator is a point.

## Overview

In-situ Chl-a was measured by the Junta de Extremadura between 2017 and 2022. A total of 138 in-situ measurements were collected; the 94 that coincide with a cloud-free Sentinel-2 acquisition form the complete satellite–in-situ pairs in `samples.csv`. The reservoirs span mesotrophic to hypertrophic states and include extreme bloom events (up to 332 µg/L).

## File formats

### `samples.csv`

| Column | Description | Units |
|---|---|---|
| `Reservoir` | Reservoir name | — |
| `Date` | Acquisition date (ISO 8601) | YYYY-MM-DD |
| `In_situ` | In-situ measured chlorophyll-a | µg/L |
| `C2RCC` | Chl-a from the C2RCC processor | µg/L |
| `C2X` | Chl-a from the C2X processor | µg/L |
| `C2XC` | Chl-a from the C2XC processor | µg/L |

### `metadata.csv`

| Column | Description | Units |
|---|---|---|
| `Location` | Reservoir name | — |
| `Samples` | Number of in-situ measurements | — |
| `Valid Dates` | Cloud-free Sentinel-2 acquisitions (= rows in `samples.csv`) | — |
| `latitude` | Latitude | °N |
| `longitude` | Longitude (negative = West) | ° |
| `Basin` | River basin | — |
| `Construction year` | Year of construction | — |
| `Surface (km2)` | Surface area | km² |
| `Volume (hm3)` | Storage capacity | hm³ |
| `Elevation` | Elevation | m |
| `Max. Chl-a` / `Min. Chl-a` / `Ave. Chl-a` / `Std. Chl-a` | In-situ Chl-a statistics over all in-situ measurements | µg/L |
| `Trophic state` | OECD class by mean in-situ Chl-a | — |

> Note: the Chl-a statistics in `metadata.csv` are computed over all 138 in-situ measurements, whereas `samples.csv` contains the 94 records with a coincident cloud-free image.

## Reservoir metadata

| Location | Samples | Valid Dates | latitude | longitude | Basin | Construction year | Surface (km2) | Volume (hm3) | Elevation | Max. Chl-a | Min. Chl-a | Ave. Chl-a | Std. Chl-a | Trophic state |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Acebo | 4 | 2 | 40.240756 | -6.710411 | Tagus | 1997 | 0.1 | 1 | 563 | 11.50 | 2.50 | 6.12 | 3.6636 | Mesotrophic |
| Aguijón | 5 | 3 | 38.475032 | -6.908223 | Guadiana | 1995 | 1.88 | 11 | 386 | 166.96 | 5.27 | 56.86 | 57.1688 | Hypertrophic |
| Alcuéscar | 5 | 2 | 39.222270 | -6.229320 | Tagus | 1977 | 1 | 2 | 443 | 206.80 | 12.35 | 56.66 | 75.2283 | Hypertrophic |
| Aldea del Cano | 5 | 4 | 39.265505 | -6.294546 | Tagus | 1988 | 0.84 | 3 | 388 | 131.60 | 46.81 | 83.06 | 28.6573 | Hypertrophic |
| Aliseda | 3 | 2 | 39.412345 | -6.689628 | Tagus | 1978 | 0.06 | 0 | 349 | 14.32 | 8.64 | 11.87 | 2.3835 | Eutrophic |
| Alpotrel | 3 | 3 | 39.367297 | -7.207824 | Tagus | 1991 | 0.49 | 2 | 500 | 25.00 | 10.40 | 17.84 | 5.9639 | Eutrophic |
| Arrocerezal | 3 | 2 | 40.389367 | -6.263217 |  |  | 0.03 |  | 556 | 18.95 | 0.73 | 8.79 | 7.5851 | Eutrophic |
| Brozas | 5 | 4 | 39.621919 | -6.767617 | Tagus | 1959 | 0.25 | 1 | 395 | 113.38 | 36.57 | 56.97 | 28.5719 | Hypertrophic |
| Burguillos del Cerro | 5 | 4 | 38.404345 | -6.602901 | Guadiana | 1993 | 0.42 | 3 | 470 | 201.10 | 1.90 | 73.69 | 71.0265 | Hypertrophic |
| Cantalgallo | 3 | 1 | 39.684074 | -5.783065 |  |  | 0.13 |  | 490 | 12.20 | 4.39 | 8.26 | 3.1887 | Eutrophic |
| El Santo | 3 | 3 | 39.634345 | -7.478031 |  |  | 0.07 |  | 286 | 62.78 | 9.77 | 28.66 | 24.1727 | Hypertrophic |
| Garciaz | 3 | 1 | 39.396485 | -5.604155 | Tagus | 1994 | 0.05 | 0 | 779 | 16.42 | 4.33 | 8.76 | 5.4385 | Eutrophic |
| Garganta del Obispo | 3 | 1 | 40.097792 | -5.856256 | Tagus | 1995 | 0.01 | 0 | 983 | 85.33 | 0.97 | 29.40 | 39.5503 | Hypertrophic |
| Hervás | 3 | 2 | 40.268834 | -5.823085 | Tagus | 1991 | 0.03 | 0 | 822 | 19.42 | 8.42 | 13.59 | 4.5149 | Eutrophic |
| Jaime Ozores | 11 | 9 | 38.467359 | -6.560673 | Guadiana | 1962 | 0.21 | 2 | 438 | 211.82 | 7.28 | 77.99 | 79.1190 | Hypertrophic |
| Las Majadillas | 3 | 3 | 40.082326 | -5.781343 |  |  | 0.17 |  | 605 | 25.99 | 2.78 | 11.31 | 10.4257 | Eutrophic |
| Llerena | 4 | 4 | 38.304330 | -5.910595 | Guadiana | 1989 | 1.55 | 8 | 543 | 147.12 | 30.43 | 65.19 | 47.5758 | Hypertrophic |
| Los Huertos | 4 | 2 | 39.726136 | -5.382478 |  |  | 0.1 |  | 525 | 70.55 | 26.69 | 48.30 | 18.9634 | Hypertrophic |
| Madroñera | 5 | 2 | 39.454987 | -5.699192 | Tagus | 1973 | 0.13 | 0 | 705 | 38.93 | 3.57 | 16.41 | 12.5613 | Eutrophic |
| Majarrobledo | 3 | 1 | 40.437671 | -6.337652 |  |  | 0.02 |  | 920 | 20.48 | 0.40 | 7.72 | 9.0573 | Mesotrophic |
| Membrío | 3 | 1 | 39.520517 | -7.064116 | Tagus | 1978 | 0.28 | 1 | 327 | 60.76 | 19.53 | 41.57 | 16.9517 | Hypertrophic |
| Navarredonda | 5 | 2 | 39.240847 | -6.017991 | Tagus | 1997 | 0.34 | 1 | 512 | 164.61 | 3.39 | 70.89 | 59.8990 | Hypertrophic |
| Navas del Madroño | 5 | 3 | 39.638273 | -6.610187 | Tagus | 1938 | 0.17 | 1 | 416 | 33.63 | 10.48 | 27.04 | 8.3969 | Hypertrophic |
| Nogales | 5 | 3 | 38.555789 | -6.730072 | Guadiana | 1991 | 1.53 | 18 | 369 | 96.46 | 26.83 | 60.08 | 29.3369 | Hypertrophic |
| Palomero | 3 | 2 | 40.241523 | -6.341918 | Tagus | 1977 | 0.07 | 0 | 476 | 44.83 | 2.35 | 21.98 | 17.4918 | Eutrophic |
| Pretura del Molino | 3 | 3 | 39.087035 | -4.911290 |  |  | 0.25 |  | 491 | 8.41 | 5.58 | 7.04 | 1.1574 | Mesotrophic |
| Ribera del Castaño | 3 | 1 | 39.837104 | -6.266681 |  |  | 0.16 |  | 435 | 26.99 | 10.51 | 19.46 | 6.8031 | Eutrophic |
| Rubiales | 4 | 3 | 38.402369 | -6.796037 |  |  | 0.06 |  | 502 | 204.58 | 47.49 | 99.42 | 61.6050 | Hypertrophic |
| San Marcos | 5 | 5 | 40.122931 | -6.320906 | Tagus | 1997 | 0.33 | 3 | 401 | 35.68 | 6.30 | 23.21 | 9.9878 | Eutrophic |
| Santa Lucía | 3 | 2 | 39.497937 | -5.465744 |  |  | 0.09 | 1 | 682 | 11.94 | 4.22 | 8.85 | 3.3345 | Eutrophic |
| Talaván | 11 | 10 | 39.673738 | -6.306319 | Tagus | 1977 | 0.42 | 1 | 360 | 72.17 | 3.00 | 25.42 | 20.7355 | Hypertrophic |
| Tres Torres | 5 | 4 | 38.093030 | -6.316272 | Tagus | 1973 | 0.3 | 1 | 435 | 331.88 | 49.46 | 169.55 | 113.6788 | Hypertrophic |

## Related articles

- A. Cuartero, J. Cáceres-Merino, J.A. Torrecilla-Pinero (2023). *An application of C2-Net atmospheric corrections for chlorophyll-a estimation in small reservoirs.* Remote Sensing Applications: Society and Environment 32, 101021. https://doi.org/10.1016/j.rsase.2023.101021
- J. Cáceres-Merino, A. Cuartero, J.A. Torrecilla-Pinero (2024). *Finding the optimal window: the influence of size on remote-sensing-based Chl-a prediction in small reservoirs.* IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. 17, 18769–18783. https://doi.org/10.1109/JSTARS.2024.3476970
- J.A. Torrecilla-Pinero, V. Amores-Chaparro, J. Cáceres-Merino, F. Broncano, A. Cuartero (2026). *Satellite-derived chlorophyll-a in inland reservoirs: bias correction of C2RCC, C2X and C2XC processors with machine learning.* Int. J. Appl. Earth Obs. Geoinf. 152, 105415. https://doi.org/10.1016/j.jag.2026.105415

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Citation

A Zenodo DOI will be added here upon release.

## Contact

Fernando Broncano — fbroncano@unex.es — Universidad de Extremadura, Spain
