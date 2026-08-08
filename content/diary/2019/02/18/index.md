---
title: "2019年2月18日"
date: 2019-02-18T00:00:00+09:00
lastmod: 2019-02-18T00:00:00+09:00
type: diary
source_month: "d201902.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

もうほとんどの作業をVSCodeでやってるんだけど、プログラム言語で唯一Vimで書いてたRubyをVSCodeで書こうと環境を構築・・・しようとして中途半端に挫折。
なんかRubocopのAutocorrectionが走らない。ローカルに.vscode/settings.json書いて、そこにいろいろ設定すればできるんだけど、なんでグローバルにセッテイングできないんだろ？なんか勘違いしてるかな。

あ、できたっぽい。

```json
    "editor.formatOnSaveTimeout": 5000,
```

が必要だった模様。Rubocopが遅いのかな・・・。

面倒なWord文書作成。Pandoc使ったら箇条書きのグルーピングがおかしくなった。
仕方なく以前作ったmd2docx.rbを修正して使った。なんでも作っておくもんだな。
