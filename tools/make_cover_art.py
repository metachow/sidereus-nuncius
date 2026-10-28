"""Turn a cleaned engraving into an ink layer for the cover: paper becomes
transparent, ink becomes a warm black, so the plate prints directly on the
cover's paper colour.

usage: python tools/make_cover_art.py figures/luna_4.png figures/cover_moon.png
"""
import sys

import numpy as np
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
g = np.asarray(Image.open(src).convert('L')).astype(float)
alpha = np.clip((235 - g) / 205, 0, 1) ** 0.9          # paper (>235) fully transparent
rgba = np.zeros(g.shape + (4,), np.uint8)
rgba[..., :3] = (38, 30, 24)                           # warm printing-ink black
rgba[..., 3] = (alpha * 255).astype(np.uint8)
Image.fromarray(rgba, 'RGBA').save(out, dpi=(657, 657))
print(out, g.shape[::-1])
