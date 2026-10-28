# Japanese translation: guidelines

The Japanese edition sets a new Japanese translation beside the same Latin as the Chinese
and English editions, page for page with the 1610 Venice print. You translate **sentence
by sentence**; the script places each sentence on the page where its Latin sentence
begins, so you do not deal with pages at all.

## 1. What you get and what you write

- See your range with `PYTHONIOENCODING=utf-8 python tools/show_range.py p015 p022 --en`.
  It prints every Latin sentence with its key (`p017.04: ...`), the English edition's
  sentence under it, the Chinese edition's text for the same passage, and any **special
  blocks** (title lines, headings, signatures) in the range. Both editions were
  proofread; their footnotes are researched.
- Write `text/ja/partN.yaml`, a flat mapping, UTF-8:

  ```yaml
  p017.04: >-
    合から四日目か五日目、月が輝く角をわれわれに見せるとき、……
  f04v.3: |-
    \vspace{0.8\baselineskip}
    ……
  ```
  One entry per Latin sentence key, no more, no fewer. Use `>-` for prose and `|-` for
  special blocks (keeps their line breaks). Never merge two Latin sentences into one entry
  or move content between entries: if Japanese wants different sentence boundaries, you may
  use several Japanese sentences inside one entry. Do not write page markers ⟦…⟧ while
  translating; they are added afterwards (§8).
- Check your file: `PYTHONIOENCODING=utf-8 python tools/check_translation.py ja text/ja/partN.yaml p015 p022`
  (completeness, LaTeX sanity, Chinese-text check, compiles your pages). It must say
  "OK, no problems". Pages "running long" are fine: page fitting is done afterwards.

## 2. Independence (essential)

Translate **directly from the Latin**. Do not consult, reproduce or paraphrase any modern
Japanese translation — 山田慶児・谷泰訳『星界の報告』（岩波文庫, 1976）, 伊藤和行訳『星界の報告』
（講談社学術文庫, 2017）, or any other — and do not reconstruct one from memory. The same
holds for modern English translations (Van Helden, Drake, Shea & Maffei). The English and
Chinese editions of this project are our own work and may be consulted for interpretation
and notes, but translate from the Latin, not from them: Japanese that reads like a
translation of the English is a fault.

## 3. Style

- Modern written Japanese, 常用漢字 and 現代仮名遣い; avoid rare kanji (write かつて, すでに,
  ほとんど, もっとも in kana where usual). Faithful, clear, readable prose; nothing added or
  dropped. Long Latin periods may be broken into shorter Japanese sentences inside the same
  entry.
