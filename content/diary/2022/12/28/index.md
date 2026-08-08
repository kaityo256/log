---
title: "2022年12月28日"
date: 2022-12-28T00:00:00+09:00
lastmod: 2022-12-28T00:00:00+09:00
type: diary
source_month: "d202212.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

卒論・修論の管理に悩んでたんだけど、git submoduleを使えばいいのか。普通にディレクトリで管理してると、それぞれgit pullしないといけなくて面倒だったけど、一つのリポジトリにまとめてsubmoduleで管理したら、全部一括でpullとかできる。

全部submoduleにして、一番上に`makefile`おいて

```makefile
all: pull_all

pull_all:
        git submodule foreach git pull
```

と書いた。make一発で全部pullできてかなり快適になった。

まずは修論チェック終わった。次は卒論だ。

あと査読もあるんだよなぁ……

大掃除。
