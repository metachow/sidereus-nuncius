# 校对记录：A 组 f01r–f06v

校对范围：f01r、f02r、f02v、f03r、f03v、f04r、f04v、f05r、f05v、f06r、f06v（f01v 空白，未动）。
每页都把拉丁文与扫描（0005、0007–0016）逐行对照，并与 Favaro 本（维基文库录文；有疑问处查了维基文库所附的 Favaro 第三卷页面扫描）核对。
改完后 11 页 `check_folio` 全部 **OK**，生成的 PNG 都看过，版面正常。修改前的副本在 scratchpad 里（folia_backup）。

## 各页结论与改动

| 叶 | 断页 | 改动 |
|---|---|---|
| f01r | 与初版一致 | `\folium` → `\folium*`。文字与扫描一致；`patricio` 已按 DECISIONS A3 处理。版面未动。 |
| f02r | 至 `non saxis ac metallis,`（`me-|tallis` 归本页），正确 | `\folium*`。中文“用意……充满了人情” → “做法……极富仁厚之心”（*institutum* 指做法；*humanitatis plenum*）；“耗资‘直抵星辰’” → “耗费巨资而‘直抵星辰’”。普罗佩提乌斯出处（《哀歌集》3.2.19）核对无误。 |
| f02v | 至 `praestantissimas`（`prae-|stan-`，整词归本页），正确 | `\folium*`。神话语境保留“朱庇特”。奥维德出处（《变形记》15.234）、恺撒彗星的脚注核对无误。 |
| f03r | 至 `ut universam`，正确 | `\folium*`。① *tamquam Iove digna proles* 改译“无愧于朱庇特的子嗣”，“它的身旁” → “他的身旁”，并在此加 Iuppiter 双关的脚注（DECISIONS A6）。② *ex benignissimo Iovis astro, secundum Deum omnium bonorum fontem*：原译把“仅次于上帝”拆成补句“当然，它仅次于……”，“当然”是多加的，现在合成一句：“从仅次于万善之源上帝的、最吉善的木星流溢而出”（*benignissimus* 取占星术中“吉星”之义）。③ *orientalemque angulum sua regia illustrans*：*regia* 是名词（王宫，占星术中行星的宫位），原译“以它王者的光辉”不准，改为“从它的王宫照亮东方的宫角”。本页现有 3 条脚注，排得下。 |
| f03v | 至 `omnium`（`om-|nium`），正确 | `\folium*`。*qui … sub tua dominatione sum* 是关系从句，原译把“我是殿下的臣民”当成要让人知道的内容，现在改为插入语：“只求让人知道：我——不仅在心里……都是殿下治下的臣民——最热切地渴望殿下的荣耀，对殿下的感激之深无以复加——这又有什么奇怪呢？” |
| f04r | 正确 | `\folium*`。罗马历纪日脚注（4 Idus Martii = 3 月 12 日）无误。 |
| f04v | 正确 | `\folium*`。脚注 1 改写（督学负责组织审查、凭审查人的证明出具证书；许可由十人议会首领颁发）。脚注 2 按查证结果改写（见下），中文职衔“助理官员” → “助理”。 |
| f05r | 至 `ac si`，正确 | `\folium*`。diametros 脚注补一句：伽利略手稿也作 *diametros*，当是笔误（依据 Favaro 的 Avvertimento）。 |
| f05v | 至 `occasionem`（`oc-|casionem`），正确 | “仿佛它只隔着两个这样的距离” → “两个这样的半径”（*easdem dimensiones* 指前文的地球半径；原译“距离”含糊）。oculorum 见下。 |
| f06r | 至 `sum intuitus,`，正确；中文整句归本页，符合规范 2.4 | `sexagesies` → `sexagies`（DECISIONS A3；行末已有 `% 1610: sexageties`）。在“近了三倍，大了九倍”处加面积放大率脚注（DECISIONS A4），并顺带说明“六十多倍”“近一千倍”对应的线度倍数（√60≈8，√1000≈32，与原文“近三十多倍”相合）。巴多维尔脚注按查证结果改写。 |
| f06v | 至 `appositis perspicillis,`，正确 | 脚注改为指向前注：“这里的‘倍数’同样指面积（见第 6 叶正面脚注）：放大四百倍，即线度放大二十倍。” 拉丁文 `perlucida` → `pellucida`（初版作 *pellucida*，已放大扫描确认；Favaro 作 *perlucida*，两者都是古典拼法，按“以初版为准”取初版），行末加注释。中文“看到恒星多得惊人” → “看到这些星多得惊人”（*harum* 指前面的恒星和行星）。 |

## 查证结果

### 1. f05v *oculorum*：初版确实没有，删去正确
- 本扫描（0014）放大后清楚读作 `quam dum libera tantum acie spectatur`，没有 *oculorum*。
- Favaro 第三卷第 59 页（维基文库 Pagina:Le opere di Galileo Galilei III.djvu/60，已看扫描）正文作 *libera tantum oculorum acie*，校勘记第 22–23 行注 *tantum acie*。按 Favaro 的 Avvertimento（第 10 页），页下校勘记列的是**伽利略手稿誊清本**（Mss. Gal., Par. III, T. III, car. 38 sgg.）的异文，正文则声称“忠实翻印威尼斯初版”，并且只交代了 *diametros → semidiametros* 一处改动。
- 所以初版和伽利略手稿都没有 *oculorum*。Favaro 的 *oculorum* 要么来自他所用初版的另一印次（初版有不同印次，如 Medicea 贴条），要么是他没有交代的改动。按规范第 3 节以初版为准，保留删去的处理；行末注释 `Favaro: libera tantum oculorum acie` 已有。

