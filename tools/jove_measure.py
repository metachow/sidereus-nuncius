r"""Measure Galileo's Jupiter diagrams on a cleaned page scan and print \jove lines.

usage:
  python jove_measure.py PAGE.png            # find all diagrams automatically
  python jove_measure.py PAGE.png --y 4450 [--x 1900]   # diagram near y (and Jupiter near x), full-res px

Positions are in Jupiter diameters (negative = east/Ori., positive = west/Occ.),
sizes relative to the median star on that line. Stars visibly above/below the line
go into the optional second list as x/size/dy (dy > 0 = above). Stars further than
about 0.9 diameters off the line are NOT detected: add them by hand. Always check the result against
the scan: dust specks and broken glyphs can still slip through.
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

def is_ring(comp):
    # hollow round glyph: sparse ink overall and an empty centre (works for open circles too)
    h, w = comp.shape
    centre = comp[int(h * 0.3):int(h * 0.7), int(w * 0.3):int(w * 0.7)]
    return comp.mean() < 0.45 and centre.mean() < 0.03

def find_rings(ink, ymin=0, ymax=None, min_d=95):
    lab, _ = ndi.label(ink)
    rings = []
    for i, s in enumerate(ndi.find_objects(lab)):
        h = s[0].stop - s[0].start; w = s[1].stop - s[1].start
        cy = (s[0].start + s[0].stop) / 2
        if not (ymin <= cy <= (ymax or ink.shape[0])):
            continue
        if min_d <= h <= 220 and min_d <= w <= 220 and abs(h - w) < 0.25 * max(h, w):
            if is_ring(lab[s] == i + 1):
                rings.append((cy, (s[1].start + s[1].stop) / 2, (h + w) / 2))
    return rings

def stars_on_line(ink, cy, cx, d):
    y0, y1 = int(cy - 0.9 * d), int(cy + 0.9 * d)
    band = ink[y0:y1]
    blob, _ = ndi.label(ndi.binary_dilation(band, iterations=max(2, int(d * 0.12))))
    words, cand = [], []
    for j, s in enumerate(ndi.find_objects(blob)):
        h = s[0].stop - s[0].start; w = s[1].stop - s[1].start
        x0, x1 = s[1].start, s[1].stop
        x = (x0 + x1) / 2
        if abs(x - cx) < 0.6 * d:
            continue                              # Jupiter itself
        if w > 1.6 * h and h > 0.3 * d:
            words.append((x0, x1)); continue      # Ori. / Occ. / running text
        if h < 0.4 * d:
            continue                              # dust, full stops
        yc = (s[0].start + s[0].stop) / 2 + y0
        cand.append((x, h, yc))
    left = max([x1 for x0, x1 in words if x1 < cx], default=-1e9)    # end of "Ori."
    right = min([x0 for x0, x1 in words if x0 > cx], default=1e9)    # start of "Occ."
    cand = [c for c in cand if left < c[0] < right]
    if not cand:
        return []
    ref = np.median([c[1] for c in cand])
    # dy in Jupiter diameters, positive = above the line (north)
    return [((x - cx) / d, h / ref, (cy - yc) / d) for x, h, yc in sorted(cand)]

def main():
    path = sys.argv[1]
    ink = np.asarray(Image.open(path).convert("L")) < 120
    if "--y" in sys.argv:
        y = float(sys.argv[sys.argv.index("--y") + 1])
        rings = find_rings(ink, y - 150, y + 150, min_d=45)
        if "--x" in sys.argv:                                # ring nearest to the given x
            x = float(sys.argv[sys.argv.index("--x") + 1])
            rings = sorted(rings, key=lambda r: abs(r[1] - x))[:1]
        else:                                                # largest ring near that line
            rings = sorted(rings, key=lambda r: -r[2])[:1]
        if not rings:
            print("no ring found near that line; the circle may be broken - measure by hand")
    else:
        rings = find_rings(ink)
    for cy, cx, d in sorted(rings):
        stars = stars_on_line(ink, cy, cx, d)
        on = ", ".join(f"{x:.1f}/{s:.2f}" for x, s, dy in stars if abs(dy) < 0.3)
        off = ", ".join(f"{x:.1f}/{s:.2f}/{dy:.2f}" for x, s, dy in stars if abs(dy) >= 0.3)
        cmd = chr(92) + "jove{" + on + "}" + (f"[{off}]" if off else "")
        print(f"y={cy:5.0f}  Jupiter d={d:.0f}px  {cmd}")

if __name__ == "__main__":
    main()
