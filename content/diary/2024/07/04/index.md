---
title: "2024年7月4日"
date: 2024-07-04T00:00:00+09:00
lastmod: 2024-07-04T00:00:00+09:00
type: diary
source_month: "d202407.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

BLASとLAPACKのインストール。

```sh
brew install openblas lapack
```

```txt
For compilers to find openblas you may need to set:
  export LDFLAGS="-L/usr/local/opt/openblas/lib"
  export CPPFLAGS="-I/usr/local/opt/openblas/include"

For compilers to find lapack you may need to set:
  export LDFLAGS="-L/usr/local/opt/lapack/lib"
  export CPPFLAGS="-I/usr/local/opt/lapack/include"
```

ということで、パスは通さないといけないっぽいな。

とりあえずOpenBLASとNumPyを比較するサンプル書いた。

[kaityo256/openblas_sample](https://github.com/kaityo256/openblas_sample)

MNISTのデータをPythonからダンプしてC++で読み込むサンプルも書いた。

[https://github.com/kaityo256/mnist_load](https://github.com/kaityo256/mnist_load)
