---
title: "2025年2月24日"
date: 2025-02-24T00:00:00+09:00
lastmod: 2025-02-24T00:00:00+09:00
type: diary
source_month: "d202502.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

学生の卒論、修論は全て一つのGitリポジトリで管理し、それぞれ年号を分けてgit submoduleとしている。
submoduleの性質上、デフォルトではコミットハッシュで管理されてしまうので、クローン直後は全て「頭が取れた状態」になってしまう。なので、

```sh
git submodule foreach git switch main
```

しなければならない。この後で、

```sh
git submodule foreach git pull
```

とすれば全部最新になる。

製本用に卒論を印刷。このために紙を買っておいた。えらい。しかし、クリアファイルが足りなくなった。えらくない。

修論も全て印刷完了。明日製本に出す。
