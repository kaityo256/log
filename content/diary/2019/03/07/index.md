---
title: "2019年3月7日"
date: 2019-03-07T00:00:00+09:00
lastmod: 2019-03-07T00:00:00+09:00
type: diary
source_month: "d201903.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

GitHubの[分子動力学法・ステップ・バイ・ステップ](https://github.com/kaityo256/mdstep)に星がついたのをきっかけに、
少しだけREADMEを修正した。こういう、自分でも書いたのを忘れたようなものに「いいね」がつくとうれしい。

```sh
git clone https://github.com/gperftools/gperftools.git
cd gperftools
./autogen.sh
./configure --prefix=$HOME/local
make install
export LD_LIBRARY_PATH=$HOME/local/lib:$LD_LIBRARY_PATH
g++ -std=c++11 -L$HOME/local/lib -ltcmalloc -g test.cpp
```

K

```sh
git clone https://github.com/gperftools/gperftools.git
cd gperftools
./autogen.sh
./configure --prefix=$HOME/local --with-CC=fccpx --with-CXX=FCCpx --with-CFLAGS=-Xg --with-CPPFLAGS=-Xg
```

ダメだ。tcmallocのクロスコンパイルが面倒すぎる。諦めよう・・・。
