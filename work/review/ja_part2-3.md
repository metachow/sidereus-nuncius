# Proofreading: ja part2 (p015–p022) and part3 (p023–p028, f16ar.2, f16br.1)

Checked every entry against the Latin, with the English and Chinese editions beside it.
Checks: `check_translation.py ja text/ja/part2.yaml p015 p022` → OK (43/43);
`... text/ja/part3.yaml p023 p028` → OK (44/44).

Both translations were sound overall. The geometry in p020.10 and p022.02–p022.05 (letters ABC/DEG/F/DA/EB; CAF, E, CF, A, EA, GCD, D; numbers 2:7, 7000, 2000, 1000, 100, 1010000, 1004, 4) matches the Latin exactly. Most corrections bring the terms into line between the two files and apply the rulings.

## Substantive corrections

### part2
- **p015.02** 斑点が無数にあって → 斑点がおびただしくあって (*magna copia* means a great number, not countless).
- **p015.03** 私は…一つ残らず例外なく次の点で一致 → われわれは…どれもみな、つねに次の点で一致 (*adnotavimus*: Galileo's plural; *semper* had been dropped).
- **p016.03** …照らされているではないか。 → …？ (ruling 5: the Latin is a question).
- **p016.04** これらの山の中腹やもっと広い部分が照らされる…つながるではないか。 → 同じ山々の中ほどの、より広い部分が照らされて光は広がり、ついに太陽が昇ると…つながるではないか？ (*mediae et largiores partes* names one group of parts, not two; the Latin is a single question, ruling 5).
- **p016.12** 私が気づいた → われわれが気づいた (*observavimus*).
- **p017.01** いくぶん黒みを帯びた縁 → ひときわ黒い縁 (*nigrioribus*: darker. "Somewhat blackish" weakened it).
- **p018.01** 両方の弦の近くで…上に掲げた二番目の図 → 上弦と下弦のどちらのころにも…上に掲げた第二組の図. Footnote adjusted to match: 「第二組の図」…二枚の図 (*in secundis figuris* is plural: two drawings, [9v] and [10r]. 「二番目の図」 read as a single figure).
- **p019.01** 斜めに当たるか否かに応じて → より斜めに当たるか、それほど斜めでなく当たるかに応じて (*magis aut minus obliqui*: a matter of degree, not yes or no).
- **p020.02** …見えるのか。 → …見えるのか？ (ruling 5).
- **p020.04, p020.08, p020.09, p020.10** 月の物体 → 月の本体 (*lunare corpus*); p020.09 月の固体 → 月の固い本体 (*soliditas*). Same term in p024.13 (part3).
- **p020.08** Moved the parenthesis so it qualifies 不透明 as in the Latin. Added a short note on アイテール (*aether*) at its first occurrence: the fifth element filling the heavens above the Moon in Aristotelian natural philosophy. This is a standard fact, and the term is used again in part3 and part5.
- **p020.09** とくに自ら輝いているとき → とくに光を帯びているときには (*luminosus exsistens* means lit by the Sun. 自ら輝く implied light of its own, which contradicts the argument).
- **p022.06** 1マイルにさえほとんど達する山は一つもない → 1マイルに近づく山さえ一つもない (the old wording was garbled: "no mountain that almost reaches even one mile").

### part3
- **p023.01** 私が最近見つけた → われわれが最近見つけた (*a nobis*; *duxi* stays without a subject).
- **p024.01** 天空のより暗い背景 → アイテールそのもののより暗い背景 (*ipsius aetheris*, kept consistent with p020.08 and part5 p081.11). Footnote: 「地照」（灰色の光ともいう） → 「地球照」 (the usual Japanese term; the remark about the English name was dropped, as the guidelines ask).
- **p024.03** 障害物を…置き → 屋根や煙突…によって角が隠され…という位置を選ぶならば (the Latin says to choose a position from which an existing roof or chimney hides the horns, not to set up an obstacle).
- **p024.04** 60度の離角かそれ以下の離角 → 離角が60度かそれより小さいとき; 精巧な → 精確な (*exacti*, as in part4 p031.03). The footnote is rewritten: the reading 「矩（くく）」 was wrong and is now 矩（く） (ruling 6). The note now says that 上弦・下弦 render the Latin "first/second quadrature" (90°) and that "60度" renders *sextilis*. The coined term 六分一の位置 is gone.
- **p024.05** 自然を探究する人々 → 哲学する人々 (ruling 7. Here the learned who put forward theories are meant; this matches part5 p081.09 正しく哲学する人々).
- **p024.08** 青銅のような色 → 銅のような色 (*aeneus*, describing the reddish eclipse light).
- **p024.11** 六分一の位置以内…いるだろうか。 → 離角が60度以内のときに…わからないほど無知な者がいるだろうか？ (now one question, as in the Latin; ruling 5; the sextile wording now matches p024.04).
- **p024.12** 矩に向かって…矩を過ぎて → 弦に向かって…弦を過ぎて (ruling 6: the phase of the Moon).
- **p024.13** 地球のほかにもう一つの天体が残されているわけでもない → もはや地球のほかに残っている天体は一つもない (the old wording was ambiguous; the Latin means "no other body remains except the Earth"). The four questions now end with ？ (ruling 5); *quaeso* is rendered as いったい; 月の天体 → 月の本体.
- **p024.16** 矩に近づく → 上弦に近づく (ruling 6; the passage describes the waxing Moon).
- **p024.17** 等しい秤で返される → 等しい重みで報いている (*aequa lance*; the old wording was translationese).
- **p024.19** 四分円 → 四分円（90度）.
- **p024.20** 太陽の衝の位置 → 太陽に対して衝の位置; 食を起こす → 月食となる.
- **p025.02** 四、五倍にしかしないとしか思えない → せいぜい四、五倍にしか拡大しないと思える (the old wording had a doubled しか).
- **p025.03** 自由な、生まれながらの目の力; いくつもの輝きに照らされ → 何にも妨げられない自然のままの目の力; ある種のぎらつく輝きに包まれ (*fulgoribus irradiata* means surrounded by glare, not lit from outside).
- **p026.04, p028.03, f16ar.2** 星の集まり → 星群 (*asterismus*. The caption now reads 「\tremph{オリオン}の帯と剣の星群」. In part4, 星の集まり stays for *congeries/coetus*).
- **p026.05** 帯…剣…は、古くから記録されているので → ずっと以前から記録されていた帯の三つの星と剣の六つの星に (the Latin does not say "because").
- **p026.06** 私は三十六 → われわれは三十六 (*nos adnotavimus*).
- **p027.01** 私が観察した → われわれが観察した (*a nobis*); 長い世紀にわたって → 幾世紀にもわたって.
- **p028.01** 天空のあちこち → アイテールのあちこち (*per aethera*).
- **p028.02** 小ささのためか、…はなはだしい遠さのために → 小さいため、あるいは…非常に遠く離れているために (smoother Japanese).

## Rulings applied
- 5 (？ after questions): p016.03, p016.04, p020.02, p024.11, p024.13.
- 6 (*quadratura*): the phase is 上弦・下弦/弦 throughout both files; 矩（く） appears only in the p024.04 footnote, with the reading corrected. No case in this range is *quadratura* as an aspect between bodies.
- 7 (*philosophantes*): p024.05 is now 哲学する人々.
- 8 (footnotes): the footnotes were checked against the Chinese and English notes; one new note (アイテール at p020.08).
- 10 (観測/観察): *observare/observatio* → 観測 in p016.06 (twice), p019.01, p022.01, p023.01 (twice), p025.01, p027.01, p028.03; p022.02 already had 観測. p020.04 観察者 (*oculus aspicientis*) is kept, as the ruling allows; *inspecta* (p025.01) stays 見た; *adnotavimus/observavimus* in the sense "noticed" (p015.03, p016.12) stays 気づいた.
- 12 (numerals): p022.02 2対7 → 二対七, and in its footnote 3対11 / 2対7 → 三対十一 / 二対七. The computed figures (7000, 2000, 1000, 100 miles; 1010000, 1004, 4) and the measured value 1.5〜1.7 km stay in Arabic numerals. The magnifications in p025.02 (百倍、四、五倍) were already in kanji, and so were the fractions (二十分の一).
- 1, 2, 3, 4, 9: nothing in this range.

## Terms made consistent across part2 and part3
macula 斑点; cavitas/lacuna くぼみ (くぼ地 for terrestrial hollows and the great round crater); eminentia 高まり, tumor 隆起; orbis vaporosus 蒸気の球層; aether アイテール; caelum 空/天空; corpus lunare 月の本体; quadratura 上弦・下弦/弦; elongatio 離角; oppositio 衝 as a position (p024.20), 満月 as a phase (p018.02); asterismus 星群; perspicillum 遠眼鏡.

## Open questions
1. p024.13 has several questions in a row, separated by ？ plus a full-width space (　). This is standard Japanese typesetting and the file compiles, but no other ja file uses a full-width space yet. The editor should confirm the convention for all parts.
2. Star counts: part3 writes them in kanji (五百, 八十, 四十, 三十六), but part4 p029.01 and p030.01 write 21個 and 36個. One style should be chosen for counts.
3. p024.22 *sexcentis* is kept as the literal 六百もの (the English edition keeps "six hundred"); the alternative is the idiomatic 数えきれないほどの.
4. *sextilis*: the text now gives 離角が60度 and the Latin term goes in the note. If the editor prefers a term in the text, 六分 could be used, but it is easily misread as "6 minutes".
5. Outside my range: part1 p014.03 has 窪み (窪 is not a 常用 kanji; part2 writes くぼみ). part5 p081.11's footnote says 「14葉裏を参照」, which breaks ruling 1 and should read [14v].
