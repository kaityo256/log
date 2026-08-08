---
title: "2026年6月25日"
date: 2026-06-25T00:00:00+09:00
lastmod: 2026-06-25T00:00:00+09:00
type: diary
source_month: "d202606.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

ChatGPT+Codexで地図の色分けエディタを作ってみた。

[World Map Group Editor](https://kaityo256.github.io/world-map-group-editor/)

こんなのがすぐ作れちゃうんだから、AIはすごいね・・・

まず、ChatGPTに世界地図の再利用可能なデータを探してもらい、[Natural Earth](Natural Earth)という、地図データを[public domain](https://www.naturalearthdata.com/about/terms-of-use/)で公開しているサイトを教えてもらう。

ここから、国ごとにグループ化して色分けできるようにすること、国はインクリメンタルサーチで探せるようにすることなどを指定して、PLANS.mdを作ってもらってCodexに確認させ、実装前に細かい調整をしてから実装してもらう。さすがに実装にはそこそこかかったが、それでも5分〜10分くらい？

GitHub Pagesでの公開に失敗したり、「名前をつけて保存」でシステムダイアログが出なかったりしたのでその辺を修正してもらって公開。

研究室ミーティング。今日の紹介論文は以下の二つ。なんか完全に機械学習の研究室になりつつある。

* Rationalization: A Neural Machine Translation Approach to Generating Natural Language Explanations, Upol Ehsan, Brent Harrison, Larry Chan, Mark O. Riedl, AIES '18: Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Societ
* van Seijen, H., Fatemi, M., Romoff, J., Laroche, R., Barnes, T., & Tsang, J. (2017). Hybrid Reward Architecture for Reinforcement Learning. Advances in Neural Information Processing Systems, 30, 5392–5402.

理事会のお仕事とか。
