# Proofreading: text/ja/part1.yaml (p001–p014 and blocks f01r.1, f01r.2, f02r.1, f04r.4, f04v.3–6, f05r.1)

Check: `check_translation.py ja text/ja/part1.yaml p001 p014` → "OK, no problems" (f05r, f05v run long, for information).

## Substantive corrections

### Accuracy
- **p002.09** *ex benignissimo Iovis astro, secundum Deum omnium bonorum fontem*: 「神に次ぐあらゆる善の源である、いとも恵み深いユピテルの星」 → 「あらゆる善の源である神に次いで、いとも恵み深いユピテルの星」. *fontem* is accusative and agrees with *Deum*: God is the source of all good, and Jupiter comes after him. The old wording made Jupiter the source. Also restructured the broken *quis ignorat … quis, inquam, ignorat* period: the tacked-on 「誰が知らないと申せましょうか。」 is now 「誰が、そう、いったい誰が知らないでしょうか？」 at the end of the one sentence.
- **p002.05** *stellam suo tempore exortam*: 「カエサルの時代に現れた星」 → 「（アウグストゥスは）自分の時代に現れた…星」. *suo* refers to the subject of *voluisset*, which is Augustus. Also 「これほどの願いの望みを裏切った」 → 「あれほど切なる望みを裏切ってしまった」.
- **p005.01** *nel libro intitolato SYDEREUS NUNCIUS, etc.*: 「『星界の使者』ほかには」 ("in the Sidereus Nuncius and other things") → 「『星界の使者』等と題する書物には」. The "etc." shortens the long title. *Riformatori*: 「改革委員」 → 「パドヴァ大学監督官」 (the footnote gives the literal sense 改革官). The footnote was changed to match.
- **f01r.1**: 「パドヴァ大学公式数学者」 → 「パドヴァ大学の数学教授」 (ruling 3). The second verb 「四つの惑星に見いだしたものである」 → 「…において観測したものである」 (the Latin has one *observata sunt* for both). 「に観測した」 → 「において観測した」. *Iovis* has `\capsemph` in the Latin, so it is now `\tremph{木星}`. The Latin's last display line *nuncupandos decrevit* was missing (the old text ended with 「さらに次のように名づけることを決めた。」 before メディチ星), so a line 「\zhdisp[10.5]{と名づけることに決めた。}」 now follows メディチ星, as in the Latin. *longeque admirabilia*: added 「このうえなく」.
- **f05r.1**: the old text 「新たになされた観測を、新しい遠眼鏡の力により…について行い、これを載せ、かつ明らかにする」 brought in an extra verb (行い) and had a broken construction. It is now in Japanese order with the same five lines and macros as the Chinese block: 「新しい遠眼鏡の力によって、月の面…これまで一度も見られたことのない、／メディチ星／と名づけられた四つの惑星について／新たに行われた観測／を収め、かつ明らかにする。」
- **f02r.1**: the lines are now in Japanese order: いとも晴朗なる／第四代トスカーナ大公／コジモ二世・デ・メディチ殿下に (was name, then title + に).
- **p002.10** *orientalemque angulum sua regia illustrans*: 「東の角をその王宮で照らし」 → 「その王宮から東の角を照らし」. Some wording smoothed.
- **p002.13**: 「ほとんどそれ以外のことを思わず」 referred forward to a clause that came later. Recast as one period ending in ？: the thing he thinks of day and night is "to be known as most eager for your glory and as grateful as possible". 「されば」 → 「それならば」.
- **p002.16**: the clumsy 「…証言しておりますので申すまでもなく」 → 「…殿下の尊いご祖先のことはさておくとしても」. *Maxime Heros* is now a vocative (「最も偉大な英雄よ」).
- **p002.06** *veriora ac feliciora*: 「真実に近く」 → 「はるかに確かで」. *vix dum … cum*: 「光りはじめたばかりであるのに」 → 「輝きはじめるやいなや」.
- **p002.08**: the added 「私が決めたのは…からです」 → 「…星々の造り主ご自身が…私に促してくださったように思われます」, closer to the Latin and with the honorific for God.
- **p001.01**: *institutum* 「企て」 → 「慣わし」. The redundant 「不朽の名にふさわしいその名」 → 「不滅に値するその人々の名」. 「優れた…すぐれた」 → 「徳において卓越した人々の輝かしい事績」.
- **p001.02**: 「星々にまで達する巨費を投じて」 (the money reaching the stars) → 「巨費を投じた円柱やピラミッドが星々にまで届くほど高く築かれ」 (Propertius: the costly pyramids raised to the stars).
- **p002.02**: *invidiosa vetustas* 「妬み深い老い」 → 「妬み深い歳月」, in the text and the Ovid note. 「標」 → 「しるし」. *commemoro* 「思い起こす」 → 「申し上げる」.
- **p013.02**: *vitrea duo perspicilla*: 「ガラスの」 was missing and is restored. Footnote: Badoer is 「バドエル」, not 「バドアー」.
- **p013.02, p013.04, p013.09, notes**: 「3倍近く」「20倍近く見せる」 read naturally as "nearly 3/20 times". Now 「三倍も近く」「三十倍以上も近く」「二十倍も近づけて見せる」. In the note, 「近さが三倍なら」.
- **p013.09** *pellucida*: 「透明に」 → 「明るく」.
- **p009.01**: 「月の天体を」 → 「月の本体は」. The dangling 「肉眼だけで見る場合に比べてである。」 is now worked into the sentence. *solidum corpus* 「立体としては」 → 「体積は」. *nequaquam* (「決して」) restored. The footnote now comes after the first sentence, which it explains.
- **p010.01**: 「論争を取り除き」 → 「論争に決着をつけ」. 「小さな重みしかもたぬと考えられてはならない」 → 「決して些細なことと考えるべきではないと思われる」 (keeps *videtur*). In the note, 「（下文参照）」 (a Chinese usage) → 「（後述）」.
- **p007.02** *inauditam per aevum novitatem*: 「これまでの長い時代に聞かれたことのない」 → 「いつの世にも聞かれなかったほど」.
- **p008.01, p013.04** *naturali facultate*: 「自然の能力によって」 and 「肉眼の力」 → 「生来の視力」 in both places.
- **p013.06**: 「わずか地球の直径2個分しか離れていないかのように、それほど近くから」 → 「地球の直径の二倍ほどしか離れていないかのように、間近に」 (*vix*).
- **p013.10**: 「…うまく行うことができるからである」 (a false causal clause from *enim*) → 「これは両目を開いたまま、同時にたやすく行うことができる。」 *superficies ambas* → 「両方の図形」.
- **p013.11** *assequemur*: 「達成しよう」 (hortative) → 「果たされる」. **p013.13**: the unreal condition is now 「向かうであろう」, and *coarctantur* 「狭められ」 → 「収束させられ」.
- **p014.02**: 「斑点だらけ」 → 「まだら」. *distinguo*: 「私は」 added. **p014.03** 「哲学者の大勢」 (which can read as "the general trend of philosophers") → 「大勢の哲学者たちが」.
- **p003.01, p002.17, p002.14**: honorifics and register (「お楽しみください」 → 「どうか末永く享受なさいますように」; 「打ち勝ったのちも、なお自分自身と競い」 → 「勝たれたのちも、なおご自身と競い合い」; 「まことに正当な権利として」 → 「まったく正当なこととして」).
- **p002.04**: ヘラクレス → ヘルクレス. All the other names are Roman (ユピテル, マルス, メルクリウス), and the constellation is ヘルクレス座.
- **f01r.2**: バリョーニ → バリオーニ. 「上位者の許可」 (translationese) → 「当局の許可と出版特権を得て」. **f04r.4**: 「最も忠誠なる僕」 → 「いとも忠実なる僕」 (matches いとも晴朗なる). **f04v.6**: the footnote was rewritten for clarity (same facts).
- The treatise's 「私たち」 (p007.02, p009.01) → 「われわれ」, consistent with the rest of the treatise.

