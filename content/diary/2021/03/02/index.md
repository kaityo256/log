---
title: "2021年3月2日"
date: 2021-03-02T00:00:00+09:00
lastmod: 2021-03-02T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Macのg++-10がいつのまにか使えなくなっていたのに対応。

現象。

```sh
$ g++-10 test.cpp 
In file included from /usr/local/Cellar/gcc/10.1.0/include/c++/10.1.0/bits/stl_algo.h:59,
                 from /usr/local/Cellar/gcc/10.1.0/include/c++/10.1.0/algorithm:62,
                 from ../sdouble.hpp:29,
                 from test.cpp:1:
/usr/local/Cellar/gcc/10.1.0/include/c++/10.1.0/cstdlib:75:15: fatal error: stdlib.h: No such file or directory
   75 | #include_next <stdlib.h>
      |               ^~~~~~~~~~
compilation terminated.
```

などと言われ、ヘッダファイルのパスが見つからない。アンインストールしようとしたら、

```sh
$ brew uninstall gcc
Error: Refusing to uninstall /usr/local/Cellar/gcc/10.1.0
because it is required by boost-mpi, fftw, kim-api, lammps, open-mpi, openblas and r, which are currently installed.
You can override this and force removal with:
  brew uninstall --ignore-dependencies gcc
```

などと怒られたので、再インストールしてみる。

```sh
brew reinstall gcc
```

```sh
g++-10 test.cpp
```

コンパイルして、ヘッダが見つからないと言われないことを確認。なおってよかった。

なんかデフォルトブランチがmainとmasterが混在していて鬱陶しいので少しずつmainに修正。

`stat::sdouble`ライブラリを修正。やっぱり`<<`で値を追加する必要はないと判断。普通に`std::vector<double>`を使うことにして、ライブラリでは誤差伝搬だけを考えることにする。
