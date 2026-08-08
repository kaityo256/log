---
title: "2019年3月6日"
date: 2019-03-06T00:00:00+09:00
lastmod: 2019-03-06T00:00:00+09:00
type: diary
source_month: "d201903.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

SIMDを使うとクロックが下がる奴を調べてたのだが、Skylakeはきれいにxmm→ymm→zmmと下がるものの、
Haswellは下がらない。調べてみると、HaswellまではIntel Speedstep Technology、
SkylakeからIntel Speed Shift Technologyで、動作クロック変更の振る舞いが違うらしい。

とりあえずテストコード書いた。

[https://github.com/kaityo256/simd_clock](https://github.com/kaityo256/simd_clock)

[ここ](https://en.wikichip.org/wiki/intel/frequency_behavior)の記述が詳しいが、まだ理解しきれていない。
