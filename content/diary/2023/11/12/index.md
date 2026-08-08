---
title: "2023年11月12日"
date: 2023-11-12T00:00:00+09:00
lastmod: 2023-11-12T00:00:00+09:00
type: diary
source_month: "d202311.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

おそらくはじめて`ls`や`cp`で正規表現を使った。

A列にあるIDが、M列のどこかにある場合「3」を表示するコマンド。

```txt
=ARRAYFORMULA(IF(ISNUMBER(MATCH(A2:A, M:M, 0)), 3, ""))
```

GitHub演習のプルリクチェック。いや、もうググるよりChatGPTに聞いた方が早い。ARRAYFORMULAなんて知らなかったよ。

GitHub演習第三回のレポート採点。

プログラミング基礎同演習第六回のレポート採点。

本の執筆。

疲れた。

ChatGPTのバックエンドにDALL-Eがついて、簡単に画像生成できるようになった。素人目にはプロに近いクオリティで何度でも気軽にリテイクできる。すごい時代になったものだ。
