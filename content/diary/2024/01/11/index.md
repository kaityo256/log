---
title: "2024年1月11日"
date: 2024-01-11T00:00:00+09:00
lastmod: 2024-01-11T00:00:00+09:00
type: diary
source_month: "d202401.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

恐ろしく寒い。

Gitのsubmodule、clone --recursiveした直後はdetached HEAD状態になっっているのか。もともとsubmoduleがハッシュを差しているから、cloneで持ってくるのがハッシュ指定になるんだな。

すべて`main`にするには

```sh
git submodule foreach git switch main
```

すればOK。

会議。笑顔を褒められた。
