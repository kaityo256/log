---
title: "2026年2月23日"
date: 2026-02-23T00:00:00+09:00
lastmod: 2026-02-23T00:00:00+09:00
type: diary
source_month: "d202602.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

いろいろ仕事。

なんかマークダウンで

```md
* hoge
    * fuga
* hoge
    * fuga
```

みたいなデータが与えられた時、これを

```txt
.
├── hoge
│   └── fuga
└── hoge
    └── fuga
```

みたいに変換したい。いろいろ調べたが、一番簡単なのは[caarlos0/mdtree](https://github.com/caarlos0/mdtree)を使うことっぽい。

```sh
go install github.com/caarlos0/mdtree@latest 
```

で使えるようになる。

```sh
$ cat test.md
* hoge
    * fuga
* hoge
    * fuga

$ mdtree < test.md
.
├── hoge
│   └── fuga
└── hoge
    └── fuga
```

うん、簡単だな。Goは、一度セットアップしてしまうと、ツールのインストールが楽だなぁ。

学生さんの受賞をお祝いするために伊藤先生のご自宅へ。美味しいご飯とお酒をありがとうございました。
