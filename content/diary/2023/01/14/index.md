---
title: "2023年1月14日"
date: 2023-01-14T00:00:00+09:00
lastmod: 2023-01-14T00:00:00+09:00
type: diary
source_month: "d202301.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

PTEPの論文がMacでコンパイルできない問題、原因がわかった。ロゴのnewlog.epsの変換に失敗しているからだ。

```sh
pstopdf newlogo.eps
```

を実行するとコンパイルできる。うーん。
