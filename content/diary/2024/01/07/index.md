---
title: "2024年1月7日"
date: 2024-01-07T00:00:00+09:00
lastmod: 2024-01-07T00:00:00+09:00
type: diary
source_month: "d202401.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

冬タイヤに履き替えた。車検の予約入れた。カーナビの入れ替え予約入れた。

疲れがたまっている。

プログラミング基礎同演習のレポートを採点した。集中力を欠いており、時間がかかってしまった。

npmとnpxの違いがよくわかっていなかったので調べた。npmはパッケージマネージャ。npxは現在インストールされていないものを一時的にインストール、実行、アンインストールする仕組み。一度インストールしたものはnpxで実行する必要はない。また、ローカルにインストールされたもの(npm --save-dev)を実行する場合も、パスを指定しないで実行できるので、npx経由で実行する。なるほど。

package.jsonだけが存在し、node_modulesが存在しない場合、

```sh
npm install
```

だけで必要なパッケージがインストールされる。bundlerと同じだ。bundlerがnpmをマネしたのかと思ったが、bundlerの方が公開が早かったみたい。

textlintが.textlintignoreを無視する問題、textlint-ignore-exampleで試したが、

```sh
npx textlint *
```

だと.textlintignoreが無視されて、

```sh
npx textlint "*"
```

だとちゃんと反映された。よくわからん。これをVSCodeで反映させるにはどうすればいいんだ？
