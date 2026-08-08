---
title: "2025年8月20日"
date: 2025-08-20T00:00:00+09:00
lastmod: 2025-08-20T00:00:00+09:00
type: diary
source_month: "d202508.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Pythonが必要。

```sh
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
pyenv install 3.11.9
pyenv global 3.11.9
python3 -m pip install --user meson ninja
pip install --upgrade pip
```

物性研にgnuplot+png+pngcairoをインストール。

```sh
cd build
```

zlib。

```sh
wget https://zlib.net/zlib-1.3.1.tar.gz
tar xvf zlib-1.3.1.tar.gz
cd zlib-1.3.1
./configure --prefix=$HOME/usr/local
make && make install
cd ..
```

libpng。

```sh
wget https://download.sourceforge.net/libpng/libpng-1.6.44.tar.gz
tar xvf libpng-1.6.44.tar.gz
cd libpng-1.6.44
./configure --prefix=$HOME/usr/local --with-zlib-prefix=$HOME/usr/local
make && make install
cd ..
```

freetype

```sh
wget https://download.savannah.gnu.org/releases/freetype/freetype-2.13.3.tar.gz
tar xvf freetype-2.13.3.tar.gz
cd freetype-2.13.3
./configure --prefix=$HOME/usr/local
make && make install
cd ..
export PKG_CONFIG_PATH=$HOME/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$HOME/usr/local/lib:$LD_LIBRARY_PATH
export CPPFLAGS="-I$HOME/usr/local/include $CPPFLAGS"
export LDFLAGS="-L$HOME/usr/local/lib $LDFLAGS"
```

expat

```sh
wget https://github.com/libexpat/libexpat/releases/download/R_2_6_3/expat-2.6.3.tar.xz
tar xvf expat-2.6.3.tar.xz
cd expat-2.6.3
./configure --prefix=$HOME/usr/local
make && make install
export PKG_CONFIG_PATH=$HOME/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$HOME/usr/local/lib:$LD_LIBRARY_PATH
```

fontconfig

```sh
wget https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.15.0.tar.gz
tar xvf fontconfig-2.15.0.tar.gz
cd fontconfig-2.15.0
./configure --prefix=$HOME/usr/local --with-add-fonts=$HOME/.fonts
make && make install
cd ..
```

pixman

```sh
wget https://cairographics.org/releases/pixman-0.43.4.tar.gz
tar xvf pixman-0.43.4.tar.gz
cd pixman-0.43.4
meson setup build --prefix=$HOME/usr/local
ninja -C build
ninja -C build install
cd ..
```



```sh
wget https://cairographics.org/releases/cairo-1.18.0.tar.xz
tar xvf cairo-1.18.0.tar.xz
cd cairo-1.18.0
meson setup build --prefix=$HOME/usr/local --libdir=lib
ninja -C build
ninja -C build install
```

できない。glibcの新しいバージョンが必要っぽい。

gnuplotをPNGのみでインストール。

```sh
wget https://sourceforge.net/projects/gnuplot/files/gnuplot/6.0.1/gnuplot-6.0.1.tar.gz
tar xvf gnuplot-6.0.1.tar.gz
cd gnuplot-6.0.1
export PKG_CONFIG_PATH=$HOME/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$HOME/usr/local/lib:$LD_LIBRARY_PATH
export CPPFLAGS="-I$HOME/usr/local/include"
export LDFLAGS="-L$HOME/usr/local/lib"
./configure --prefix=$HOME/usr/local --without-qt
```

だめだ。libgdが必要。

```sh
wget https://github.com/libgd/libgd/releases/download/gd-2.3.3/libgd-2.3.3.tar.gz
tar xvf libgd-2.3.3.tar.gz
cd libgd-2.3.3
./configure --prefix=$HOME/usr/local \
  --with-png=$HOME/usr/local \
  --without-xpm --without-freetype --without-jpeg --without-fontconfig
make
make install
```

できた。結局、pngcairoは駄目だった。もう一度まとめなおす。


ビルド場所とインストール先を作成。

```sh
mkdir -p ~/build ~/usr/local
```

ビルド場所に移動。

```sh
cd build
```

zlibのインストール。

```sh
wget https://zlib.net/zlib-1.3.1.tar.gz
tar xvf zlib-1.3.1.tar.gz
cd zlib-1.3.1
./configure --prefix=$HOME/usr/local
make
make install
cd ..
```

libpngのインストール。

```sh
wget https://download.sourceforge.net/libpng/libpng-1.6.44.tar.gz
tar xvf libpng-1.6.44.tar.gz
cd libpng-1.6.44
./configure --prefix=$HOME/usr/local --with-zlib-prefix=$HOME/usr/local
make
make install
cd ..
```

libgdのインストール。

```sh
wget https://github.com/libgd/libgd/releases/download/gd-2.3.3/libgd-2.3.3.tar.gz
tar xf libgd-2.3.3.tar.gz
cd libgd-2.3.3
./configure --prefix=$HOME/usr/local \
  --with-png=$HOME/usr/local \
  --without-freetype --without-fontconfig --without-xpm --without-jpeg
make
make install
cd ..
```

gnuplotのインストール。

```sh
wget https://sourceforge.net/projects/gnuplot/files/gnuplot/6.0.1/gnuplot-6.0.1.tar.gz
tar xf gnuplot-6.0.1.tar.gz
cd gnuplot-6.0.1
export PKG_CONFIG_PATH=$HOME/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=$HOME/usr/local/lib:$LD_LIBRARY_PATH
export CPPFLAGS="-I$HOME/usr/local/include"
export LDFLAGS="-L$HOME/usr/local/lib"
./configure --prefix=$HOME/usr/local --without-qt
make
make install
```

あとは、

```sh
~/usr/local/bin/gnuplot
```

を使うことで、計算ノードでgnuplotが利用可能。物性研システムB, Cともにいけた。
