---
title: "2021年5月8日"
date: 2021-05-08T00:00:00+09:00
lastmod: 2021-05-08T00:00:00+09:00
type: diary
source_month: "d202105.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

また日記のpush忘れ・・・。木金分は後でmergeですな。真面目にpushしたかどうかの状態表示をつけることを考えよう。

自動車税払った。Yahoo公金支払い便利。納税証明書は電子化され、紙では発行されないとのこと。

自動車税の住所変更した。これで来年から新住所に送られるはず。

push忘れ防止機能つけた。以下は覚え書き。

```sh
name=`git symbolic-ref HEAD 2> /dev/null | sed -e "s/refs\/heads\///g" `
upstream=`git status -sb | grep -E "## .*\.\.\." | sed -e "s/^##.*\.\.\.//"`
if [[ -z $upstream ]]; then
  echo "We do not have an upstream branch."
else
  if [[ -z `git log ${upstream}..${name}` ]]; then
    echo "Already pushed"
  else
    echo "We have unpushed commits."
  fi
fi
```
