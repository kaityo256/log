---
title: "2021年9月17日"
date: 2021-09-17T00:00:00+09:00
lastmod: 2021-09-17T00:00:00+09:00
type: diary
source_month: "d202109.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

ISSP ohtakaでTensorFlow。

```sh
mkdir tftest
cd tftest
python3 -m venv tf
source tf/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install tensorflow tensorflowjs
python3 -m pip install ipython
```

```sh
git clone git@github.com:kaityo256/fashion_mnist_check.git
cd fashion_mnist_check
python3 -m venv tf
source tf/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install tensorflow tensorflowjs
python3 train.py
python3 export.py
```

ここまで動いた。

ローカルでの確認。

```sh
git clone https://github.com/kaityo256/fashion_mnist_check.git
cd fashion_mnist_check
python3 -m venv tf
source tf/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install tensorflow tensorflowjs
python3 train.py
python3 export.py
```

バッチ処理の確認。

```sh
#!/bin/sh
#SBATCH -p i8cpu
#SBATCH -N 1
#SBATCH -n 1

source tf/bin/activate
python3 train.py
python3 export.py
```

```sh
sbatch test.sh
```

問題なく実行できた。

WSL2のGitのバージョンが古くて(2.25.1)デフォルトブランチを変更できないのでバージョンアップする。

```sh
$ sudo add-apt-repository ppa:git-core/ppa
$ sudo apt update
$ sudo apt upgrade
$ git --version
git version 2.33.0
```

できたできた。

学会スライド作った。
