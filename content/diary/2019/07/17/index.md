---
title: "2019年7月17日"
date: 2019-07-17T00:00:00+09:00
lastmod: 2019-07-17T00:00:00+09:00
type: diary
source_month: "d201907.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

sshが遅い問題、ssh -vvしてみたら、

```sh
debug1: SSH2_MSG_SERVICE_ACCEPT received
```

で時間がかかってる。ググったら以下のブログの記述に答えがあった。

[http://tegetegekibaru.blogspot.com/2013/07/ssh.html](http://tegetegekibaru.blogspot.com/2013/07/ssh.html)

sshd_configのUseDNSをnoにしてsystemctl restart sshd.service。

VMDのインストール。最初に適当なアカウントとパスワードを設定しないとダウンロードできない。

```sh
tar xvf vmd-1.9.3.bin.LINUXAMD64-CUDA8-OptiX4-OSPRay111p1.opengl.tar.gz
cd vmd-1.9.3
./configure LINUXAMD64
cd src
sudo make install
```

微妙に分かりづらいぞこれ。

次、LAMMPS。

```sh
git clone --depth 1 git://github.com/lammps/lammps.git
cd lammps
cd src
make
```

`atoi`などでコケる。どうすりゃいいんだ？
