---
title: "2026年4月21日"
date: 2026-04-21T00:00:00+09:00
lastmod: 2026-04-21T00:00:00+09:00
type: diary
source_month: "d202604.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Rocky Linuxにxeyesインストール(←なぜ？)。

```sh
git clone https://gitlab.freedesktop.org/xorg/app/xeyes.git
sudo dnf install \
  libX11-devel \
  libXext-devel \
  libXt-devel \
  libXi-devel \
  libXmu-devel \
  xorg-x11-proto-devel \
  xorg-x11-util-macros
./autogen.sh
make
sudo make install
```

できた。

Xの開通確認で`xeyes`便利なんだけど、なんでデフォルトで入ってないんだろ。`xclock`使えってか？

バッチシステムハンズオン。内容がOpenPBSのままになっていることに直前で気づいて修正。いかん。今年度はマジでバタバタしてる。

[物性研スパコンハンズオン](https://github.com/kaityo256/issp_handson)の内容も修正した。

駄目だ。なかなか論文修正まで手が回らない。頭も回ってない。
