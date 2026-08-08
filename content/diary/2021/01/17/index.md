---
title: "2021年1月17日"
date: 2021-01-17T00:00:00+09:00
lastmod: 2021-01-17T00:00:00+09:00
type: diary
source_month: "d202101.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

卒論チェック。

CentOSにpovrayのインストール。とりあえずローカルで。

```sh
mkdir local
cd local
mkdir lib
cd lib
wget http://www.povray.org/redirect/www.povray.org/ftp/pub/povray/Old-Versions/Official-3.62/Linux/povlinux-3.6.tgz
tar xvzf povlinux-3.6.tgz
```

その後、`~/local/bin`にpovrayへのシンボリックリンクをはってから

```sh
export PATH=~/local/bin:$PATH
````

でパスを通した。さらに、`~/.povrayrc`に、

```sh
Width = 320
Height = 240
Library_Path=/home/watanabe/local/lib/povray-3.6/
Library_Path=/home/watanabe/local/lib/povray-3.6/include
```

このパスを通しておかないと、`#include`が通らない(povrayがcolors.incを見つけられない)。

スパコンにジョブを投げる。
