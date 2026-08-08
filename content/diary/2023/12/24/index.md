---
title: "2023年12月24日"
date: 2023-12-24T00:00:00+09:00
lastmod: 2023-12-24T00:00:00+09:00
type: diary
source_month: "d202312.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

レポートの採点。

GitでSubmoduleがある時、そのsubmoduleがさらに別のsubmoduleを持っていて、その深い方のsubmoduleの権限を持っていない、という場合に--recursiveでcloneしようとすると失敗する。こういう時の対処法。

1. リポジトリの問題を個別に解消しておく
1. `--recursive`をつけずにcloneする
1. `git submodule init`
1. `git submodule update --remote`

これにより、submoduleが「最新のコミット」を持ってくるので解決する。これまで単に`git submodule foreach git pull`しようとすると、追加された時のコミットをもってこようとするから失敗していた。これに長い間悩んでたが、これでようやく解決。

いや、学生さんたちの卒論、修論をすべてsubmoduleで管理してたので。
