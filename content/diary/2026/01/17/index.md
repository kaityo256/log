---
title: "2026年1月17日"
date: 2026-01-17T00:00:00+09:00
lastmod: 2026-01-17T00:00:00+09:00
type: diary
source_month: "d202601.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

ZennのAPIを叩いて記事一覧をjsonで得る。

```sh
wget -O zenn1.json "https://zenn.dev/api/articles?username=kaityo256"
wget -O zenn2.json "https://zenn.dev/api/articles?username=kaityo256&page=2"
```

僕は2ページ分で十分だった。

Zennの移行準備。最初、画像の出し方がわからず、GitHubのrawに直リンしてたのを、/imagesにコピーして修正。
