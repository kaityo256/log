---
title: "2024年4月6日"
date: 2024-04-06T00:00:00+09:00
lastmod: 2024-04-06T00:00:00+09:00
type: diary
source_month: "d202404.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

NOP

日記のビルドに失敗したという連絡。どうもタイトルの`# 2024年4月`をつけ忘れたせいで、makefileの

```mk
docs/%.html: log/%.md
  TITLE=$(shell head -1 $< | sed -e '1 s/^# \(.*\)$$/\1/g'); pandoc -s $< -o $@ $(PANDOC_HTMLOPT) --metadata pagetitle=$$TITLE
```

というコマンドが、

```sh
TITLE=## [04月02日(火)](#02) <a id="02"></a>; pandoc -s log/d202404.md -o docs/d202404.html --mathjax -t html --template=template  --metadata pagetitle=$TITLE
/bin/sh: 1: Syntax error: "(" unexpected
```

となり、カッコ対応がおかしくなったせいだった。ローカルではうまくいくのだが、シェルの違いか？
