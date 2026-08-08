---
title: "2021年12月18日"
date: 2021-12-18T00:00:00+09:00
lastmod: 2021-12-18T00:00:00+09:00
type: diary
source_month: "d202112.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

要旨見た、

そんな時間はないのだが、どうしても気になったので[おかしなエラーバーのグラフ](https://zenn.dev/kaityo256/articles/weird_errorbars)の記事を書いた。以前[Qiitaに書いた奴](https://qiita.com/kaityo256/items/197a4811e5694dacfa04)が、いまいち本質が伝わっていない気がして。

VimでPythonを書いてて、`numpy.random`が無いと言われる。どうやらPylintの静的解析に問題があるようだ。`~/.pylintrc`に、

```txt
extension-pkg-whitelist = numpy
```

と書いて解決。
