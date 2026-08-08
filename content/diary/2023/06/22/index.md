---
title: "2023年6月22日"
date: 2023-06-22T00:00:00+09:00
lastmod: 2023-06-22T00:00:00+09:00
type: diary
source_month: "d202306.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

pandocを使ってmarkdownからpdfを作ると、boldsymbolが太字にならない問題、bmを使ってもうまくいかない。仕方ないのでpandocが吐いたtexソースを見て二分探索。最終的に

```latex
\usepackage{unicode-math} 
```

が問題を起こしていることが判明。

つまり、

```tex
\documentclass{ltjarticle}
\usepackage{amsmath}
\begin{document}
$$
  \boldsymbol{r} = r
$$
\end{document}
```

というファイルをつくってlualatexでコンパイルしてもボールドになるが、

```tex
\documentclass{ltjarticle}
\usepackage{amsmath}
\usepackage{unicode-math}
\begin{document}
$$
  \boldsymbol{r} = r
$$
\end{document}
```

とするとうまくいかない。

検索したら[解決策](https://tex.stackexchange.com/a/55417)を見つけた。

```tex
\setmainfont{XITS}
\setmathfont{XITS Math}
\setmathfont[version=bold,FakeBold=3.5]{XITS Math}
```

を追加するとうまくいく。ちょっとフォントが変わってしまうが。

いろいろ調べたが、結局「太字の斜体を使うな」というのが正しいらしい。`\mathbf`を使うのが正解。どうしてもやりたければ上記のworkaroundでなんとかする。

ハンズオン。バッチシステムの使い方。

研究室ミーティング。レイリーテイラー不安定性。

輪講。シャノンエントロピーとKL divergence。

[このサイト](https://linesegment.web.fc2.com/index.html)すごい。高木貞治の解析概論が丸々載っている。
