---
title: "2018年12月4日"
date: 2018-12-04T00:00:00+09:00
lastmod: 2018-12-04T00:00:00+09:00
type: diary
source_month: "d201812.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

<a href="https://qiita.com/implicit_none/items/6e2ddb42dd3392d88824">Qiitaのこの記事</a>を読んで、真面目に
Runge-Kuttaの精度の証明をする。途中、かなり計算がとっちらかったが、なんとか古典RKが4次精度であること、
この記事のアルゴリズムが4次精度ではないことを確認できた。記事のアルゴリズムはLow-storage Runge-Kuttaと呼ばれるもので、
線形の場合には4次精度になるが、非線形の場合には2次精度に落ちる。

　しかし、Runge-Kuttaの精度の証明、もっと賢い方法ないのかなぁ。計算が相当に面倒くさい。
