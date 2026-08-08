---
title: "2022年7月19日"
date: 2022-07-19T00:00:00+09:00
lastmod: 2022-07-19T00:00:00+09:00
type: diary
source_month: "d202207.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

学生さんのPCが壊れたので急遽新しいのを購入。「PCは突然壊れる」という感覚を肌で覚えるのは非常に重要なことだと思います。

いろいろやりたいことがある。いまローカルのエクセルで管理している予算をGoogle SpreadSheetにしたい。Pukiwikiで管理している研究室WikiをGitHubに移行したい。しかし、忙しい。

GitHubのMarkdownがいつのまにか数式をサポートしていた。

[Math support in Markdown](https://github.blog/2022-05-19-math-support-in-markdown/)

いままで、Markdownで書いてからいちいちPandocでHTMLになおしていたのだが、これが不要になるのか。

「一週間でなれる！スパコンプログラマ」の表示がおかしかった気がしてissueを立てたが、いま見たら直っていた上に、そもそもMarkdown上で数式が見えて驚いた。対応の途中で表示がおかしかったのをたまたま目にしたのか？いずれにせよ数式対応はありがたい。

なんか、「進捗が無いと世の中に意見を言いたくなる病」にかかっている。いかん。進捗は百薬の長。

GitHubにブランチ保護機能がついた。例えば「削除を許す」「歴史がまっすぐであることを要求する(マージコミットを含む歴史のpushを許さない)」などがある。とりあえずデフォルトで「Allow force pushes」と「Allow deletions」がオフになっている状態なので、ルールを有効化することで、それができなくなったはず。

ちょっとこれUIがよくないな。デフォルトでオフになっている「Allow force pushes」が、ルールを有効化することで有効化される、つまりforce pushを許さなくなる、というのは、ちょっとよくないと思う。デフォルトでは現状、すなわちAllow force pushesやAllow deletionsがオンになっておき、Protectionの有効化によりオフになる、という方がよいと思う。

Macにnpmが入っていなかったのでいれる。

```sh
brew install npm
```

その後、zennを管理するリポジトリにて

```sh
npm install zenn-cli 
```

でOK。他の場所(WSL)で作成したzenn-contentを、別の場所(Mac)でいじる、ということを想定しておらず、またnpmによる管理がどうなっているか理解していなかったので戸惑った。

あー、でもMacのパワポで絵を描くの大変だから、やっぱりWSLで書こう。
