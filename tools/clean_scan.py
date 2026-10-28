"""Remove paper yellowing from a book scan while keeping engraving tones.
Paper colour is modelled as a smooth 2-D quadratic surface fitted to paper pixels,
then divided out, so large dark areas (engravings) are not mistaken for background."""
import sys
import numpy as np
from PIL import Image

def fit_paper(ch, mask, xs, ys):
    A = np.stack([np.ones_like(xs), xs, ys, xs*xs, xs*ys, ys*ys], 1)
    coef, *_ = np.linalg.lstsq(A[mask.ravel()], ch.ravel()[mask.ravel()], rcond=None)
    return coef

def clean(src, white=0.93, black_pct=0.3):
    im = np.asarray(Image.open(src).convert("RGB"), np.float32)
    H, W, _ = im.shape
    k = 8
    sm = np.asarray(Image.fromarray(im.astype(np.uint8)).resize((W//k, H//k), Image.BOX), np.float32)
    h, w, _ = sm.shape
    yy, xx = np.mgrid[0:h, 0:w]
    xs, ys = (xx/w).ravel(), (yy/h).ravel()
    L = sm.mean(2)
    mask = L > 0.8*np.percentile(L, 90)
    for _ in range(3):  # refit, dropping pixels darker than the current paper estimate
        coefs = [fit_paper(sm[..., c], mask, xs, ys) for c in range(3)]
        A = np.stack([np.ones_like(xs), xs, ys, xs*xs, xs*ys, ys*ys], 1)
        est = np.stack([(A @ cf).reshape(h, w) for cf in coefs], 2)
        mask = (sm / est).mean(2) > 0.9
    # evaluate surface at full resolution
    Y, X = np.mgrid[0:H, 0:W].astype(np.float32)
    X /= W; Y /= H
    out = np.empty((H, W), np.float32)
    lum = (0.299, 0.587, 0.114)
    for c, cf in enumerate(coefs):
        paper = cf[0] + cf[1]*X + cf[2]*Y + cf[3]*X*X + cf[4]*X*Y + cf[5]*Y*Y
        if c == 0:
            out[:] = lum[c] * im[..., c] / paper
        else:
            out += lum[c] * im[..., c] / paper
    del X, Y
    b = np.percentile(out[::4, ::4], black_pct)
    out = np.clip((out - b) / (white - b), 0, 1)
    return Image.fromarray((out*255 + 0.5).astype(np.uint8), "L")

if __name__ == "__main__":
    clean(sys.argv[1]).save(sys.argv[2], quality=int(sys.argv[3]) if len(sys.argv) > 3 else 85)
