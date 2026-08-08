---
title: "2025年8月25日"
date: 2025-08-25T00:00:00+09:00
lastmod: 2025-08-25T00:00:00+09:00
type: diary
source_month: "d202508.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

RBMの重み初期化について。

* Lecun初期化
    * 古典的な初期化
    * 平均ゼロ、分散1の正規分布で初期化
    * LeCun et al., 1998
* Xavier初期化
    * 正規化初期化。勾配消失、爆発や局所解収束を防ぐために行われる。Sigmoid活性化のために導入された。
    * 原著はXavier Glorot and Yoshua Bengio, "Understanding the difficulty of training deep feedforward neural networks," In Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics (AISTATS 2010)*, vol. 9, pp. 249–256, 2010.のようだ。
* He初期化
    * Xavier初期化と相性が悪いReLU活性化関数のために提案された？
    * Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
    * Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification
    * [arXiv:1502.01852v1](https://arxiv.org/abs/1502.01852)
    * RBMには不要かな？

僕の解析コードにバグがあったので修正。

学生さんの研究計画を作って送る。

完全オンライン化された予算システムを使って、初めて学生の出張申請・・・をしたら、早速間違えた。異なる予算をクリックして始めてしまった。送信したらもう修正できないらしい。慌てて修正依頼を出す。駄目だなぁ・・・

しかし、やり方はわかった。次はいけるはず。
