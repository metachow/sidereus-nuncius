"""Download the original page scans from the Internet Archive and de-yellow them.

usage: python tools/fetch_scans.py

Writes scans/NNNN.png (full resolution, ~657 dpi, greyscale; covers and bookplate
kept in colour) and work/pages/NNNN.png (1/3 size, for reading). The scans are
from the Smithsonian Libraries copy, archive.org item Sidereusnuncius00Gali
("Not in copyright"). Takes a few minutes; needs about 400 MB of disk.
"""
import io
import os
import sys
import urllib.request
import zipfile
from concurrent.futures import ProcessPoolExecutor

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from clean_scan import clean  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = 'https://archive.org/download/Sidereusnuncius00Gali/Sidereusnuncius00Gali_jp2.zip'
KEEP_COLOR = {1, 2, 68}   # front cover, bookplate, back cover


def work(args):
    data, n = args
    src = io.BytesIO(data)
    if n in KEEP_COLOR:
        im = Image.open(src).convert('RGB')
    else:
        im = clean(src)
    im.save(os.path.join(ROOT, 'scans', f'{n:04d}.png'))
    im.resize((im.width // 3, im.height // 3), Image.LANCZOS).save(
        os.path.join(ROOT, 'work', 'pages', f'{n:04d}.png'))
    return n


def main():
    os.makedirs(os.path.join(ROOT, 'scans'), exist_ok=True)
    os.makedirs(os.path.join(ROOT, 'work', 'pages'), exist_ok=True)
    print('downloading', URL)
    z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(URL).read()))
    jobs = [(z.read(f), int(f[-8:-4])) for f in sorted(z.namelist()) if f.endswith('.jp2')]
    with ProcessPoolExecutor(4) as ex:
        for n in ex.map(work, jobs):
            print(n, end=' ', flush=True)
    print('\ndone')


if __name__ == '__main__':
    main()
