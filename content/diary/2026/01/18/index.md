---
title: "2026年1月18日"
date: 2026-01-18T00:00:00+09:00
lastmod: 2026-01-18T00:00:00+09:00
type: diary
source_month: "d202601.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

JekyllでOGPを設定。最初はサイトのタイトルしか表示されなかったが、以下のようにすれば記事のタイトルが`og:title`に設定される。

```html
{% if page.title %}
  {% assign og_title = page.title %}
{% else %}
  {% assign og_title = site.title %}
{% endif %}

<meta property="og:title" content="{{ og_title | escape }}">
<meta name="twitter:title" content="{{ og_title | escape }}">
```

あと、Jekyll:Composeを導入。`Gemfile`に

```sh
gem 'jekyll-compose', group: [:jekyll_plugins]
```

と入れて、

```sh
bundle
```

するだけ。`post`サブコマンドとかが追加される。

```sh
bundle exec jekyll -h 
```

Subcommandsに以下が追加される。

```sh
  draft      # Creates a new draft post with the given NAME
  post       # Creates a new post with the given NAME
  publish    # Moves a draft into the _posts directory and sets the date
  unpublish  # Moves a post back into the _drafts directory
  page       # Creates a new page with the given NAME
  rename     # Moves a draft to a given NAME and sets the title
  compose    # Creates a new file with the given NAME
```

ブログ完成したことにする。

[さらばいいねの世界](https://kaityo256.github.io/farewell-to-likes)

jekyll postはpermlinkがつかないんだな。デフォルトでつくように修正しないと。

Jekyll::Composeを導入したが、いまいちだったので自作した。っていうか仕様だけ切ってChatGPTに
作らせた。

```sh
./post slug
```

とかすれば記事を作ってくれるし、-dオプションで日付を、-tオプションでタグを指定して、-iオプションでイメージ用のディレクトリを掘ってくれる。地味に便利。

VSCodeがscssも壊すので、scssも無視設定に追加。

```json
{
  "[html]": {
    "editor.formatOnSave": false,
    "editor.codeActionsOnSave": {}
  },
  "[scss]": {
    "editor.formatOnSave": false,
    "editor.codeActionsOnSave": {}
  },

  "editor.formatOnSave": true
}
```

なんか日記だけ見るとブログにかまけてる感じだけど、当然ながら日記に書けないタスクを大量にこなしており、その空き時間にどうにかちょこちょこブログの設定だけできている感じ。本当はレポートの採点やシラバスの確認もしたかったけど、どうにも時間が取れなかった。

忙しいアピールはしたくないけどさ、暇だと思われるのも困る。昔、博士の学生さんがブログにドラマの感想ばかり書いてて、それを見ていた年配の研究者に「テレビばかり見てないで研究もしないとね」みたいなことを言われた、という話を思い出す。もちろん研究はしてて、ドラマは家事とかの合間に見ているだけで、わざわざ忙しいアピールをしていなかっただけなのだが、とても悲しかった、とブログに書いてあった。

なんだかタスクが積み上がりすぎて心が荒んでますね。がんばらないと。
