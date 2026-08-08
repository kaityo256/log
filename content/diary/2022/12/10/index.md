---
title: "2022年12月10日"
date: 2022-12-10T00:00:00+09:00
lastmod: 2022-12-10T00:00:00+09:00
type: diary
source_month: "d202212.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室サーバにclang-formatが欲しかったのでllvmを入れ、ようとしたがcmakeが古すぎた。

```sh
$ cmake --version
cmake version 2.8.12.2
```

```sh
sudo yum remove cmake 
cd build
wget https://cmake.org/files/v3.25/cmake-3.25.1.tar.gz
tar xvzf cmake-3.25.1.tar.gz
cd cmake-3.25.1
./bootstrap
make
sudo make install
```

```sh
$ cmake --version
cmake version 3.25.1

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

入ったぞ、と。

```sh
cd build
git clone --depth=1 https://github.com/llvm/llvm-project.git
cd llvm-project
mkdir build
cd build
cmake -DLLVM_ENABLE_PROJECTS=clang -DCMAKE_BUILD_TYPE=Release -G "Unix Makefiles" ../llvm
make
sudo make install
```

ってやってたら「sshfsでいいのでは？」と言われた。確かにそっちの方が楽だわ。手元のWSLにsshfsを入れる。

```sh
sudo apt install sshfs
```

デフォルトではVSCodeから開けないので、`/etc/fuse.conf`の`user_allow_other`を有効にしてから、

```sh
sshfs username@remote.server:/path/to/dir ~/path/to/mountpoint -o allow_other
```

としてマウント。あとはローカルのVSCodeで開ける。これは楽だ。

プログラミング基礎同演習のレポート、8割採点して時間切れ。明日に持ち越し。

講義ノートがちっとも進んでない。
