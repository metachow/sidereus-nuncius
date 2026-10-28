"""Side-by-side images of the same page: the 1610 scan, the Chinese edition, the
English edition and (when its PDF is there) the Japanese edition, for the README.

usage: python tools/make_comparison.py f01r f02r f10v ...
Needs work/pages/ (tools/fetch_scans.py) and the edition PDFs
(Sidereus_Nuncius_la-zh.pdf, Sidereus_Nuncius_la-en.pdf, Sidereus_Nuncius_la-ja.pdf). Writes showcase/compare_<folio>.jpg.
"""
import csv
import os
import re
import sys

import fitz
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = 1100                     # height of each page image, px
PAD, LABEL = 24, 54
LATIN_FONT = 'c:/texlive/2022/texmf-dist/fonts/opentype/public/ebgaramond/EBGaramond-Regular.otf'
CJK_FONT = os.path.join(ROOT, 'fonts', 'NotoSerifSC-Regular.ttf')
JA_FONT = os.path.join(ROOT, 'fonts', 'NotoSerifJP-Regular.ttf')

scan_of = {}
with open(os.path.join(ROOT, 'work', 'folio_map.tsv'), encoding='utf-8') as f:
    for row in list(csv.reader(f, delimiter='\t'))[1:]:
        scan_of[row[2]] = row[0]


def pdf_page(path, label):
    """render the page whose running head carries the folio label, e.g. [ 16b v ]"""
    doc = fitz.open(os.path.join(ROOT, path))
    want = re.sub(r'\s+', '', label)
    for page in doc:
        m = re.search(r'\[\s*([0-9]+[a-z]?\s*[rv])\s*\]', page.get_text())
        if m and re.sub(r'\s+', '', m.group(1)) == want:
            zoom = H / page.rect.height
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
            return Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    raise SystemExit(f'{label} not found in {path}')


def folio_label(name):
    m = re.match(r'f0*(\d+)([a-z]?)([rv])$', name)
    return f'{m.group(1)}{m.group(2)}{m.group(3)}'


for name in sys.argv[1:]:
    label = folio_label(name)
    scan = Image.open(os.path.join(ROOT, 'work', 'pages', scan_of[name] + '.png')).convert('RGB')
    scan = scan.resize((round(scan.width * H / scan.height), H), Image.LANCZOS)
    pages = [scan, pdf_page('Sidereus_Nuncius_la-zh.pdf', label), pdf_page('Sidereus_Nuncius_la-en.pdf', label)]
    titles = [('Venetiis 1610 · 初版扫描', CJK_FONT), ('拉丁文—中文对照本', CJK_FONT),
              ('Latin–English edition', LATIN_FONT)]
    if os.path.exists(os.path.join(ROOT, 'Sidereus_Nuncius_la-ja.pdf')):
        pages.append(pdf_page('Sidereus_Nuncius_la-ja.pdf', label))
        titles.append(('ラテン語・日本語対訳', JA_FONT))
    W = sum(p.width for p in pages) + PAD * (len(pages) + 1)
    out = Image.new('RGB', (W, H + LABEL + PAD), (246, 244, 240))
    d = ImageDraw.Draw(out)
    x = PAD
    for p, (t, fnt) in zip(pages, titles):
        font = ImageFont.truetype(fnt, 26)
        tw = d.textlength(t, font=font)
        d.text((x + (p.width - tw) / 2, 14), t, fill=(70, 60, 50), font=font)
        out.paste(p, (x, LABEL))
        d.rectangle([x - 1, LABEL - 1, x + p.width, LABEL + H], outline=(200, 195, 185))
        x += p.width + PAD
    os.makedirs(os.path.join(ROOT, 'showcase'), exist_ok=True)
    path = os.path.join(ROOT, 'showcase', f'compare_{name}.jpg')
    out.save(path, quality=88)
    print(path, out.size)