### Numbers
Following the guideline (kanji in prose for words like 二倍 and 千倍近く), magnifications and distances in p008–p013 are now in kanji (十倍, 六十倍, 二万七千倍, 三倍, 九倍, 四百倍, 二十倍, …), also in the notes. Before, Arabic and kanji were mixed inside one sentence (「ほぼ千倍大きく、30倍以上近く」). Angular minutes stay Arabic (1分か2分). In the dedication, 12年 → 十二年, like 四年間 in p002.12.

## Rulings applied
- 1: the note at p009.01 「（6葉裏）」 → 「[6v]」; the note at p013.09 「6葉表の注」 → 「[6r]の注」.
- 3: f01r.1 パドヴァ大学の数学教授.
- 5: ？ at p002.02, p002.09, p002.11, p002.13, p002.15, p002.17 (「？　」 with a full-width space when text follows in the same entry).
- 8, 9: notes end with 。. `\tremph` only where the Latin has `\capsemph` (now including 木星 in f01r.1).
- 10: checked every 観測/観察. *observare/observatio* = 観測 (f01r.1, f05r.1, p011, p012, p013.07/08/17, p014.03). *inspicere/intueri* = 観察/眺める (p007.01, p013.01/13 観察者, p009, p013.06, p014.03). No change was needed.
- 11: *mundi centrum* (p002.07 and its note) 宇宙の中心 → 世界の中心.

## Open questions
1. f01r.1: the added last line 「と名づけることに決めた。」 (\zhdisp[10.5]) is not in the Chinese block, which ends with 美第奇星. It follows the Latin's *nuncupandos decrevit.* line. Check that it fits on the title page; drop it if the editor prefers the Chinese layout.
2. Should magnifications be in kanji or Arabic numerals? I used kanji because of the guideline's example 「千倍近く」. Other parts should agree (few magnifications occur after p013).
3. p002.15 *Quod si … indagavi*: kept as a conditional (「もし…私であるならば」); it could also be read as assertive (「…私である以上」).
4. p002.10 note: 「南中点」 for the midheaven (MC) could also be 「天頂点（MC）」; I left the translator's term.
5. p002.12: *Serenissimis parentibus* is 「尊い御両親」, not the glossary's いとも晴朗なる (too heavy here). The editor may want it uniform.
