---
title: "2021年3月13日"
date: 2021-03-13T00:00:00+09:00
lastmod: 2021-03-13T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Rubyのヒアドキュメント中に引用符を書きたい場合がある。こんなの。

```rb
t = [1, 2, 3]
puts <<"TEST"
#{t.join(",")}
TEST
```

ここで`t.join(",")`の引用符を、Rubocopはデフォルトでシングルクォーツにしろと怒ってくる。

```txt
test.rb:3:10: C: Style/StringLiteralsInInterpolation: Prefer single-quoted strings inside interpolations.
#{t.join(",")}
         ^^^
```

でも、rufoはここをデフォルトでダブルクォーツに直してくる。VimのALEがチェックにrubocopを、フォーマッタにrufoを使うので、保存時にrufoが直してはrubocopが怒る、というループになる。

結局、`.rubocop.yml`に

```yaml
Style/StringLiteralsInInterpolation:
  EnforcedStyle: double_quotes
```

と書いて、rubocopをrufoに歩み寄らせた。
