---
title: "2026年1月16日"
date: 2026-01-16T00:00:00+09:00
lastmod: 2026-01-16T00:00:00+09:00
type: diary
source_month: "d202601.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

jekyllでサイトを作る。

```sh
jekyll new mysite
```

デフォルトではテーマはminimaになる。このテーマの_layoutなどは

```sh
bundle info minima  
```

で場所がわかる。今回は

```sh
$ bundle info minima
  * minima (2.5.2)
 Summary: A beautiful, minimal theme for Jekyll.
 Homepage: https://github.com/jekyll/minima
 Path: /Users/watanabe/github/mysite/vendor/bundle/ruby/3.3.0/gems/minima-2.5.2
```

から場所がわかる。

cssをいじるにはmain.scssをいじれば良いが、VSCodeのデフォルトフォーマッタがフロントマターを認識できず、壊してしまう。VSCodeの設定の「SCSS＞Format: Enable」のチェックを外せば良い。

他にもVSCodeがliquidを認識せず、htmlをいじってしまうので、`.vscode/settings.json`に

```json
{
  "[html]": {
    "editor.formatOnSave": false,
    "editor.codeActionsOnSave": {}
  },
  "editor.formatOnSave": true
}
```

と書いた。QiitaのAPIを叩いて、タイトルやタグを取得。これをJekyll向けに修正してexportするスクリプトを書いた。

というわけで、ブログ完成。

[A Robot’s Sigh](https://kaityo256.github.io/)

とりあえずQiitaの記事のうち、重要と思われるものだけexportした。まだ微妙に表示がおかしいところがあるが、おいおい修正しよう。次はZennの記事をexportしたり、カテゴリ検索できるようにしたり、ページネーションをつけたり、OGPを生成したりとかですね。

卒論修論の概要チェックした。
