---
title: "2022年11月17日"
date: 2022-11-17T00:00:00+09:00
lastmod: 2022-11-17T00:00:00+09:00
type: diary
source_month: "d202211.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室ミーティング。卒論、修論の日程確認。

TODOをめっちゃ潰した。

logで`--shift-heading-level-by=-1`をやると、日付がすべてH1になってしまう。アドホックだが、結局こうした。

```make
docs/%.html: log/%.md
 TITLE=$(shell head -1 $< | sed -e '1 s/^# \(.*\)$$/\1/g'); pandoc -s $< -o $@ $(PANDOC_HTMLOPT) --metadata pagetitle=$$TITLE
```

もうちょっとスマートな方法がある気がするが・・・

というわけで、HTMLのタイトルがちゃんと「2022年11月」とかになるようにした。

しかし、pushするたびに、いちいちPandocをインストールしてmakeが走るんだよなぁ。GitHub Actionsの練習としてやってみたんだけど、なんか若干もったいない気もする。まぁ、ビルド一回あたり1分かかってないから良しとするか・・・

```sh
pandoc -s vcs/README.md -o vcs/index.html --mathjax -t html --shift-heading-level-by=-1 --template=template
pandoc: unrecognized option `--shift-heading-level-by=-1'
Try pandoc --help for more information.
```

うぉ、WSLのPandocが古い。

```sh
$ pandoc -v
pandoc 1.19.2.1
Compiled with pandoc-types 1.17.0.4, texmath 0.9, skylighting 0.1.1.4
Default user data directory: /home/watanabe/.pandoc
Copyright (C) 2006-2016 John MacFarlane
Web:  http://pandoc.org
This is free software; see the source for copying conditions.
There is no warranty, not even for merchantability or fitness
for a particular purpose.
```

```sh
$ which pandoc
/home/watanabe/.pyenv/shims/pandoc
```

ん？なんでここにあるんだ？Anacondaが入れたらしい。削除。

```sh
conda uninstall pandoc
```

最新版を入れる。

```sh
wget https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-1-amd64.deb
sudo dpkg -i pandoc-2.19.2-1-amd64.deb
```

```sh
$ pandoc -v
pandoc 2.19.2
Compiled with pandoc-types 1.22.2.1, texmath 0.12.5.2, skylighting 0.13,
citeproc 0.8.0.1, ipynb 0.2, hslua 2.2.1
Scripting engine: Lua 5.4
User data directory: /home/watanabe/.local/share/pandoc
Copyright (C) 2006-2022 John MacFarlane. Web:  https://pandoc.org
This is free software; see the source for copying conditions. There is no
warranty, not even for merchantability or fitness for a particular purpose.
```

入った。これで`--shift-heading-level-by=-1'が使えた。よしよし。
