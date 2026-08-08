---
title: "2019年3月11日"
date: 2019-03-11T00:00:00+09:00
lastmod: 2019-03-11T00:00:00+09:00
type: diary
source_month: "d201903.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

git clone --recursiveしたら、" Server does not allow request for unadvertised object "と言われて失敗した。
家で修正したsubmoduleのpushを忘れてしまったらしい。うげぇ。

再現方法と対策を[Qiitaにまとめておいた](https://qiita.com/kaityo256/items/c269b8f2cc47b4799e9f)。
要するにsubmoduleでgit co masterしてから、main moduleでgit add;commitすればよろしい。
あとでマージすることになる。
