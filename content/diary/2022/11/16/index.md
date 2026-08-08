---
title: "2022年11月16日"
date: 2022-11-16T00:00:00+09:00
lastmod: 2022-11-16T00:00:00+09:00
type: diary
source_month: "d202211.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

会議その1。

TODOをばしばし潰していった。懇親会の確認とかコースディスクリプションとか。

なんか「ゼロから学ぶPython」のmakeが走らないなぁ、と思って、もう一度エラーをよく見てみた。

```sh
$ make
sed '2a [[Up]](../index.html)' about/README.md > about/index.md
sed: 1: "2a [[Up]](../index.html)": command a expects \ followed by text
make: *** [about/index.md] Error 1
rm about/index.md
```

あー、これはMacのsedがBSD系でgsedじゃないからだわ。

```sh
brew install gnu-sed
```

さて、makeが参照するsedをgsedにしたい。まともにやるなら、make内で判定するようにするのが妥当。しかし、そんなことで変な判定いれたくないし、そもそもMacでBSDのsedは使わない。

sedが`/usr/bin/`に、gsedが`/usr/local/bin/`に入っている。パスは`/usr/local/bin`を先に見るので、`/usr/local/bin/sed`として`gsed`にシンボリックリンクをはってしまえば良い。

```sh
$ cd /usr/local/bin/
$ sudo ln -s gsed sed
$ which sed
/usr/local/bin/sed
$ sed --version
sed (GNU sed) 4.9
Copyright (C) 2022 Free Software Foundation, Inc.
(snip)
```

pandocでmarkdownからHTMLにするときに「タイトルがないよ」という警告が出るやつ、これまでは`--metadata pagetitle=`で直接指定していたが、`--shift-heading-level-by=-1`を使うことでMarkdownのトップレベルのタイトル`# title`を自動取得してくれるらしい。便利。さっそく[ゼロから学ぶPython](https://kaityo256.github.io/python_zero)と[GitHub演習](https://kaityo256.github.io/github/)のHTMLを修正した。ちゃんとタイトルが反映されている。素晴らしい。

なんだ？GitHub Pagesが変なエラー出して死んだぞ。

```text
sudo apt-get install -y make pandoc
```

で死んでる。エラーメッセージはこんな感じ。

```txt
Reading package lists...
Building dependency tree...
Reading state information...
make is already the newest version (4.2.1-1.2).
make set to manually installed.
Suggested packages:
  texlive-latex-recommended texlive-xetex texlive-luatex pandoc-citeproc
  texlive-latex-extra context wkhtmltopdf librsvg2-bin groff ghc nodejs python
  libjs-mathjax node-katex
The following NEW packages will be installed:
  pandoc pandoc-data
0 upgraded, 2 newly installed, 0 to remove and 29 not upgraded.
Need to get 15.5 MB of archives.
After this operation, 125 MB of additional disk space will be used.
Err:1 http://azure.archive.ubuntu.com/ubuntu focal/universe amd64 pandoc-data all 2.5-3build2
  Could not connect to azure.archive.ubuntu.com:80 (52.252.75.106), connection timed out
Err:2 http://azure.archive.ubuntu.com/ubuntu focal/universe amd64 pandoc amd64 2.5-3build2
  Unable to connect to azure.archive.ubuntu.com:http:
E: Failed to fetch http://azure.archive.ubuntu.com/ubuntu/pool/universe/p/pandoc/pandoc-data_2.5-3build2_all.deb  Could not connect to azure.archive.ubuntu.com:80 (52.252.75.106), connection timed out
E: Failed to fetch http://azure.archive.ubuntu.com/ubuntu/pool/universe/p/pandoc/pandoc_2.5-3build2_amd64.deb  Unable to connect to azure.archive.ubuntu.com:http:
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
```

Dockerで試してみたが、Dockerのubuntu:latestでは`archive.ubuntu.com`にデータを取りに行ってるのに、Actionsでは`azure.archive.ubuntu.com`に取りに行ってタイムアウトしてるな。

もう一度実行したら通ったっぽい。

logのPandocのオプションが古いな。あとで修正しておかないと。

会議その2。
