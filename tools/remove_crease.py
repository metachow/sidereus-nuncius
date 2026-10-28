"""Remove fold creases from an engraving scan.

usage: python tools/remove_crease.py IMAGE.png SEGMENTS [--preview OUT.png]
  SEGMENTS: "x0,y0,x1,y1,hw;..."  rough course of each crease (full-resolution px)
            and the half width of the band to repair. Append ",1" to a segment
            to use the line exactly as given instead of locating the crease
            (useful where dense hatching confuses the search).

The first run keeps the untouched image as IMAGE_orig.png and always works from
that copy, so the segments can be adjusted and the script run again.

1. Locating: a crease runs roughly horizontally while the engraved hatching is
   diagonal, so after smoothing along x the crease stands out. Within 40 px of
   the rough line, each column's crease row is taken where the smoothed image
   deviates most from its surroundings; the result is median-smoothed.
2. Filling: one hatching direction per crease is estimated from the structure
   tensor of the surroundings. Each band pixel is interpolated between the two
   points where a line in that direction leaves the band, so strokes continue
   across the repaired strip.
"""
import os
import sys

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

SEARCH = 40


def locate(img, seg):
    x0, y0, x1, y1, hw = seg[:5]
    if len(seg) > 5 and seg[5]:      # fixed: take the given straight line as it is
        xs = np.arange(max(int(min(x0, x1)), 0), min(int(max(x0, x1)), img.shape[1] - 1) + 1)
        return xs, y0 + (y1 - y0) * (xs - x0) / (x1 - x0), hw
    g = img.astype(float)
    hs = ndi.uniform_filter1d(g, 81, axis=1)                  # smooth along the crease
    local = ndi.uniform_filter1d(hs, 2 * SEARCH + 1, axis=0)  # surroundings
    dev = np.abs(hs - local)
    xs = np.arange(max(int(min(x0, x1)), 0), min(int(max(x0, x1)), img.shape[1] - 1) + 1)
    centres = []
    for x in xs:
        yr = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
        a, b = int(yr - SEARCH), int(yr + SEARCH) + 1
        a, b = max(a, 0), min(b, img.shape[0])
        centres.append(a + int(np.argmax(dev[a:b, x])))
    centres = ndi.median_filter(np.array(centres, float), size=101, mode='nearest')
    return xs, centres, hw


def direction(img, mask, xs, centres):
    y0 = int(max(centres.min() - 150, 0)); y1 = int(min(centres.max() + 150, img.shape[0]))
    sub = img[y0:y1, xs[0]:xs[-1] + 1].astype(float)
    m = ~mask[y0:y1, xs[0]:xs[-1] + 1]
    gx, gy = ndi.sobel(sub, 1)[m], ndi.sobel(sub, 0)[m]
    jxx, jyy, jxy = (gx * gx).sum(), (gy * gy).sum(), (gx * gy).sum()
    theta = 0.5 * np.arctan2(2 * jxy, jxx - jyy) + np.pi / 2  # stroke direction
    dx, dy = np.cos(theta), np.sin(theta)
    if abs(dy) < 0.35:              # strokes nearly parallel to the crease: bridge vertically
        dx, dy = 0.0, 1.0
    return dx, dy


def fill(img, out, mask_one, dx, dy):
    H, W = img.shape
    ys, xs = np.nonzero(mask_one)
    for y, x in zip(ys, xs):
        ends = []
        for sgn in (1, -1):
            t = 1
            while True:
                ix, iy = int(round(x + sgn * t * dx)), int(round(y + sgn * t * dy))
                if not (0 <= ix < W and 0 <= iy < H) or not mask_one[iy, ix]:
                    break
                t += 1
            ix = min(max(int(round(x + sgn * (t + 1) * dx)), 0), W - 1)
            iy = min(max(int(round(y + sgn * (t + 1) * dy)), 0), H - 1)
            ends.append((t, float(img[iy, ix])))
        (t1, v1), (t2, v2) = ends
        out[y, x] = (v1 * t2 + v2 * t1) / (t1 + t2)