### 2. f04v *off. Con. Blasph. Coad.*：“渎神罪执行官署助理”的推测成立
- Horatio F. Brown, *The Venetian Printing Press* (London 1891，公有领域；archive.org 全文 venetianprinting00brow) 第 78–79 页：十人议会 1542/43 年的法令把查处无许可印刷的权力交给 Esecutori contro la Bestemmia；第 93–94 页：十人议会 **1566 年 9 月 17 日**的法令规定，凡从十人议会首领处获得印刷许可的人，付印前须把许可带到 Esecutori contro la Bestemmia 署，**登记在专册中**（免费），该署因此出具登记证明。Brown 还概括了 1562 年督学法令规定的程序：宗教裁判官、公爵府秘书、公共讲师分别出具审查证明（fede），督学秘书据以出具证书，十人议会首领颁发许可。
- 本页的 “1610, adì 8 Marzo. Registrato in libro a carte 39” 正是这种登记，签名者就是该署的人。缩写当读作 *officii contra blasphemiam coadiutor*（渎神罪执行官署助理）。*Coad.* = *coadiutor*，与威尼斯文书机构中“coadiutore”（助理书记）一职相合。没有找到 Breatto 本人的资料，这一读法是依据制度推断的，所以脚注用了“当读作”。
- f04v 脚注 1 原来说督学“负责书籍出版前的审查”，据 Brown 改得更准确。

### 3. f06r “巴多维尔曾随伽利略学习”：有一手证据，保留
- 伽利略《驳巴尔达萨雷·卡普拉的诽谤与欺骗》(*Difesa contro alle calunnie et imposture di Baldessar Capra*, 威尼斯 1607) 收有巴多维尔亲笔写的证明，日期为 “Adì 13 di Maggio 1607, in Padova”（Favaro 编国家版第二卷第 534–535 页；维基文库有录文）：“Io Giacomo Badovere Francese … sendo io, già nove anni passati, alloggiato nella propria casa et in compagnia del Sig. Galileo Galilei … et imparando da esso Galilei le scienze Matematiche …”。也就是说，约 1598 年他寄住在伽利略家中，随伽利略学习数学。
- 英文维基百科 “Giacomo Badoer (French diplomat)” 也说他 1598/99 年在帕多瓦随伽利略学数学（转引 Treccani）。
- 脚注改为：巴多维尔（又作 Giacomo Badoer）据他本人 1607 年写的证明，约 1598 年曾寄住在伽利略帕多瓦的家中，随他学习数学。

### 4. Iuppiter 双关脚注
加在 f03r *Iove digna proles* 处（这是双关最明显的地方），f02v 列举英雄时不再另加注。脚注说明：Iuppiter 既是主神之名，又是木星之名；伽利略把新星说成“朱庇特的子嗣”，又借占星术中主吉、主王权的木星颂扬科西莫，把美第奇家族与木星及其卫星联系起来。没有采用“四颗卫星对应科西莫兄弟四人”的说法，因为本书正文没有明说。
用语：神话语境（2v 英雄名单、3r *Iove digna proles*）用“朱庇特”；3r *Iovis stellam*、*Iovis astro*、*Iuppiter, Iuppiter, inquam*（星占中的行星）和其余各处都用“木星”。

### 5. 其他核对
- 断页：11 页的起止都与初版一致，跨页词（metallis、praestantissimas、omnium、occasionem、intuitus）都归开头所在页；提示词、帖号均未录入。
- 拼法：*sexagies*、*patricio*、*quattuor*、*numquam*、*repperi*、*intellego*、*exspecto* 等都已执行；本范围内没有 *miliarium* 一类词，也没有合写数词（*sex denas*、*viginti septem* 已分写，*terdenis* 是单词）。
- 1610 年的初版与 Favaro 本标点不同处（如 5v *millibus, maius*、*paucis abhinc diebus, reperta*、*nemini eorum, qui ante nos, cognitas*）属于细节，没有改。

## 仍需主编决定

1. **f06v `pellucida`**（主编样张）：已从初版改为 *pellucida*，Favaro 作 *perlucida*。两种都是古典拼法；如果主编希望拼写统一从 Favaro，请改回。
2. **f05v *oculorum***：已确认初版和伽利略手稿都没有这个词。是否需要在中文栏加一条短注，说明 Favaro 本多出此词？我认为不必，目前只在 LaTeX 注释里记录。
3. **f03r 共 3 条脚注**（十二年、Iuppiter 双关、占星术用语），排得下，但超过“每页 0–2 条”的一般标准。如果要精简，可以删去“十二年”注的第二句。
4. **f03r *sua regia***：现译“从它的王宫”（*regia* 作名词，占星术中行星的宫位）。如果主编认为应理解为“以王者之光”，请改回。
5. **f04v 签名的展开** *officii contra blasphemiam coadiutor* 依据的是制度史（Brown 1891），没有找到 Breatto 本人的直接文献，脚注措辞“当读作”留有余地。
6. f01r 书名页的标点（*philosophis atque astronomis*，初版在 atque 前有逗号）按现代习惯去掉了逗号；Favaro 录文没有收书名页，无从比对。等主编统一设计书名页时一并确定。
