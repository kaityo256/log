---
title: "2018年11月26日"
date: 2018-11-26T00:00:00+09:00
lastmod: 2018-11-26T00:00:00+09:00
type: diary
source_month: "d201811.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

最近、太ももに肉がついて悲しい。

　LaTeXiT(Ver 2.11.0)が動かなくなった。おそらくMojave関連だろう。
TexLive (MacTex 2018)を再インストールしてみる。
<a href="https://qiita.com/khys/items/c47d73af8993890cb9e5">ここ</a>を参考に。

```sh
$ brew cask install mactex
==> We'll set permissions properly so we won't need sudo in the future.
```


なんだこりゃ？いつかsudo不要にするけど、今は要るからごめんねってこと？

　あまり理解していないがこれもやってみる。

```sh
$ sudo tlmgr update --self --all
[  1/601] auto-remove: fontloader-luaotfload ... done
[  2/601, ??:??/??:??] update: a2ping [69k] (46893 -> 49161) ... done
[  3/601, 00:15/40:58:55] update: aastex [724k] (39929 -> 47692) ... done
...
```

　おおぅ、これは時間かかりそうだな・・・。

  アップデート終わったが、LaTeXitがまだ使えない。悲しい・・・。

  miがMojaveでobsoleteだという表示が出たので最新版にアップデートしたのだが、大幅にデザインが変わっていて慣れない。
結局このHTMLもVSCodeで書くことにした。
もういい加減、ここも生HTMLではなくてMarkdownかなにかで書くかなぁ・・・。

  VSCodeにLaTeX Workshop入れた。ついでにlatex-previewを入れようとしたが、なぜか動作せず。
LaTeX WorkshopにPDF Preview機能がついており、それがちゃんと動作したのでvscode-pdfをアンインストール。
Markdownのリンク先のPDFが開けなくて困りそうな気もするが・・・。

  どうでもいいが、Qiitaその他でMarkdownのプレビューは右にあっても全く違和感ないのに、なぜかLaTeXに関してはプレビューが左にあって欲しいなぁ。なぜだ？とりあえず右プレビューに頑張って慣れるか・・・。

  もう一度gdbチャレンジ。

```sh
$ git clone --depth=1 git://sourceware.org/git/binutils-gdb.git 
$ cd binutils-gdb 
$ ./configure --disable-intl --prefix=$HOME/local
$ make all-gdb
```

  駄目だ。有象無象のエラーが出てきてどうにもならない。
