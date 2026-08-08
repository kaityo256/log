---
title: "2019年1月11日"
date: 2019-01-11T00:00:00+09:00
lastmod: 2019-01-11T00:00:00+09:00
type: diary
source_month: "d201901.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

ふと思い立って、HTMLで書いてた曰記のMarkdown化をした。

```mk
HTML=$(shell ls d*.html)
MD=$(HTML:.html=.md)

all: $(MD)

%.md2: %.html
  pandoc -f html -t markdown_strict $< -o $@

%.md: %.md2
  ruby convert.rb $< > $@

.PHONY: clean

clean:
  rm -f *.md *.md
```

pandocで原型を作ってみたらわりときれいにいったので、それをRubyで修正。

ついでに12月の分を埋めた。また公開してみるか。
公開してまずいことは書いてないはずだし。
