---
title: "2026年1月3日"
date: 2026-01-03T00:00:00+09:00
lastmod: 2026-01-03T00:00:00+09:00
type: diary
source_month: "d202601.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

卒論、修論はすべてgit submoduleで管理しているが、submodule addした時点でのハッシュに固定されてしまうので、一度 mainにswitch してからpullしないといけない。

```sh
git submodule update --init --recursive
git submodule foreach 'git switch main'
git submodule foreach 'git pull'
```

これだと、すべての年度の卒論・修論にアップデートかかるんだよなぁ。

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

いま、こんな構造なんだけど、GitはSubversionと違って部分更新できないから、全部を見に行って時間がかかってしまう。うーむ。

修論1編見た。
