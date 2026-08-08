---
title: "2021年1月9日"
date: 2021-01-09T00:00:00+09:00
lastmod: 2021-01-09T00:00:00+09:00
type: diary
source_month: "d202101.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

僕がbashではなくzshを使う一番の理由がCtrl+P/Nによるヒストリーサーチだったんだけど、スパコンとかではbashをそのまま使ったほうが良くて、どうせzshにあるならbashにもあるはずと思って調べたらあった。

```bash
bind '"\C-n": history-search-forward'
bind '"\C-p": history-search-backward'
HISTSIZE=100000
```

いや、絶対あるとは思ってたんだけど、なんか腰が重くていままで探していなかった。

ohtakaのセットアップ。

.gitconfigを作ってからdotfilesをクローン。deinもインストール。

```sh
git clone --depth 1 https://github.com/llvm/llvm-project.git
cd llvm-project
mkdir build
cd build
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=~/usr/local
Make 3.13.4 or higher is required.  You are running version 3.11.4
```

まじすか。

```sh
mkdir usr
cd usr
wget https://github.com/Kitware/CMake/releases/download/v3.19.2/cmake-3.19.2-Linux-x86_64.tar.gz
tar xvzf cmake-3.19.2-Linux-x86_64.tar.gz 
mv cmake-3.19.2-Linux-x86_64 local
export CMAKE_ROOT=~/usr/local
export PATH=~/usr/local/bin:$PATH
```

```sh
git clone --depth 1 https://github.com/llvm/llvm-project.git
cd llvm-project
mkdir build
cd build
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=~/usr/local ../llvm
make
```

なんかできているっぽい。一時間くらい経過して50%くらいしか進んでないけど。
