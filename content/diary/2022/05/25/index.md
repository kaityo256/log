---
title: "2022年5月25日"
date: 2022-05-25T00:00:00+09:00
lastmod: 2022-05-25T00:00:00+09:00
type: diary
source_month: "d202205.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

ミネソタ大のLinux悪意パッチ事件、あのあとどうなったかなと調べた。

* [オープンソースのセキュリティ懸念について（ある顛末）](https://www.nds-osk.co.jp/wp/wp-content/uploads/2021/07/onelcof13_keynote1.pdf)
* [コミュニティ総括](https://lkml.org/lkml/2021/5/5/1244)
* [Togetter](https://togetter.com/li/1702680)

ざっと見返したけど、結局Aditya Pakkiという人の対応がまずかった印象。

[当該論文についてのコメント](https://www-users.cse.umn.edu/~kjlu/papers/clarifications-hc.pdf)

人間向けの研究だと思っていなかったとか、いろいろ書いてあるけど、最後の

> OSS projects would be suggested to update the code of conduct, something like “By submitting the patch, I agree to not intend to introduce bugs”

がひどい。
