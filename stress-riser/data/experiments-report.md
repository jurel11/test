## A. Accent saliency proxy (Achanta frequency-tuned saliency on a 168x94 downscale; 40 random scenes per cell)
hit = share of scenes in which the most salient pixel lies on the accent disc; ratio = median(mean saliency on disc / mean saliency elsewhere)

| accent | background | hit rate | saliency ratio |
|---|---|---|---|
| red | paper | 100% | 3.3 |
| red | sky | 100% | 3.4 |
| red | grn_l | 100% | 2.9 |
| red | grn_d | 100% | 2.9 |
| red | brown | 85% | 2.0 |
| red | tan | 100% | 3.4 |
| red | white | 100% | 3.2 |
| red | ink | 78% | 1.8 |
| amber | paper | 98% | 2.5 |
| amber | sky | 100% | 2.8 |
| amber | grn_l | 2% | 1.6 |
| amber | grn_d | 48% | 1.9 |
| amber | brown | 8% | 1.6 |
| amber | tan | 98% | 2.3 |
| amber | white | 98% | 2.5 |
| amber | ink | 100% | 1.9 |
| **red mean over backgrounds** | | 95% | 2.9 |
| **amber mean over backgrounds** | | 69% | 2.1 |

## B. JPEG q90 edge damage (mean dE76 in a 16 px band at a hard edge with NO outline; transition width in px)

| pair | dL* | 4:2:0 dE76 | 4:2:0 width px | 4:4:4 dE76 | 4:4:4 width px |
|---|---|---|---|---|---|
| red/grn_d | 4.0 | 3.1 | 2 | 0.61 | 0 |
| red/brown | 2.5 | 1.87 | 2 | 0.57 | 0 |
| amber/grn_l | 3.3 | 1.61 | 2 | 0.24 | 0 |
| tan/grn_l | 2.9 | 1.78 | 2 | 0.45 | 0 |
| tan/amber | 0.5 | 1.43 | 2 | 0.21 | 0 |
| red/paper | 41.2 | 2.01 | 2 | 0.6 | 0 |
| red/sky | 35.9 | 2.96 | 2 | 0.61 | 0 |
| amber/ink | 66.2 | 1.88 | 2 | 0.0 | 0 |
| ink/paper | 83.7 | 0.69 | 0 | 0.34 | 0 |
| grn_d/brown | 1.4 | 1.84 | 2 | 0.65 | 0 |
| red/ink | 42.5 | 2.59 | 2 | 0.27 | 0 |

## C. File size of a flat-colour cartoon thumbnail (demo_1, 1280x720)

| encoding | bytes |
|---|---|
| PNG (RGB, optimized) | 33,005 |
| PNG-8 (64 colours, no dither) | 14,506 |
| JPEG q85 4:2:0 | 55,713 |
| JPEG q85 4:4:4 | 66,623 |
| JPEG q90 4:2:0 | 63,058 |
| JPEG q90 4:4:4 | 75,690 |
| JPEG q95 4:2:0 | 76,428 |
| JPEG q95 4:4:4 | 93,797 |