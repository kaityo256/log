---
title: "2023年1月31日"
date: 2023-01-31T00:00:00+09:00
lastmod: 2023-01-31T00:00:00+09:00
type: diary
source_month: "d202301.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

matplotlibでfontが見つからないと言われる。

```txt
findfont: Font family 'Times New Roman' not found.
findfont: Font family 'Times New Roman' not found.
findfont: Font family 'Times New Roman' not found.
findfont: Font family 'Times New Roman' not found.
findfont: Font family 'Times New Roman' not found.
findfont: Font family 'Times New Roman' not found.
findfont: Font family 'Times New Roman' not found.
findfont: Font family 'Times New Roman' not found.
```

Ubuntu系なら以下でインストールできる。matplotlibのキャッシュを消しておかないといけない。

```sh
sudo apt install msttcorefonts -qq
rm ~/.cache/matplotlib -rf
```

LaTeXで作ったPDFをChrome系(だからEdgeも)のブラウザで見るとおかしくなる現象、Ryumin-Light-Identity-Hの埋め込みが禁止されているから。

```sh
$ pdffonts.exe thesis.pdf
name                                 type              encoding         emb sub uni object ID
------------------------------------ ----------------- ---------------- --- --- --- ---------
Ryumin-Light-Identity-H              CID Type 0        Identity-H       no  no  no       5  0
WMQMSW+CMR12                         Type 1C           Builtin          yes yes yes      6  0
YZOQWI+CMR10                         Type 1C           Builtin          yes yes yes      7  0
KOIXZI+CMR17                         Type 1C           Builtin          yes yes yes     14  0
GothicBBB-Medium-Identity-H          CID Type 0        Identity-H       no  no  no      19  0
YBBHUL+CMSS10                        Type 1C           Builtin          yes yes yes     20  0
EUWIXX+CMSS17                        Type 1C           Builtin          yes yes yes     27  0
```

Ryumin-Light-Identity-Hの埋め込みがnoになってる。この代替フォントとして、普通はMS Minchoを使うが、Chromeが変なフォントを探してしまうのでおかしくなるらしい。MS Minchoを指定して埋め込めなくもないが、かなり面倒なようだ。

うーん、「スパコンを使う以上、hardware-awareなコードを書きなさい」という気持ちはすごくわかるんだけど、例えば「hardware-awareなコードを書ける計算物性科学者」にそこまでのニーズがあるのか、と言われると、ユーザに時間をかけてそのスキルを身に着けてくださいとは強く言えないような……

論文がacceptされた！長かった。

調べたら、この研究に関する最古のスライドが2012年4月。10年以上前だ……

諦めずに戦い抜いた。がんばった。
