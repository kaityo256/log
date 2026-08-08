---
title: "2024年11月8日"
date: 2024-11-08T00:00:00+09:00
lastmod: 2024-11-08T00:00:00+09:00
type: diary
source_month: "d202411.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

CentOS 7にopenssl 3.0.15を入れる。

```sh
cd build
wget https://github.com/openssl/openssl/releases/download/openssl-3.0.15/openssl-3.0.15.tar.gz
tar xvzf openssl-3.0.15.tar.gz 
cd openssl-3.0.15
./config
make
```

```sh
$ sudo cp libssl.so.3 libcrypto.so.3 /lib64
$ ./apps/openssl version
OpenSSL 3.0.15 3 Sep 2024 (Library: OpenSSL 3.0.15 3 Sep 2024)
```

```sh
cd build
wget http://ftp.jaist.ac.jp/pub/OpenBSD/OpenSSH/portable/openssh-8.7p1.tar.gz
tar x openssh-8.7p1.tar.gz
cd openssh-8.7p1
./configure
make
```

```sh
$ ./ssh -V
OpenSSH_8.7p1, OpenSSL 1.0.2k-fips  26 Jan 2017
```

ありゃ、ダメだ。ちゃんと場所を指定しないといけないのか。

物情広報の学生さん。写真を撮影。インスタグラムに出すとか。

GitHub演習。ゲーム開発。わりとスムーズだったのでは。

そこからいろいろメールしたり、印刷したり。
