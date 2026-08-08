---
title: "2025年6月4日"
date: 2025-06-04T00:00:00+09:00
lastmod: 2025-06-04T00:00:00+09:00
type: diary
source_month: "d202506.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物性研にSLATEをインストール。

```sh
cd build
git clone --recursive https://github.com/icl-utk-edu/slate.git
cd slate
mkdir build
cd build
cmake -Dblas=mkl -Dbuild_tests=no -DCMAKE_INSTALL_PREFIX=/usr/local
```

```sh
module purge
module load oneapi_compiler oneapi_mpi oneapi_mkl
```

```sh
$ mpiicpc --version
icpc (ICC) 2021.8.0 20221119
Copyright (C) 1985-2022 Intel Corporation.  All rights reserved.
```

```sh
export CXX=mpiicpc
export FC=mpiifort
cmake -Dblas=mkl -Dbuild_tests=no -Dgpu_backend=none -DCMAKE_INSTALL_PREFIX=$HOME/usr/local ..
```

```txt
CMake Error at blaspp/CMakeLists.txt:8 (cmake_minimum_required):
  CMake 3.21 or higher is required.  You are running version 3.19.2
```

CMakeが古いな。自分が入れた古いのを見てた。やりなおし。

```txt
CMake Error at blaspp/CMakeLists.txt:8 (cmake_minimum_required):
  CMake 3.21 or higher is required.  You are running version 3.20.2
```

まだ古い。

```sh
cd build
wget https://github.com/Kitware/CMake/releases/download/v4.0.2/cmake-4.0.2-linux-x86_64.tar.gz
tar xvzf cmake-4.0.2-linux-x86_64.tar.gz 
cd cmake-4.0.2-linux-x86_64/
cp bin/* ~/usr/local/bin/
'cp' -r share ~/usr/local
export PATH=~/usr/local/bin:$PATH
export CMAKE_ROOT=~/usr/local
```

```sh
$ cmake --version
cmake version 4.0.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

よろしい。改めて。

```sh
cd build
export CXX=mpiicpc
export FC=mpiifort
cmake -Dblas=mkl -Dbuild_tests=no -Dgpu_backend=none -DCMAKE_INSTALL_PREFIX=$HOME/usr/local ..
make
```

```sh
$ /opt/intel/oneapi/mpi/2021.8.0/bin/mpiicpc -DSLATE_ID=\"f8348a7c\" -Dslate_EXPORTS -I/home/k0117/k011700/build/slate/include -I/home/k0117/k011700/build/slate/src -I/home/k0117/k011700/build/slate/build/blaspp/include -I/home/k0117/k011700/build/slate/blaspp/include -I/home/k0117/k011700/build/slate/build/lapackpp/include -I/home/k0117/k011700/build/slate/lapackpp/include -std=c++17 -fPIC -qopenmp -MD -MT CMakeFiles/slate.dir/src/hemmA.cc.o -MF CMakeFiles/slate.dir/src/hemmA.cc.o.d -o CMakeFiles/slate.dir/src/hemmA.cc.o -c /home/k0117/k011700/build/slate/src/hemmA.cc

/home/k0117/k011700/build/slate/src/hemmA.cc(305): error: unsupported lvalue expression on locator-list
              #pragma omp task depend(in:gemm[A.nt()-1])
                                         ^
          detected during instantiation of "void slate::hemmA(blas::Side, scalar_t, slate::HermitianMatrix<scalar_t> &, slate::Matrix<scalar_t> &, scalar_t, slate::Matrix<scalar_t> &, const slate::Options &) [with scalar_t=float]" at line 673

/home/k0117/k011700/build/slate/src/hemmA.cc(553): error: unsupported lvalue expression on locator-list
              #pragma omp task depend(in:gemm[A.nt()-1])
                                         ^
          detected during instantiation of "void slate::hemmA(blas::Side, scalar_t, slate::HermitianMatrix<scalar_t> &, slate::Matrix<scalar_t> &, scalar_t, slate::Matrix<scalar_t> &, const slate::Options &) [with scalar_t=float]" at line 673

compilation aborted for /home/k0117/k011700/build/slate/src/hemmA.cc (code 2)
```

エラーだな。

```sh
g++ -DSLATE_ID=\"f8348a7c\" -Dslate_EXPORTS -I/home/k0117/k011700/build/slate/include -I/home/k0117/k011700/build/slate/src -I/home/k0117/k011700/build/slate/build/blaspp/include -I/home/k0117/k011700/build/slate/blaspp/include -I/home/k0117/k011700/build/slate/build/lapackpp/include -I/home/k0117/k011700/build/slate/lapackpp/include -std=c++17 -fPIC -fopenmp -MD -MT CMakeFiles/slate.dir/src/hemmA.cc.o -MF CMakeFiles/slate.dir/src/hemmA.cc.o.d -o CMakeFiles/slate.dir/src/hemmA.cc.o -c /home/k0117/k011700/build/slate/src/hemmA.cc
```

通る。

```sh
git clone --recursive https://github.com/icl-utk-edu/slate.git
cd slate
mkdir build
cd build
export CXX=mpicxx
export FC=mpiifort
cmake -Dblas=mkl -Dbuild_tests=no -Dgpu_backend=none -DCMAKE_INSTALL_PREFIX=$HOME/usr/local ..
```

一応ビルドは通ったが・・・？

等周問題を考えたが、意外に難しい。うーむ。

査読した結果が次々返ってくる。他の査読者のコメント、参考になる。
