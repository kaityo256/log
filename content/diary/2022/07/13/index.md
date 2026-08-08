---
title: "2022年7月13日"
date: 2022-07-13T00:00:00+09:00
lastmod: 2022-07-13T00:00:00+09:00
type: diary
source_month: "d202207.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物性研システムC(kugui)でLAMMPS。

```sh
mkdir github
cd github
git clone -b stable --depth=1  https://github.com/lammps/lammps.git
cd lammps
cd src
qsub -I -V -q i2cpu  -l select=1:ncpus=2
module load intel intel-mpi
make mpi CC=mpiicc LINK=mpiicc CCFLAGS="-g -O3 -std=c++11 -qopenmp" LINKFLAGS="-g -O3 -std=c++11 -qopenmp" -j 20
```

基本的にコンパイラとリンカに`mpiicc`を指定するだけだが、module loadするのと、コンパイルオプションだけでなく、リンクオプションにも`-qopenmp`が必要なのがポイント。

WindowsでPDFをプレビューする時、Adobe Readerが自動再読み込みに対応していないため、WSLでevniceで開いているのが、なんともアホっぽい。

塩漬け論文、子供が寝てから気合で返事をかきあげた。10年近く寝かせた論文。とにかくpublishまでこぎつけなければ。
