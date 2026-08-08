---
title: "2021年9月21日"
date: 2021-09-21T00:00:00+09:00
lastmod: 2021-09-21T00:00:00+09:00
type: diary
source_month: "d202109.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

学会発表。久しぶりだ。

座長。つつがなく。

なんかMacのアップデートをして、macOS Big Sur 11.6にしたら、Cisco系のアプリケーションが全てマルウェアとして判定されるように。うまくアンインストールもできない。以下の様に、ターミナルからsuduで消したらうまくいった。

```sh
sudo /opt/cisco/anyconnect/bin/vpn_uninstall.sh
sudo /opt/cisco/anyconnect/bin/dart_uninstall.sh 
sudo /opt/cisco/anyconnect/bin/websecurity_uninstall.sh
sudo /opt/cisco/anyconnect/bin/amp_uninstall.sh
sudo /opt/cisco/anyconnect/bin/nvm_uninstall.sh
sudo /opt/cisco/anyconnect/bin/umbrella_uninstall.sh
sudo /opt/cisco/anyconnect/bin/iseposture_uninstall.sh
sudo /opt/cisco/hostscan/bin64/csd_uninstall.sh
```

root権限が無いところに、Zshをソースから入れる。

```sh
mkdir build
cd build
wget ftp://ftp.gnu.org/gnu/ncurses/ncurses-6.1.tar.gz
tar xf ncurses-6.1.tar.gz
cd ncurses-6.1
./configure --prefix=$HOME/local CXXFLAGS="-fPIC" CFLAGS="-fPIC"
make -j && make install
cd ..

ZSH_SRC_NAME=$HOME/packages/zsh.tar.xz
ZSH_PACK_DIR=$HOME/packages/zsh
ZSH_LINK="https://sourceforge.net/projects/zsh/files/latest/download"

if [[ ! -d "$ZSH_PACK_DIR" ]]; then
    echo "Creating zsh directory under packages directory"
    mkdir -p "$ZSH_PACK_DIR"
fi

if [[ ! -f $ZSH_SRC_NAME ]]; then
    curl -Lo "$ZSH_SRC_NAME" "$ZSH_LINK"
fi

tar xJvf "$ZSH_SRC_NAME" -C "$ZSH_PACK_DIR" --strip-components 1
cd "$ZSH_PACK_DIR"

./configure --prefix="$HOME/local" \
    CPPFLAGS="-I$HOME/local/include" \
    LDFLAGS="-L$HOME/local/lib"
make -j && make install
```

領域11のインフォーマルミーティング出た。何年ぶりだろ。