def patch_fill(img, out, mask_one, xs, centres, hw, chunk=48, overlap=16, border=8):
    """Fill the band with real engraving copied from nearby: for each chunk of
    columns, search a shifted source block whose rows just above and below the
    band best match the rows bordering the band, copy it in, and feather the
    chunks together."""
    H, W = img.shape
    g = img.astype(float)
    acc = np.zeros_like(g); wsum = np.zeros_like(g)
    step = chunk - overlap
    for start in range(xs[0], xs[-1] + 1, step):
        cx = np.arange(start, min(start + chunk, xs[-1] + 1))
        if len(cx) < 4:
            continue
        cc = centres[cx - xs[0]]
        ya, yb = int(cc.min() - hw), int(cc.max() + hw) + 1
        h = yb - ya
        top = (ya - border, ya); bot = (yb, yb + border)
        if top[0] < 0 or bot[1] > H:
            continue
        tgt = np.concatenate([g[top[0]:top[1], cx], g[bot[0]:bot[1], cx]])
        best, bs = None, None
        for sy in list(range(-(2 * h + 60), -(h + 2 * border), 3)) + list(range(h + 2 * border, 2 * h + 60, 3)):
            for sx in range(-60, 61, 3):
                x0, x1 = cx[0] + sx, cx[-1] + sx + 1
                if x0 < 0 or x1 > W or top[0] + sy < 0 or bot[1] + sy > H:
                    continue
                src = np.concatenate([g[top[0] + sy:top[1] + sy, x0:x1], g[bot[0] + sy:bot[1] + sy, x0:x1]])
                d = ((src - tgt) ** 2).mean()
                if best is None or d < best:
                    best, bs = d, (sx, sy)
        if bs is None:
            continue
        sx, sy = bs
        block = g[ya + sy:yb + sy, cx[0] + sx:cx[-1] + sx + 1]
        # feather weights across the chunk (triangular in x)
        wx = np.minimum(np.arange(1, len(cx) + 1), np.arange(len(cx), 0, -1)).astype(float)
        wx = np.minimum(wx, overlap) / overlap
        acc[ya:yb, cx] += block * wx
        wsum[ya:yb, cx] += wx
    sel = mask_one & (wsum > 0)
    out[sel] = acc[sel] / wsum[sel]
    # soften the band edges over a couple of pixels
    edge = ndi.binary_dilation(mask_one, iterations=2) & ~ndi.binary_erosion(mask_one, iterations=2)
    blur = ndi.uniform_filter(out, 3)
    out[edge] = blur[edge]


def main():
    path = sys.argv[1]
    segs = [tuple(float(v) for v in s.split(',')) for s in sys.argv[2].split(';') if s]
    base, ext = os.path.splitext(path)
    orig = base + '_orig' + ext
    if not os.path.exists(orig):
        Image.open(path).save(orig, dpi=(657, 657))
    img = np.asarray(Image.open(orig).convert('L'))
    out = img.astype(float).copy()
    allmask = np.zeros(img.shape, bool)
    for seg in segs:
        xs, centres, hw = locate(img, seg)
        m = np.zeros(img.shape, bool)
        for x, c in zip(xs, centres):
            m[int(c - hw):int(c + hw) + 1, x] = True
        if '--interpolate' in sys.argv:
            dx, dy = direction(img, m, xs, centres)
            fill(img, out, m, dx, dy)
        else:
            # copy from the image as repaired so far, so later segments never
            # pick up a crease that an earlier segment has already removed
            patch_fill(out.copy(), out, m, xs, centres, hw)
        allmask |= m
        print(f'segment x {xs[0]}-{xs[-1]}: crease rows {int(centres.min())}-{int(centres.max())}')
    res = np.clip(out, 0, 255).astype(np.uint8)
    Image.fromarray(res).save(path, dpi=(657, 657))
    if '--preview' in sys.argv:
        prev = sys.argv[sys.argv.index('--preview') + 1]
        ys = np.nonzero(allmask.any(1))[0]
        y0, y1 = max(ys.min() - 150, 0), min(ys.max() + 150, img.shape[0])
        a = np.stack([img[y0:y1]] * 3, -1)
        mk = a.copy(); sel = allmask[y0:y1]
        mk[sel] = (mk[sel] * 0.5 + [127, 0, 0]).astype(np.uint8)
        b = np.stack([res[y0:y1]] * 3, -1)
        w, h = img.shape[1] // 3, (y1 - y0) // 3
        s = Image.new('RGB', (w, h * 3 + 20), 'gray')
        for i, arr in enumerate((a, mk, b)):
            s.paste(Image.fromarray(arr).resize((w, h)), (0, i * (h + 10)))
        s.save(prev)


if __name__ == '__main__':
    main()
