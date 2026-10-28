# Japanese: page markers in sentences that cross a page (§8)

48 sentences, 48 marked. `≈` = the Japanese order made the split approximate (some Latin
words before the break land after the marker in Japanese, or the reverse); the note says
which. Unmarked = the Japanese before the marker renders essentially the Latin before the break
(at most a word or two of order difference).

Text changes beyond inserting the marker (three entries):
- p002.10: the footnote (天の中央の要／東の角) moved from the end of the entry to the end of the
  first Japanese sentence, so it stays on page 3r with the phrase it explains.
- p013.06: one clause reordered into two sentences: 「まず月を間近に眺めた。⟦6v⟧地球の直径の二倍ほどしか離れていないかのようであった。」 (was 「まず月を、地球の直径の二倍ほどしか離れていないかのように、間近に眺めた。」).
- p020.10: a 、 added after the subject: 「月の本体ABCが、⟦13r⟧蒸気の球層DEGに取り巻かれている。」

## part1.yaml

| key | marker | placement |
|---|---|---|
| p002.01 | ⟦2v⟧ | 石や金属にではなく、⟦2v⟧ムーサたちの守護と |
| p002.06 | ⟦3r⟧ | あたかも舌のように、⟦3r⟧殿下のこのうえなく卓越した徳を |
| p002.10 | ⟦3v⟧ | 大気の中に注ぎ出したのです。\footnote{…}⟦3v⟧それは、柔らかな小さいお体が (Latin *ut universam* falls before) |
| p002.16 | ⟦4r⟧ ≈ | ご祖先のことはさておくとしても、⟦4r⟧もっとも偉大な英雄よ (relative clause precedes its noun in Japanese, so *historiarum monumenta testantur* lands before) |
| p009.01 | ⟦5v⟧ | 見るも楽しいことである。⟦5v⟧こうして月の直径は (*per duas tantum easdem dimensiones distaret* lands before) |
| p012.01 | ⟦6r⟧ | 考え出すきっかけを、⟦6r⟧私はまず手短に述べ |
| p013.06 | ⟦6v⟧ | まず月を間近に眺めた。⟦6v⟧地球の直径の二倍ほどしか (reordered, see above) |
| p013.13 | ⟦7r⟧ | しかしレンズを置くと、⟦7r⟧屈折した線ECH、EDIに沿って |
| p014.01 | ⟦7v⟧ ≈ | 向いている月の面について、⟦7v⟧まず述べよう。 (*vergit* lands before) |

## part2.yaml

| key | marker | placement |
|---|---|---|
| p015.02 | ⟦8r⟧ | 小さな斑点がおびただしくあって、⟦8r⟧暗い部分からは (*exiguarum copia* lands before) |
| p016.06 | ⟦9r⟧ | 小さな尖りが輝き始めた。⟦9r⟧そうするうちに (*exiguae lucere coeperunt* lands before) |
| p016.11 | ⟦9v⟧ ≈ | 見えるにちがいないと、⟦9v⟧一度も疑ったことがない。 (Latin after the break is only *daturam*; Japanese puts the main verb last, so *mihi dubium fuit numquam* lands after) |
| p019.01 | ⟦11v⟧ | 大きな斑点にも、⟦11v⟧図に記したとおり、 (*exsistunt quidem* lands after) |
| p020.02 | ⟦12r⟧ | 東の半円周が、⟦12r⟧そして満月では |
| p020.06 | ⟦12v⟧ ≈ | 広がっているように見える。⟦12v⟧波の間には (*idem planum videntur extensi* lands before) |
| p020.10 | ⟦13r⟧ | 月の本体ABCが、⟦13r⟧蒸気の球層DEGに (、 added) |
| p022.02 | ⟦13v⟧ | CFは2000、⟦13v⟧CEは1000となり |
| p022.05 | ⟦14r⟧ | ある頂を表しており、⟦14r⟧4イタリア・マイルを超える高さ (*eminentior est* lands after) |

## part3.yaml

