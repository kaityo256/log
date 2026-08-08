---
title: "2021年11月12日"
date: 2021-11-12T00:00:00+09:00
lastmod: 2021-11-12T00:00:00+09:00
type: diary
source_month: "d202111.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Macでlatexdiffが走らず、WSL2で動く問題、TeXLiveのバージョンの問題だった。

[latexdiff with \cite commands gives output with apparently mismatched braces](https://tex.stackexchange.com/questions/574280/latexdiff-with-cite-commands-gives-output-with-apparently-mismatched-braces)

これはLaTeXが2020年からいくつかのパッケージに互換性のない修正を入れたから。その一つが`ulem.sty`。latexdiffは`ulem.sty`を使う。

```tex
\RequirePackage[normalem]{ulem} %DIF PREAMBLE
```

この状態で、打ち消し線`\sout`を使うとまずいらしい。回避策はいくつかあるが、簡単なのは`latexdiff`に`-t CFONT`オプションをつけること。しかし、これだとstrikeout(打ち消し線)が使えない。うーむ。

非常にad-hocだが、結局`uname`でホスト判別して、`Darwin`ならオプションをつける、という形にした。

```sh
HOST=$(shell uname)
DIFFPARAM=
ifeq ($(HOST),Darwin)
    DIFFPARAM=-t CFONT
endif

diff.tex: $(SRC)
    latexdiff $(DIFFPARAM) $(DIFFDIR)/$(SRC) $(SRC) > diff.tex
```

とりあえず自分用だからこれで良いや。

Xbyakハンズオンを僕がやることに。とりあえずDockerで動作確認しようとしたらビルドに失敗する。直さないと。

塩漬け論文修正して共著者に送ったぞ！

WSL2のUbuntuが恐ろしく遅い問題、Xにつなごうとしてタイムアウトしているっぽい。VcXsrcを起動するか、DISPLAY環境変数を消せば早くなる。なんじゃらほい。

学科分け用ビデオ作った。Zoomで緑背景にしてそれをOBS Studioで受け取ってクロマキーした。

だいぶTODOつぶしたぞコノヤロー。
