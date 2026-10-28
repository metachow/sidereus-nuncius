"""Render a Chinese character as an aged woodblock initial, to match the
woodcut initials of the 1610 edition.

usage: python tools/make_zh_initial.py CHAR FONTFILE OUT.png [--seed N] [--wght W]

Double-ruled square block with a hatched ground, the character in solid ink
with a white halo, then worn: ragged edges, uneven inking, specks where the
ink did not take. Output: greyscale PNG, 900 px square (about 35 mm at 657 dpi).

The character is scaled to fill the frame, as the roman capitals of the 1610
woodcut initials do, and set in a Song (serif) face: the woodcut letters are
plain roman capitals, so the Chinese counterpart is the plain book face too.
--wght instances a variable font (e.g. NotoSerifSC-VF.ttf --wght 900).
"""
import io
import sys

import numpy as np
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi

char, fontfile, out = sys.argv[1], sys.argv[2], sys.argv[3]
seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1
rng = np.random.default_rng(seed)
if '--wght' in sys.argv:
    w = int(sys.argv[sys.argv.index('--wght') + 1])
    inst = instancer.instantiateVariableFont(TTFont(fontfile), {'wght': w})
    fontfile = io.BytesIO()
    inst.save(fontfile)

S = 900
ink = Image.new('L', (S, S), 0)          # 255 = ink
d = ImageDraw.Draw(ink)

# frame: heavy outer rule, thin inner rule
d.rectangle([8, 8, S - 9, S - 9], outline=255, width=22)
d.rectangle([52, 52, S - 53, S - 53], outline=255, width=6)

# hatched ground inside the inner rule
ground = Image.new('L', (S, S), 0)
g = ImageDraw.Draw(ground)
for k in range(-S, 2 * S, 17):
    g.line([(k, S), (k + S, 0)], fill=255, width=5)
gmask = Image.new('L', (S, S), 0)
ImageDraw.Draw(gmask).rectangle([66, 66, S - 67, S - 67], fill=255)
ink.paste(ground, (0, 0), gmask)

# character: white halo, then solid ink; sized so its larger side is FILL px
FILL = 730
if isinstance(fontfile, io.BytesIO):
    fontfile.seek(0)
    data = fontfile.getvalue()
    load = lambda size: ImageFont.truetype(io.BytesIO(data), size)
else:
    load = lambda size: ImageFont.truetype(fontfile, size)
box = d.textbbox((0, 0), char, font=load(600))
font = load(round(600 * FILL / max(box[2] - box[0], box[3] - box[1])))
box = d.textbbox((0, 0), char, font=font)
x = (S - (box[2] - box[0])) / 2 - box[0]
y = (S - (box[3] - box[1])) / 2 - box[1]
glyph = Image.new('L', (S, S), 0)
ImageDraw.Draw(glyph).text((x, y), char, font=font, fill=255)
gl = np.asarray(glyph) > 127
halo = ndi.binary_dilation(gl, iterations=16)
a = np.asarray(ink) > 127
a = (a & ~halo) | gl

# --- wear -------------------------------------------------------------
f = a.astype(float)
# ragged edges: blur, add noise at two scales, re-threshold
f = (ndi.gaussian_filter(f, 2.5) + rng.normal(0, 0.18, f.shape)
     + 0.12 * ndi.gaussian_filter(rng.normal(0, 1, f.shape), 4) * 4)
f = ndi.gaussian_filter(f, 1.0) > 0.5
# hatching breaks where the ink skipped (only on the thin ground lines)
skip = ndi.gaussian_filter(rng.normal(0, 1, (S, S)), 9) > 0.035
ground_only = a & ~ndi.binary_dilation(gl, iterations=2) & (np.asarray(gmask) > 0)
f &= ~(ground_only & skip)
# uneven inking: low-frequency field, some areas print lighter
field = ndi.gaussian_filter(rng.normal(0, 1, (S, S)), 60)
field = (field - field.min()) / (field.max() - field.min())
tone = 0.68 + 0.32 * field
# specks where the ink did not take
specks = ndi.gaussian_filter(rng.random((S, S)), 3.0)
voids = specks > np.quantile(specks, 0.9965)
voids = ndi.binary_dilation(voids, iterations=1) & (rng.random((S, S)) > 0.3)
# a few worn chips along the frame
chips = ndi.binary_dilation(rng.random((S, S)) > 0.99985, iterations=6)
inked = f & ~voids & ~chips
dark = np.where(inked, 255 * tone, 0)
# slight ink spread and paper tooth
dark = ndi.gaussian_filter(dark, 0.7) * (1 - 0.12 * rng.random((S, S)))
img = (245 - np.clip(dark, 0, 245)).astype(np.uint8)
Image.fromarray(img).save(out, dpi=(657, 657))
print(out)
