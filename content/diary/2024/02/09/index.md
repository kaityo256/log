---
title: "2024年2月9日"
date: 2024-02-09T00:00:00+09:00
lastmod: 2024-02-09T00:00:00+09:00
type: diary
source_month: "d202402.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

博士論文公聴会。

修論のタイトルを承認した。

卒論・修論の最終提出の案内を流した。

Swendsen-WangのGPGPU実装。

* [CUDA programs for the GPU computing of the Swendsen–Wang multi-cluster spin flip algorithm: 2D and 3D Ising, Potts, and XY models](https://doi.org/10.1016/j.cpc.2013.10.029)
* [Improved CUDA programs for GPU computing of Swendsen–Wang multi-cluster spin flip algorithm: 2D and 3D Ising, Potts, and XY models](https://doi.org/10.1016/j.cpc.2015.10.003)

どちらもソースコードが公開されている。これは、

[Parallel graph component labelling with GPUs and CUDA](https://doi.org/10.1016/j.parco.2010.07.002)

に基づいている。グラフの並列処理について、どうしてもアトミックな処理が必要になるが、それはCUDAの`atomicMin()`を利用している。

量子系でも似たような処理が必要になるが、それについては藤堂さんが論文を出している。

[Parallel loop cluster quantum Monte Carlo simulation of quantum magnets based on global union-find graph algorithm](https://doi.org/10.1016/j.cpc.2019.01.004)

ここではロック機構としてcompare-and-swap atomic instructionを使っている。Intel x86なら`cmpxchgl`、SPARCなら`cas`だそうな。

論文の査読した。初めてのsigned referee。やはり緊張する。オンラインでどんどん議論する形なのか。時代は変化していくのだなぁ。
