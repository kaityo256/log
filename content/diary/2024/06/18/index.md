---
title: "2024年6月18日"
date: 2024-06-18T00:00:00+09:00
lastmod: 2024-06-18T00:00:00+09:00
type: diary
source_month: "d202406.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

VSCodeのDraw.io拡張がPDFを吐けないことの対処。

まずdraw.ioをインストール。

```sh
brew install --cask drawio
```

デフォルトでパスが通らないので、alias。

```sh
alias draw.io=/Applications/draw.io.app/Contents/MacOS/draw.io  
```

drawioファイルをpdfに変換。

```sh
draw.io -xf pdf -o test.pdf test.drawio
```

`includegraphics`にwidthを指定したら通らない。原因は

```tex
\usepackage[dvipdfmx]{graphics}
```

と書いていたから。正しくは

```tex
\usepackage[dvipdfmx]{graphicx}
```

アホ過ぎる。
