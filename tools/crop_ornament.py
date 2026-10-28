"""Crop a woodcut ornament from a cleaned scan.

usage: python tools/crop_ornament.py SCAN x0 y0 x1 y1 OUT.png
Coordinates are a rough box in work/pages/ pixels (1/3 of full size); the box
is tightened to the ink inside it on the full-resolution scan (scans/), padded
slightly and saved as a greyscale PNG at 657 dpi.
"""
import sys

import numpy as np
from PIL import Image

scan, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
im = np.asarray(Image.open(f'scans/{scan}.png').convert('L'))
box = im[y0 * 3:y1 * 3, x0 * 3:x1 * 3]
ink = box < 140
rows = np.where(ink.mean(1) > 0.01)[0]
cols = np.where(ink.mean(0) > 0.01)[0]
pad = 12
r0, r1 = max(rows.min() - pad, 0), min(rows.max() + pad, box.shape[0])
c0, c1 = max(cols.min() - pad, 0), min(cols.max() + pad, box.shape[1])
crop = box[r0:r1, c0:c1]
Image.fromarray(crop).save(out, dpi=(657, 657))
print(out, crop.shape[1], 'x', crop.shape[0], 'px =',
      round(crop.shape[1] / 657 * 25.4), 'x', round(crop.shape[0] / 657 * 25.4), 'mm')
