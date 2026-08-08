---
title: "2025年7月16日"
date: 2025-07-16T00:00:00+09:00
lastmod: 2025-07-16T00:00:00+09:00
type: diary
source_month: "d202507.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

参院選が近いせいか、SNSで選挙の話題になることが多い。それで思うのは、「正しいことを言う事」が「正しいこと」に繋がらないこと。多くの場合、「X支持、X不支持」を決めている人は、その意見を変えることがない。で、例えばXを支持する人が、不支持の人の意見について間違いを指摘する。この時、不支持の人が「ごめんなさい」をすることはほぼないので、レスバ泥仕合となることが多い。すると、その指摘が正しかったとしても、Xについての悪印象を聴衆に植え付ける。X支持の人の目的は、「現在、Xを支持するかどうか決めかねている人たち」を取り込むことのはずで、そのためには「Xを支持する人たち」の言葉を取り上げ、「多くの人がXを支持している」という雰囲気を作らなければならない。いちいちX不支持の人の意見にコメントしていると、聴衆は「X不支持の人、結構いるんだなぁ」と思ってしまい、少なくともX支持にはまわらなくなるだろう。

なんというか、Xを支持する人の言動が、X支持の拡大に繋がらないように見えて、いろいろむずかしいな、と思う。

```sh
$ which ruby
/usr/bin/ruby
```

rbenvが有効になっていないな。なにかで問題起こしたから消したんだっけ？

`.zshrc`の最後に

```sh
eval "$(rbenv init -)"
```

を追加。

```sh
$ which ruby 
/Users/watanabe/.rbenv/shims/ruby
```

OK。

bundleは最初にconfigでローカルの`vendor/bundle`をセットして、後は単に`bundle install`で良さそう。するとカレントディレクトリに`.bundle`ができる。bundleはまず`.bundle/config`をチェックするので、そこに

```txt
---
BUNDLE_PATH: "vendor/bundle"
```

と書いてあれば、デフォルトでそこに入れてくれる。いちいち`bundle install --path vendor/bundle --local`とする必要はない。Pythonのvenvよりスマートだな。

質問メールに返事。ついでに論文データリポジトリを修正しておく。

[Gas-Liquid Phase Boundary of Lennard-Jones System](https://github.com/kaityo256/lj_gas_liquid_boundary)
