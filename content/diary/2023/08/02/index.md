---
title: "2023年8月2日"
date: 2023-08-02T00:00:00+09:00
lastmod: 2023-08-02T00:00:00+09:00
type: diary
source_month: "d202308.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

昨日のまとめ。

Markdownで書いたファイルをRe:VIEWに変換してPDF化するコードが動かない。ものすごく昔は、RedcarpetがRe:VIEWレンダラを持っていたのでそれを使っていたのだが、途中でなくなったらしい。仕方なく`md2review`を使ったが、エラーが出る。問題は数式の中にMarkdownの予約シンボルがあるとバグること。

たとえばこんなファイルを食わせてみると、

```md
# test

$$
a_1 + a_2
$$
```

こうなってしまう。

```txt
= test


$$
a@<b>{1 + a}2
$$
```

`_`で挟まれた場所を太字にしようとしている。

あとはこんなのが、

```md
# test

$$
a^*+b^*
$$
```

こうなる。

```txt
= test
$$
a^@<b>{+b^}
$$
```

さらに、改行も処理されてしまう。これが、

```md
$$
\begin{aligned}
a &= 1\\
b &= 2
\end{aligned}
$$
```

こうなる。

```txt
$$
\begin{aligned}
a &= 1\
b &= 2
\end{aligned}
$$
```

というわけで、問題になりそうな記号類を全てエスケープしてからmd2reviewに食わせて、その後もとに戻す、という処理をしたのだが、makefileが

```make
%.re: ../%/README.md
  ruby pre.rb $^ > $*.pre
  md2review $*.pre > $*.post
  ruby post.rb $*.post > $*.re
```

という感じになってダサい。おそらくRedcarpetのレンダラを自作するのがまっとうな解決策だが、そこまですべきかなぁ・・・

あれ？手元の環境には`redcarpet/render/review`があるぞ？なんでだ？

こんなコードを書いてみる。

```rb
require 'redcarpet'
a = $LOADED_FEATURES.dup()
require 'redcarpet/render/review'
b = $LOADED_FEATURES

puts b-a
```

結果。

```txt
/Users/watanabe/.rbenv/versions/3.2.2/lib/ruby/3.2.0/digest/version.rb
/Users/watanabe/.rbenv/versions/3.2.2/lib/ruby/3.2.0/x86_64-darwin22/digest.bundle
/Users/watanabe/.rbenv/versions/3.2.2/lib/ruby/3.2.0/digest/loader.rb
/Users/watanabe/.rbenv/versions/3.2.2/lib/ruby/3.2.0/digest.rb
/Users/watanabe/.rbenv/versions/3.2.2/lib/ruby/3.2.0/x86_64-darwin22/digest/md5.bundle
/Users/watanabe/.rbenv/versions/3.2.2/lib/ruby/gems/3.2.0/gems/md2review-1.12.1/lib/redcarpet/render/review.rb
```

`md2review`によりレンダラに`render/review`が追加されている。なるほど。それじゃ、これを使えばいちいちファイルに何度も吐かなくて済むはずか。

ひょっとして、昔からRedcarptはRe:VIEWには対応していなくて、僕がmd2reviewを入れたからメソッドが追加されたのを勘違いしていた？

1on1たくさん。

数理物理成績確定した。わりと理想的な成績分布だったのでは。

とりあえず解析力学のリポジトリ、`Redcarpet::Render::ReVIEW.new`を使って一括変換する形に修正。ついでにLinterとしてRubocopを入れたが、相変わらずうるさいのでrubocop.ymlに

```yml
Metrics:
  Enabled: false
```

と書いてしまった。それでもまだうるさい。あと、若干動作が遅いのが気になるなぁ。
