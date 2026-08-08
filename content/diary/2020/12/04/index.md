---
title: "2020年12月4日"
date: 2020-12-04T00:00:00+09:00
lastmod: 2020-12-04T00:00:00+09:00
type: diary
source_month: "d202012.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

レポートの採点。毎週数時間かかる大仕事。

Kaggleもくもく会。今日も「House Prices: Advanced Regression Techniques」の続き。LogisticRegression、RandomForest、LightGBMの三種類を試しました。トレーニングデータを２つにわけてチェックしたところ、RandomForestは「完璧に」過学習していることが判明。パラメータを変えて過学習を防ぐと汎化性能も落ちてしまう。この三種類の中では、線形回帰がダメだめ、RandomForestがそれなり、LightGBMが最も性能が良かった。
