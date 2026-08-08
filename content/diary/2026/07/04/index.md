---
title: "2026年7月4日"
date: 2026-07-04T00:00:00+09:00
lastmod: 2026-07-04T00:00:00+09:00
type: diary
source_month: "d202607.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Macのgnuplotがエラーを出す。

```sh
qt.qpa.plugin: Could not find the Qt platform plugin "cocoa" in ""
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
```

gnuplot再インストールしてもだめ。qtを再インストールしてみる。

```sh
brew reinstall qt
```

これで直った。

42110字。
