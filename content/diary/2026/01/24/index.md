---
title: "2026年1月24日"
date: 2026-01-24T00:00:00+09:00
lastmod: 2026-01-24T00:00:00+09:00
type: diary
source_month: "d202601.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

久しぶりに長めに眠ることができた。

最近、SNSに教育関連のポストをすることが多い。昔、研究者が研究ではなく教育のことばかり書くようになるのが嫌だった。自分もそうなっている。

この6年間、どうしても忙しくて研究が手薄になっていた。研究者なのに。今年は自身が筆頭著者の論文を書く。絶対に書く。何があろうと。

卒論・修論のチェックが滞っている。申し訳ない。

卒論、修論の管理、git submoduleでこんな感じで管理している。

```sh
thesis_list
├── README.md
├── graduate_thesis
│   ├── 2020
│   ├── 2021
│   ├── 2022
│   ├── 2023
│   ├── 2024
│   └── 2025
├── makefile
└── master_thesis
    ├── 2022
    ├── 2023
    ├── 2024
    └── 2025
```

これがあまりよくない気がしている。特に、submodule全部git pullとかが遅い。年度ごとにわけたほうが良いな。thesis_2025とかで、その中にそれぞれgraduate_thesisとmaster_thesisを入れる感じかな。
