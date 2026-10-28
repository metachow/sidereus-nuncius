# A：f01r–f06r 工作记录

## 完成情况

| 叶 | 扫描 | 内容 | check_folio |
|---|---|---|---|
| f01r | 0005 | 书名页（印刷商标用 `\placeholderfig` 占位） | OK |
| f02r | 0007 | 献词抬头 + 献词开头（页首花边占位）…`non saxis ac metallis,` | OK |
| f02v | 0008 | `sed Musarum custodiae`…`quae tamquam linguae praestantissimas` | OK |
| f03r | 0009 | `virtutes tuas`…`ut universam` | OK |
| f03v | 0010 | `illam vim`…`quorum gloriam sempiternam omnium` | OK |
| f04r | 0011 | 献词结尾、日期、署名 | OK |
| f04v | 0012 | 出版许可（意大利文，`\selectlanguage{italian}`） | OK |
| f05r | 0013 | ASTRONOMICUS NUNCIUS 标题（花边占位）+ 引言…`tam ex propinquo intueri, ac si` | OK |
| f05v | 0014 | `per duas tantum easdem dimensiones`…`excogitandi occasionem` | OK |
| f06r | 0015 | `prius breviter commemorabo`…`ac Lunam prius tam ex propinquo sum intuitus,`；中文把整句译完，到“……只有不到两个地球直径那么远。” | OK |

扫描 0006（第 1 叶背面）是空白页，没有建文件。装饰首字母（2r 的 P，5r 的 M）没有占位，正文按普通段落排。

## 新增术语、人名的译法

- Serenissimus → 至尊的；Celsitudo tua → 殿下；Princeps → 君主；Maximus Heros → 最伟大的英雄
- Magnus Etruriae Dux IIII → 第四任托斯卡纳大公
- Patavinum Gymnasium, publicus mathematicus → 帕多瓦大学，公共数学教授
- Thomas Baglionus → 托马索·巴利奥尼（印刷商）；Superiorum permissu et privilegio → 经上级许可，并享有出版特许权
- Iacobus Badovere → 雅克·巴多维尔；Lutetia → 巴黎；nobilis Gallus → 一位法国贵族
- Iovis, Martis, Mercurii, Herculis（2v，指神话英雄）→ 朱庇特、玛尔斯、墨丘利、赫拉克勒斯；3r 以后凡指天体或占星术中的 Iuppiter，一律译“木星”（包括 `tamquam Iove digna proles` → “犹如无愧于木星的子嗣”）
- Iulium sidus → 尤利乌斯之星；cometae / crinitae → 彗星 / 长发星
- siderum Opifex → 星辰的创造者；medium caeli cardo → 中天；orientalis angulus → 东方的宫角
- erraticae stellae, vagantes → 行星（照术语表）
- 意大利文：Capi dell'Eccelso Consiglio de' X → 十人议会首领；Riformatori dello Studio di Padova → 帕多瓦大学督学；Inquisitor → 宗教裁判官神父；Secretario del Senato → 元老院秘书；Con. Blasph. Coad. → 渎神罪执行官署助理官员（属推测，见下）
- 人名：Gio. Maraviglia → 乔瓦尼·马拉维利亚；M. Ant. Valaresso → 马尔科·安东尼奥·瓦拉雷索；Nicolò Bon → 尼科洛·邦；Lunardo Marcello → 卢纳尔多·马尔切洛；Bartholomaeus Cominus → 巴尔托洛梅奥·科米诺；Ioan. Baptista Breatto → 乔瓦尼·巴蒂斯塔·布雷亚托；“D.” → 先生／阁下

## 异文及处理（行末均有 `% 1610:` 注释）

采用 Favaro 校改的明显误印：
- 2r `HAETRURIAE` → Etruriae
- 2v `in qua` → in quae；`coaptare` → cooptare
- 3v `MEDICAEA SYDERA` → \textsc{medicea sidera}
- 5r `aequidem` → equidem；**`diametros` → semidiametros**（在中文栏加了脚注说明）
- 5v `milllbus` → millibus；`ad Monitos` → admonitos
- 6r `sexageties` → sexagesies（Favaro 的读法；古典形式应作 sexagies，见待定问题）

以初版为准：
- 5v 初版作 `quam dum libera tantum acie spectatur`，Favaro 多一个 `oculorum`。按初版不录 `oculorum`。
- 2v `vi, tempestate ac vetustate`：Favaro 无逗号，按初版加逗号。

按规范统一拼写（不另出注）：Sydera → sidera，tanquam → tamquam，inclyto/inclito → inclito，authoritatis/Author → auctoritatis/auctor，extinguatur → exstinguatur，ocium → otium，Quo circa → Quocirca，intelligeret → intellegeret，iocundissimum/iocundum → iucund-，Galaxya → Galaxia，substulisse → sustulisse，assequutus → assecutus，literas → litteras，Marittima → maritima，plusquam → plus quam，patritio → patricio，aërem → aerem。Lacteus Circulus 照术语表大写。

意大利文页（4v）只做最小规范化：长 s、u/v、& → e、ij → ii、ę → ae；展开了 Ecc. Cons.、Sig.、Reuer. P.、Circ:、&c.、Regist.；`hauuia`（误印）作 havuta；`à` → a。人名缩写和 `off.`、`Con. Blasph. Coad.` 照录。书名保留初版拼法 \textsc{sydereus nuncius}。

## 需要主编决定的问题

1. **页眉**：`\folium` 给每页都加了 RECENS HABITAE / OBSERVAT. SIDEREAE 页眉和叶码，但初版书名页、献词（2r–4r）、出版许可（4v）、5r 都没有页眉。是否在这些页加 `\thispagestyle{empty}` 或另设页面样式？我没有改动。
2. **f01r 版面**：只做到内容完整、正好一页，大字号部分用了临时字号，等主编统一设计。
3. **f01r `patricio`**：初版作 PATRITIO，我改成了古典拼法 patricio。如果主编希望书名页照录原拼法，请改回。
4. **f06r `sexagesies`**：初版 sexageties，Favaro sexagesies，古典形式 sexagies。暂从 Favaro。
5. **f05v `oculorum`**：按初版删去了 Favaro 的 `oculorum`。Favaro 可能另有依据（比如伽利略的手校本），请核实。
6. **f05r 脚注**：说明了 diametros/semidiametros 的问题。f06r/f06v 的“两个地球直径”初版和 Favaro 都作 diametros，没有另外出注。
7. **面积放大率**：“近三倍、大九倍”第一次出现在 f06r，但解释面积放大率的脚注在 f06v（主编样张）。是否把那条脚注提前到 f06r？我没有重复加。
8. **f04v 职衔**：`off. Con. Blasph. Coad.` 的展开与译法（渎神罪执行官署助理）是推测，脚注里用了“大约”。f04v 脚注 1 说督学“负责书籍出版前的审查”，也请核实措辞。
9. **f06r 脚注**：说巴多维尔曾在帕多瓦随伽利略学习，这是通行说法，请主编确认是否保留。
10. **两位“朱庇特”**：2v 列举英雄时译“朱庇特”，3r 以后一律译“木星”，`Iove digna proles` 的神话双关因此没有译出。是否需要加注？