| key | marker | placement |
|---|---|---|
| p024.03 | ⟦14v⟧ ≈ | 輝く角そのものが隠され、⟦14v⟧月の球の残りの部分は (*si quis talem sibi eligat situm* = 位置を選ぶならば lands after, verb-last) |
| p024.09 | ⟦15r⟧ | わかる。すなわち、⟦15r⟧月をぐるりと取り巻く (*radiorum solarium* lands after) |
| p024.16 | ⟦15v⟧ | 地球をかすかに照らす。⟦15v⟧月が上弦に近づくにつれて |
| p024.21 | ⟦16r⟧ | もっとも強く照らされる時期には、⟦16r⟧逆に月が |
| p025.04 | ⟦16v⟧ | 次の事実からたやすくわかる。⟦16v⟧日没の最初の薄明 |
| p026.02 | ⟦16a\,r⟧ | at the end, after the footnote (as in the Latin) |
| p028.01 | ⟦16b\,v⟧ | 遠眼鏡を向けるなら、⟦16b\,v⟧密集した星の群れに |

## part4.yaml

| key | marker | placement |
|---|---|---|
| p032.02 | ⟦17v⟧ | at the end: 次のようであった。⟦17v⟧ |
| p033.04 | ⟦18r⟧ ≈ | 木星のせいにはまったくできないと悟った。⟦18r⟧さらに、 (*nulla ratione reponi posse intellegerem* lands before) |
| p035.01 | ⟦18v⟧ | 次のように並んでいた。⟦18v⟧東の星は |
| p038.02 | ⟦19r⟧ | 三番目の星は、⟦19r⟧わずかに北へ |
| p040.02 | ⟦19v⟧ | 東の星はただ一つで、⟦19v⟧木星から3分 |
| p042.04 | ⟦20r⟧ ≈ | 第5時には、この星が、⟦20r⟧木星と東の星の間の (*manifeste vidi* = はっきり見えた lands after) |
| p043.06 | ⟦20v⟧ | わずかに南へそれて、⟦20v⟧もっとも西の星から10秒 |
| p045.07 | ⟦21r⟧ | at the end: 1分20秒であった。⟦21r⟧ |
| p047.04 | ⟦21v⟧ | しかし第6時には、⟦21v⟧星は二つしか現れず (*duae* lands after; footnote stays with the 配置 phrase) |
| p050.01 | ⟦22r⟧ | 日没後第1時には、⟦22r⟧小さな星がただ一つだけ (*unica tantum* lands after) |
| p053.03 | ⟦22v⟧ | 東の二つの星は、⟦22v⟧互いにいっそう近づいていた (*viciniores* lands after) |

## part5.yaml

| key | marker | placement |
|---|---|---|
| p056.01 | ⟦23r⟧ | 1分30秒離れ、⟦23r⟧木星にもっとも近い西の星は |
| p059.01 | ⟦23v⟧ | 二つの星だけが現れ、⟦23v⟧木星をあいだにはさんでいた |
| p062.01 | ⟦24r⟧ | 東の星が二つ、⟦24r⟧西の星が一つあり |
| p064.03 | ⟦24v⟧ | 第四の星が見えた。⟦24v⟧ほかの星より小さく |
| p066.03 | ⟦25r⟧ | 西の二つのうち、⟦25r⟧木星から遠いほうの星は |
| p068.01 | ⟦25v⟧ | 東の星は木星から7分、⟦25v⟧木星は西の次の星から5分 |
| p070.04 | ⟦26r⟧ | 次の星から3分、⟦26r⟧次の星は木星から1分50秒 |
| p074.02 | ⟦26v⟧ | 木星からの距離も等しく、⟦26v⟧4分であった (*aequales* lands before) |
| p076.01 | ⟦27r⟧ | 木星にもっとも近い星は30秒、⟦27r⟧西の次の星は2分30秒 |
| p078.01 | ⟦27v⟧ | 四つの星が見え、⟦27v⟧すべて東にあった |
| p080.01 | ⟦28r⟧ | 記録をここに添えたのは、⟦28r⟧それによって、 |
| p081.05 | ⟦28v⟧ | 四つのさまよう星を示している。⟦28v⟧しかもそれらすべてが (*offert stellas* lands before) |
