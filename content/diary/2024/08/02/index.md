---
title: "2024年8月2日"
date: 2024-08-02T00:00:00+09:00
lastmod: 2024-08-02T00:00:00+09:00
type: diary
source_month: "d202408.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

最近、PGASどうなってるのかな、と調べたら、NERSCのチュートリアルを見つけた。

[Introduction to High-Performance Parallel Distributed Computing Using Chapel, UPC++ and Coarray Fortran, July 2023](https://www.nersc.gov/users/training/past-training-events/2023/hpc-pgas-chapel-upc-coarray-fortran-jul2023/)

動画もある。

[Intro to High-Performance Parallel Distributed Computing with Chapel, UPC++, Coarray Fortran (day 1)](https://www.youtube.com/watch?v=yjpJwTOIppw)

まだ、Chapel、UPC++、Coarray Fortranって現役なんだな・・・

会議。最近会議がバッティングしはじめている。二次の項が無視できなくなってきている。

Chapel、日本語版のWikiのURLが古いな。英語版から以下の公式サイトを見つけた。

[https://chapel-lang.org/](https://chapel-lang.org/)

最新リリースはChapel 2.1で、2024年6月27日。全然現役だった。

OpenBLASのスレッド並列、Pythonだと`OPENBLAS_NUM_THREADS`だが、C++から呼ぶときには普通に`OMP_NUM_THREADS`だった。
