---
title: "2018年11月17日"
date: 2018-11-17T00:00:00+09:00
lastmod: 2018-11-17T00:00:00+09:00
type: diary
source_month: "d201811.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

x86infoがAMD EPYCに対応していない。

```sh
$ sudo yum install pciutils-devel 
$ git clone https://github.com/kernelslacker/x86info.git 
$ wget ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/pciutils-3.6.2.tar.gz
$  tar xvzf pciutils-3.6.2.tar.gz 
$ make install-lib
$ export PKG_CONFIG_PATH=$HOME/build/pciutils-3.6.2/lib
$ wget http://zlib.net/zlib-1.2.11.tar.gz
$ tar xvzf zlib-1.2.11.tar.gz 
$ cd zlib-1.2.11
$ ./configure --prefix=$HOME/local
```

 x86infoのMakefileでLDFLAGS = -Wl,-z,relro,-z,now -lzで、最後に-lzを付け加えないとダメだった。

```sh
$ wget http://vault.centos.org/7.5.1804/os/Source/SPackages/x86info-1.30-6.el7.src.rpm
```
