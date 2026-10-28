# English translation: guidelines

The English edition sets a new English translation beside the same Latin as the Chinese
edition, page for page with the 1610 Venice print. You translate **sentence by sentence**;
the script places each sentence on the page where its Latin sentence begins, so you do
not deal with pages at all.

## 1. What you get and what you write

- See your range with `PYTHONIOENCODING=utf-8 python tools/show_range.py p015 p022`.
  It prints every Latin sentence with its key (`p017.04: ...`), the Chinese edition's
  text for the same passage (useful for its footnotes, which were researched and
  proofread), and any **special blocks** (title lines, headings, signatures) in the range.
- Write `text/en/partN.yaml`, a flat mapping, UTF-8:

  ```yaml
  p017.04: >-
    On the fourth or fifth day after conjunction, when the Moon shows herself to us with
    bright horns, ...
  f04v.3: |-
    \vspace{0.8\baselineskip}
    {\raggedleft Secretary of the Most Illustrious Council of Ten\\ Bartolomeo Comino\par}
  ```
  One entry per Latin sentence key, no more, no fewer. Use `>-` for prose and `|-` for
  special blocks (keeps their line breaks). Never merge two Latin sentences into one entry
  or move content between entries: if English wants different sentence boundaries, you may
  use several English sentences inside one entry.
- Check your file: `PYTHONIOENCODING=utf-8 python tools/check_translation.py en text/en/partN.yaml p015 p022`
  (completeness, LaTeX sanity, compiles your pages). It must say "OK, no problems".
  Pages "running long" are fine: page fitting is done afterwards.

## 2. Independence (essential)

Translate **directly from the Latin**. Do not consult, reproduce or paraphrase any modern
English translation (Van Helden 1989, Drake 1957, Shea & Maffei 2009, or any other still in
copyright), and do not reconstruct one from memory. The public-domain translation of
E. S. Carlos (1880) may be consulted to check your understanding of a hard passage, but the
wording must be your own. The Chinese edition may be consulted for interpretation and notes.

## 3. Style

- Faithful, clear, modern English prose (American spelling). Keep Galileo's tone: precise,
  occasionally exultant, courteous in the dedication. Long Latin periods may be broken into
  shorter English sentences inside the same entry; nothing may be added or dropped.
- Persons as in the Latin: Galileo moves between "I" and "we"; follow him.
- Numbers in the observation log as Galileo gives them: "On the 12th, at the first hour of
  the night", "distant from Jupiter 2 minutes", "min. 7" → "7 minutes".
- The dedication is printed in italic in 1610; the generator sets it in italic, so write
  plain text there (no `\textit` around whole sentences).

## 4. LaTeX in your text

- The Latin uses `\capsemph{planetas}` for words the 1610 print sets in capitals. Mark the
  English equivalent with `\tremph{planets}` (rendered as spaced capitals). Italic passages
  inside roman text (titles of books): `\textit{...}`.
- Footnotes: `\footnote{...}` at the end of the sentence (or phrase) it explains. Take the
  Chinese edition's footnotes as the basis: translate and adapt them for English readers
  (drop remarks that only concern Chinese terms, e.g. traditional Chinese star names; keep
  the facts). Do not add many new notes; about 0–2 per page is the norm.
- Escape `%` `&` `#` as `\%` `\&` `\#`. Quotation marks: “ ” and ‘ ’. Dashes: — and –.
- Do not write `\noindent`, page markers ⟦…⟧ or paragraph breaks: the generator adds them.

## 5. Special blocks

Translate a special block **whole**, keeping its LaTeX structure: the same lines, sizes and
macros as the Latin block (`\dispcaps`, `\lital`, `\litsw`, `\small`, `\\[2pt]`, `\vspace`,
`\raggedleft`, tabular/brace constructions), with the English text in place of the Latin.
The Chinese edition's block shows how the same structure was carried into another language.

## 6. Glossary (use consistently)

| Latin | English | note |
|---|---|---|
| perspicillum | spyglass | the word *telescopium* did not yet exist; never "telescope" in the text |
| specillum; perspicilla (the lenses) | lens(es) | by context |
| organum, instrumentum | instrument | |
| stellae fixae, inerrantes | fixed stars | |
| planetae, stellae vagae / erraticae | planets, wandering stars | *vaga sidera* = wandering stars |
| Medicea Sidera; planetae Medicei | Medicean Stars; Medicean planets | |
| Iuppiter | Jupiter | the dedication's pun on the god and the planet works in English as in Latin |
| Luna; Tellus, Terra; Sol | the Moon; the Earth; the Sun | capitalised |
| Galaxia, Lacteus Circulus | the Milky Way (the Galaxy) | |
| stellae nebulosae | nebulous stars | |
| Nebulosa Capitis Orionis | the Nebula of Orion's Head | a cluster near λ Ori, not M42 (see the Chinese note) |
| Praesepe; Aselli | Praesepe (the Beehive); the Aselli (“the Little Asses”) | |
| Pleiades | the Pleiades | |
| Cingulum et Ensis Orionis | the Belt and Sword of Orion | |
| maculae magnae / antiquae | the large or ancient spots | |
| terminus (lucis et tenebrarum) | the boundary (between light and darkness) | not "terminator" |
| coniunctio (of the Moon) | conjunction | |
| ecliptica; zodiacus | the ecliptic; the zodiac | *iuxta longitudinem zodiaci* = along the length of the zodiac |
| minutum (primum); secundum | minute; second (of arc) | |
| hora noctis prima | the first hour of the night | Italian hours, counted from sunset; the note is on f. 17r (p030) |
| orientalis / occidentalis | eastern / western | Ori. / Occ. in the figures stay untranslated |
| miliaria Italica | Italian miles | |
| Cosmus Medices II; Magnus Etruriae Dux | Cosimo II de' Medici; Grand Duke of Tuscany | |
| Florentia, Venetiae, Patavium | Florence, Venice, Padua | |
| philosophi | philosophers | |

New terms you decide on: list them at the end of your notes file.

## 7. Notes file

Write `work/notes/en_partN.md`: range done, check result, new glossary decisions, passages
where you were unsure (key + why), and footnotes you added or dropped compared with the
Chinese edition.
