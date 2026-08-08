---
title: "2021年2月17日"
date: 2021-02-17T00:00:00+09:00
lastmod: 2021-02-17T00:00:00+09:00
type: diary
source_month: "d202102.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

これで2日連続日付挿入スニペットを使ったぞ。

卒論の製本依頼した。表紙を別紙に用意したが、申込用紙の「表紙」にバツマークをつけて「マーク有」と書けば、ペンマークを入れてくれる。

研究室ミーティング。なるほど、面白い。

その後、B3のPCセットアップ。

Anacondaのインストール画面が違う。

pyenvでanacondaはM1にうまく入らなかったっぽい。

```sh
brew install pyenv
pyenv install 3.9.1
```

これでいけるはず。

また、lammpsをbrewで入れた時のパスが違う。

```sh
cd
mkdir lammps
cd lammps
cp -r /opt/homebrew/Cellar/lammps/2020-10-29/share/lammps/examples/melt .
cd melt
```

WSL2のインストールも書かないと。
