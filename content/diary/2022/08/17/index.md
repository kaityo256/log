---
title: "2022年8月17日"
date: 2022-08-17T00:00:00+09:00
lastmod: 2022-08-17T00:00:00+09:00
type: diary
source_month: "d202208.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

体調はあまりよくないが、仕事はできている感じ。

いつの間にか、MacのVimの背景が白くなってしまっている。colorschemeをdefaultにするともとに戻る。今はdelek。他の場所では大丈夫なのに。とりあえずdefaultで逃げる。

おかしいcolorshemeは他にもあった。調べてみよう。

* delek (白くなってしまう)
* zellner (白くなってしまう)

特におかしいのは上記２つ。

以下の２つは、Macは背景色が適用されるが、Linuxではだめ。

* deseart (背景色がやや違う。Macは薄い黒、Linuxは黒)
* peachpuff (Macだけ背景色が適用)

なぜだ？

TERMをxtermにすると背景色が無視される。

[このissue](https://github.com/vim-jp/issues/issues/1096)が関連するのかなぁ？
