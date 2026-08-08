---
title: "2025年6月25日"
date: 2025-06-25T00:00:00+09:00
lastmod: 2025-06-25T00:00:00+09:00
type: diary
source_month: "d202506.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

```sh
mkdir build # もしbuildディレクトリがなければ作る
cd build
wget https://github.com/libffi/libffi/releases/download/v3.5.1/libffi-3.5.1.tar.gz
tar xvzf libffi-3.5.1.tar.gz
cd libffi-3.5.1/
$ ./configure --prefix=$HOME/local/libffi --disable-static --with-pic
make
make install
cd
export PKG_CONFIG_PATH=$HOME/local/libffi/lib/pkgconfig:$PKG_CONFIG_PATH
export CFLAGS="-I$HOME/local/libffi/include"
export LDFLAGS="-L$HOME/local/libffi/lib"
ulimit -u 300
env \
  CFLAGS="-I$HOME/local/libffi/include" \
  LDFLAGS="-L$HOME/local/libffi/lib" \
  PKG_CONFIG_PATH="$HOME/local/libffi/lib/pkgconfig" \
  pyenv install 3.10.14
```

```sh
mkdir test
cd test
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install scipy
python3 -m pip install deephyper
```

いろいろだめ。miniforgeに逃げる。

```sh
cd build
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
eval "$(/home/k0117/k011700/miniforge3/bin/conda shell.bash hook)" 
conda init
conda create -n myenv python=3.10
```

deephyperのテスト。

```sh
$ python3 test.py
     p:b p:function       p:x  ...  sol.p:function   sol.p:x sol.objective
0      7      cubic -1.103350  ...           cubic  8.374450    590.312101
1      3      cubic  8.374450  ...           cubic  8.374450    590.312101
2      6      cubic  4.680560  ...           cubic  8.374450    590.312101
3      9     linear  8.787395  ...           cubic  8.374450    590.312101
4      6      cubic  9.109560  ...           cubic  9.109560    761.948419
..   ...        ...       ...  ...             ...       ...           ...
96    10      cubic  9.999914  ...           cubic  9.999998   1009.999489
97    10      cubic  9.999943  ...           cubic  9.999998   1009.999489
98    10     linear  9.999705  ...           cubic  9.999998   1009.999489
99    10     linear  9.999884  ...           cubic  9.999998   1009.999489
100   10      cubic  9.999922  ...           cubic  9.999998   1009.999489

[101 rows x 12 columns]

Optimum values
function: cubic
x: 9.99999829679699
b: 10
y: 1009.9994890391841
```

できてるな。

シミュレーション工学のレポートの採点残り終えた。

中間テスト作った。

理事会のお仕事返した。

いろいろ余裕がなさすぎる。数理物理の講義がある期間は何もできないと思っておいたほうが良さそう。
