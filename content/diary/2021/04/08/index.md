---
title: "2021年4月8日"
date: 2021-04-08T00:00:00+09:00
lastmod: 2021-04-08T00:00:00+09:00
type: diary
source_month: "d202104.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

え？git mergeって、ブランチ指定しないとデフォルトでoriginの同じやつをマージするの？

[git fetchとブランチ取り込み系コマンドの引数を省略すると？](https://qiita.com/matsumon-development/items/b37b1ce988fb810eb8ac)

ブランチ名やリモートを省略した場合、カレントブランチに上流ブランチが指定されていると、暗黙にそれが指定されたことになる。上流ブランチとは

* `git fetch`
* `git merge`
* `git rebase`
* `git pull`
* `git pull --rebase`

の引数を省略したときの処理の対象となるブランチ。マジか。知らなかった。確かに`git fetch`とかはリモートとか省略してた。

え、`git rebase`をリモートに対して実行するケースってあるの？
