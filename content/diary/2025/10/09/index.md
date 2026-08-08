---
title: "2025年10月9日"
date: 2025-10-09T00:00:00+09:00
lastmod: 2025-10-09T00:00:00+09:00
type: diary
source_month: "d202510.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

サーバ設定。Rockeyで

```sh
sudo dnf update -y
```

とすると

```txt
Error: 
 Problem 1: package authselect-1.2.6-3.el9.x86_64 from baseos requires authselect-libs(x86-64) = 1.2.6-3.el9, but none of the providers can be installed
  - cannot install the best update candidate for package authselect-1.2.6-2.el9.x86_64
  - package authselect-libs-1.2.6-3.el9.x86_64 from baseos is filtered out by exclude filtering
 Problem 2: package authselect-compat-1.2.6-3.el9.x86_64 from appstream requires authselect(x86-64) = 1.2.6-3.el9, but none of the providers can be installed
  - package authselect-1.2.6-3.el9.x86_64 from baseos requires authselect-libs(x86-64) = 1.2.6-3.el9, but none of the providers can be installed
  - cannot install the best update candidate for package authselect-compat-1.2.6-2.el9.x86_64
  - package authselect-libs-1.2.6-3.el9.x86_64 from baseos is filtered out by exclude filtering
(try to add '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
```

のようなエラーがでる。これは、`/etc/dnf/dnf.conf`に

```txt
exclude=ypbind nss_nis yp-tools authselect-libs autofs
```

と、authselect-libの除外設定があるから。

Rockeyにslurmインストール。最初にソースからインストールしてしまったので話がややこしくなった。素直にdnfを使うべき。

ログインノードでのジョブ投入は成功。計算ノードからつながらない。

```sh
$ nc -zv login-node-name 6817
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: No route to host.
```

ポートが塞がってますね。ログインノードで以下を実行。

```sh
sudo firewall-cmd --zone=public --add-port=6817/tcp --permanent
sudo firewall-cmd --zone=public --add-port=6818/tcp --permanent
sudo firewall-cmd --reload
```

計算ノードは6818をあける必要がある。

```sh
sudo firewall-cmd --permanent --add-port=6818/tcp
sudo systemctl restart firewalld
```

通った(firewalldを再起動忘れて繋がらなかった・・・)。

次はMPI。計算ノードで以下を実行。

```sh
sudo dnf install -y openmpi openmpi-devel
```

パスを通す。/etc/bashrcに以下を追加。

```sh
export PATH=/usr/lib64/openmpi/bin:$PATH
```

```sh
PartitionName=default Nodes=ALL Default=YES MaxTime=INFINITE State=UP
```

としたらエラー。defaultは予約後だそうで。

```sh
PartitionName=main Nodes=ALL Default=YES MaxTime=INFINITE State=UP
```

としたら通った。

```sh
PartitionName=main Nodes=ALL Default=YES MaxTime=1-00:00:00 State=UP
```

と、24時間制限をつけた。

クラスタにlammpsインストール

```sh
cd github
git clone -b release --depth 1  https://github.com/lammps/lammps.git
cd lammps
mkdir build
cd build
cmake ../cmake \
  -D CMAKE_C_COMPILER=mpicc \
  -D CMAKE_CXX_COMPILER=mpicxx \
  -D CMAKE_INSTALL_PREFIX=~/usr/local \
  -D CMAKE_CXX_FLAGS="-O3 -std=c++11 -fopenmp" \
  -D BUILD_MPI=yes \
  -D BUILD_OMP=yes \
  -D CMAKE_EXE_LINKER_FLAGS="-O3 -std=c++11 -fopenmp" \
  -D PKG_MOLECULE=on
make -j 4
make install
```

無事にログインノード、計算ノードでlammpsも並列に走った。よし。これで研究室クラスター復活。

・・・疲れたなぁ。
