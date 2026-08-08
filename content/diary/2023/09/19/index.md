---
title: "2023年9月19日"
date: 2023-09-19T00:00:00+09:00
lastmod: 2023-09-19T00:00:00+09:00
type: diary
source_month: "d202309.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Slackの2FAをしろというメールが来たので対応した。GitHubも2FAが義務付けられたので、GitHub演習も対応しないと。

最後は経済物理のセッション。C206。

* C206-1 ε-τ解析。株価がεだけ変化するか、時間がτだけ経つかしたら参照点を追加、upトレンドとdownトレンドを定義する。いわゆる損切りのモデル。
* C206-3 Gravity interaction model。正方格子でγの値により分岐。
* C206-4 ランダム乗算過程モデル。ファットテール分布の解析。Weiboのハッシュタグの一日あたりの利用回数がファットテール。一日当たりの利用回数を$x_t$とすると、成長率は$b_t = x_{t_1}/x_t$。すると$log b_t$がラプラス分布となる。
* C206-7 戦略多様性を考慮した一般化Lillo-Mike-Farmerモデルとその検証 [arXiv:2301.13505](https://arxiv.org/abs/2301.13505) PRLに通ったらしい。
* C207-8 [マハラノビス距離](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%8F%E3%83%A9%E3%83%8E%E3%83%93%E3%82%B9%E8%B7%9D%E9%9B%A2)

累積確率分布CDFについて、僕はいつも$f(x) = P(X<x)$の形で定義してたので、$x \rightarrow \infty$で$P(x) = 1$になってたんだけど、高安グループは$f(x) = P(X>x)$で定義しているので、$P(x) = 0$にしてる。その方が傾きが右肩下がりになって見やすいかもなぁ。

coinという動詞があることを知った。LDOCEによると「to invent a new word or expression, especially one that many people start to use」らしい。へぇ。

今回の学会は、学生さんがそっちだったということもあり、領域12にいることが多かったなぁ。