- **Register**: the dedication to Cosimo II (p001–p006) in respectful 敬体 (です・ます, with
  殿下 for *Celsitudo tua*, 謙譲語 for Galileo's own acts where natural, not overdone); the
  licence (f04r/f04v) in plain official style; the treatise itself (from p007) in
  である調. Keep Galileo's tone: precise, occasionally exultant.
- Persons as in the Latin: Galileo moves between 「私」 and 「われわれ」; follow him.
- Punctuation: 、 and 。 (never ，．). Quotations 「」, quotations inside quotations and
  titles of books 『』. Use full-width ？！ only where the Latin asks a question or
  exclaims. Ellipsis ……, dash ——.
- Numbers (the text is set horizontally): Arabic numerals for dates, hours, distances and
  measures in the observations — 「12日、夜の第1時」「木星から2分離れていた」; kanji numerals
  in words and idioms (一つ、二倍、数日、十か月前、千倍近く). Ordinal hours: 「夜の第1時」.
- Proper names in the usual Japanese katakana: ガリレオ・ガリレイ、コジモ二世・デ・メディチ、
  トスカーナ大公、フィレンツェ、ヴェネツィア、パドヴァ、ネーデルラント人 (Belga)、
  ジャック・バドヴェール (Iacobus Badovere)、プロペルティウス、オウィディウス、ピュタゴラス派.
- The dedication is printed in italic in 1610; the generator sets it in the Kyokasho face
  (the Japanese counterpart of italic), so write plain text there.

## 4. LaTeX in your text

- The Latin uses `\capsemph{planetas}` for words the 1610 print sets in capitals. Mark the
  Japanese equivalent with `\tremph{惑星}`: it is printed with 傍点 (a dot over each
  character). Put only plain characters inside `\tremph{}` (no macros, no footnotes).
  Italic passages inside roman text (e.g. a Latin word quoted): `\textit{...}`.
- Footnotes: `\footnote{...}` at the end of the sentence (or phrase) it explains, after
  the 。 or 、. Take the Chinese and English editions' footnotes as the basis: translate and
  adapt them for Japanese readers (drop remarks that only concern Chinese or English terms;
  keep the facts). Do not add many new notes; about 0–2 per page is the norm. Latin words
  in notes in `\textit{}`.
- Ruby: kanji outside the 常用漢字 (噂、靄、楕円、論駁 …) and words with a special reading
  (遠眼鏡、合（ごう）、矩（く）) get `\ruby{漢字}{かな}` at their first occurrence in the book only;
  never write readings in parentheses. Prefer kana for a rare word where it reads as well.
- Escape `%` `&` `#` as `\%` `\&` `\#`.
- Do not write `\noindent`, page markers ⟦…⟧ or paragraph breaks: the generator adds them.
- Initials: write p001.01 and p007.01 as plain text (the editor adds the woodblock
  initials). p013.01 begins with a plain drop capital: write its first character as
  `\zhinitial[2]{\CJKfamily{zhsemi}X}` followed by the rest, as the Chinese edition does.

## 5. Special blocks

Translate a special block **whole**, keeping its LaTeX structure. The Japanese edition uses
the same macros as the Chinese edition (`\zhdisp[size]{..}` display lines in semibold
Mincho, `\zhital{..}` for lines the 1610 print sets in italic, `{\small ..}`, `\\[2pt]`,
`\vspace`, `\raggedleft`, the tabular/brace constructions), so take the Chinese block as
the model: the same lines, sizes and macros, with Japanese text in place of the Chinese.
Check the Latin line by line: the Chinese block shows the structure, the Latin gives the
sense.

## 6. Glossary (use consistently)

| Latin | Japanese | note |
|---|---|---|
| Sidereus Nuncius / Astronomicus Nuncius (title) | 星界の使者 / 天文の使者 | as in the Chinese and English editions (messenger); never 『星界の報告』 |
| perspicillum | 遠眼鏡（とおめがね） | the word *telescopium* did not yet exist; never 望遠鏡 in the text; reading in a note at the first occurrence (f01r title or p013.01) is enough |
| specillum; perspicilla (the lenses) | レンズ | by context |
| organum, instrumentum | 器具、装置 | by context; prefer 器具 |
| stellae fixae, inerrantes | 恒星 | |
| planetae, stellae vagae / erraticae | 惑星、さまよう星 | *vaga sidera* = さまよう星々 |
| Medicea Sidera; planetae Medicei | メディチ星; メディチ惑星 | |
| Iuppiter | 木星 (planet), ユピテル (god) | the dedication plays on the god and the planet: use ユピテル where the god is meant, and make the link explicit once (e.g. 「ユピテルの星、すなわち木星」); a short note may explain |
| Luna; Tellus, Terra; Sol | 月; 地球; 太陽 | |
| Galaxia, Lacteus Circulus | 銀河、天の川 | 「銀河（天の川）」 at the first occurrence |
| stellae nebulosae | 星雲状の星 | |
| Nebulosa Capitis Orionis | オリオンの頭の星雲 | a cluster near λ Ori, not M42 (see the Chinese note) |
| Praesepe; Aselli | プレセペ（かいばおけ）; アセッリ（「ロバの子」） | figure caption uses プレセペ星雲 |
| Pleiades | プレアデス（すばる） | |
| Cingulum et Ensis Orionis | オリオンの帯と剣 | |
| maculae magnae / antiquae | 大きな斑点 / 古くからの斑点 | |
| terminus (lucis et tenebrarum) | （明暗の）境界 | not 明暗境界線 as a technical term |
| coniunctio (of the Moon) | 合（ごう） | |
| ecliptica; zodiacus | 黄道; 獣帯 | |
| minutum (primum); secundum | 分; 秒（角度の） | |
| hora noctis prima | 夜の第1時 | Italian hours, counted from sunset; the note is at the first occurrence, p032.01 (f. 17r) |
| orientalis / occidentalis | 東の / 西の | Ori. / Occ. in the figures stay untranslated |
| miliaria Italica | イタリア・マイル | |
| Cosmus Medices II; Magnus Etruriae Dux | コジモ二世・デ・メディチ; トスカーナ大公 | Serenissimus = いとも晴朗なる; Celsitudo tua = 殿下 |
| Florentia, Venetiae, Patavium | フィレンツェ、ヴェネツィア、パドヴァ | |
| philosophi; astronomi | 哲学者; 天文学者 | |

New terms you decide on: list them at the end of your notes file.

## 7. Notes file

Write `work/notes/ja_partN.md`: range done, check result, new glossary decisions, passages
where you were unsure (key + why), and footnotes you added or dropped compared with the
Chinese and English editions.

## 8. Page breaks inside a sentence (added after the first build)

48 Latin sentences run across a page of the 1610 print; their Latin carries the page marker
(⟦2v⟧ …). Without a marker in the Japanese, the whole Japanese sentence goes to the earlier
page and the next page's Japanese column starts with a blank. So the Japanese gets the same
marker(s), at a **clause boundary** — after 、 or 。, or between two Japanese sentences inside the
entry — chosen so that the Japanese before the marker renders, as nearly as Japanese allows,
the Latin before the break. Rules:
- natural Japanese first: never inside a word, never between a modifier and its noun or a
  noun and its particle; light reordering of clauses inside the entry is allowed only if the
  Japanese stays natural and faithful;
- where the Japanese order inverts the Latin (verb last, relative clauses before the noun),
  take the clause boundary that best matches the amount of Latin on each side;
- a footnote stays attached to the phrase it explains;
- the same number of markers as the Latin sentence, same labels (`list_breaks.py ja` lists
  them; `check_translation.py` checks the count).
