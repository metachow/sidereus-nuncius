"""Shared model for the text-first sources (text/*.yaml).

la.yaml      [{id: p012, s: {'01': sentence, ...}, notes: {seg: '% ...'}, noindent: bool}]
             markers inside sentences: ⟦8v⟧ page break, ⟦|⟧ split on the same page
layout.yaml  [{file, folio, nohead?, blank?, items: [{pair, mode?, la: [parts]} | {fig} | {tex}]}]
             la parts: {seg: 'p012:1', wrap?} | {pre: line} | {raw: paragraph}
zh.yaml      {pair_id: text}                      translation by alignment block
<lang>.yaml  {'p012.03': text}                    translation by sentence (distributed by script)
"""
import re

import yaml

MARK = re.compile(r'\s*⟦[^⟧]*⟧\s*')
ABBR = {'min', 'sec', 'h', 'm', 'hor', 'pr', 'D', 'M', 'Ant', 'Gio', 'Ioan', 'off', 'Con',
        'Blasph', 'Coad', 'etc', 'cf', 'P', 'Sig', 'Rev', 'S', 'Ill'}
SPLIT = re.compile(r'(?<=[.?!])(\)?)\s+(?=(?:⟦[^⟧]*⟧\s*)?[A-Z\\])')


# ------------------------------------------------------------------ YAML
class _Dumper(yaml.SafeDumper):
    pass


def _str(dumper, s):
    if '\n' in s:
        return dumper.represent_scalar('tag:yaml.org,2002:str', s, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', s)


_Dumper.add_representer(str, _str)


def dump_yaml(data, path, header=''):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(header)
        yaml.dump(data, f, Dumper=_Dumper, allow_unicode=True, sort_keys=False,
                  width=10 ** 9, default_flow_style=False)


def load_yaml(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


# ------------------------------------------------------------------ sentences
def _split_chunk(text):
    out, start = [], 0
    for m in SPLIT.finditer(text):
        left = text[start:m.start()]
        w = re.search(r'([A-Za-z]+)[.?!]$', left)
        if w and (w.group(1) in ABBR or len(w.group(1)) == 1):
            continue
        out.append(text[start:m.end(1)] if m.group(1) else text[start:m.start()])
        start = m.end()
    out.append(text[start:])
    return [s for s in out if s.strip()]


def split_sentences(text):
    """Sentences of one paragraph. ⟦|⟧ always ends a sentence; a page-break marker
    that falls exactly between two sentences is attached to the end of the first."""
    # a figure is introduced by a colon; when the page turns right after that colon
    # (figure at the foot of the page), the sentence also ends there
    pieces = re.split(r'(\s*⟦\|⟧\s*|(?<=:)\s*⟦[^⟧|]+⟧\s*)', text)
    sents = []
    for i in range(0, len(pieces), 2):
        part = _split_chunk(pieces[i])
        if i + 1 < len(pieces):
            part[-1] += ' ' + pieces[i + 1].strip()
        sents.extend(part)
    for i in range(1, len(sents)):           # move a leading marker back
        m = re.match(r'^(⟦[^⟧]*⟧)\s*', sents[i])
        if m:
            sents[i - 1] += ' ' + m.group(1)
            sents[i] = sents[i][m.end():]
    return sents


def segments(par):
    """-> (list of segment texts, {sentence_key: index of the segment it starts in})"""
    keys = list(par['s'])
    text = ' '.join(par['s'][k] for k in keys)
    segs = MARK.split(text)
    start, seg = {}, 0
    for k in keys:
        start[k] = seg
        seg += len(re.findall(r'⟦[^⟧]*⟧', par['s'][k]))
    return segs, start
