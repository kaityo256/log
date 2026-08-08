---
title: "2021年7月1日"
date: 2021-07-01T00:00:00+09:00
lastmod: 2021-07-01T00:00:00+09:00
type: diary
source_month: "d202107.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

似鳥さんの講義。

A64FXのレイテンシが9もあるの？レジスタが32本しかないと、普通に足りないのでは？

ARMの逆数近似、8bitなんだ。

svrsqrte_f64が逆数近似かな。

__restrictをつけると、エイリアスがないことを宣言できる。

ストア命令もFPUのパイプを消費するのマジか。
ロード命令は消費しない。

srqrtsという補助命令がある

Tree Height Reduction (THR)という考えがあることを知った。

SWPが効くのはtrad mode。-KfastでSWP
 
IntelコンパイラにLLVMベースのがあるのか！

引き算の順序で性能が代わる。x86はメモリをオペランドに取れるから。

ARMではSIMDレジスタ内転置(SoA→AoS)が一発(1命令)でできる。ただし、レジスタが連番でなければいけない。
