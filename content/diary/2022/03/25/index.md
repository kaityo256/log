---
title: "2022年3月25日"
date: 2022-03-25T00:00:00+09:00
lastmod: 2022-03-25T00:00:00+09:00
type: diary
source_month: "d202203.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室サーバにGit 2.X系を入れる(以前入れた気がするが)。

```sh
$ git --version
git version 1.8.3.1
```

古い。削除してから入れる。

```sh
sudo yum remove git
sudo yum install \
https://repo.ius.io/ius-release-el7.rpm \
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum install git --enablerepo=ius --disablerepo=base,epel,extras,updates
```

```sh
$ git --version
git version 2.24.4
```

新しくなった。

講義スライド、第一回分はできたことにする。めちゃくちゃ難産だった。
