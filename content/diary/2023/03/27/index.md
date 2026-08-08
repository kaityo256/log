---
title: "2023年3月27日"
date: 2023-03-27T00:00:00+09:00
lastmod: 2023-03-27T00:00:00+09:00
type: diary
source_month: "d202303.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

実験ガイダンス。

Kudosから、「お前の論文の簡単な紹介を書け」と言われたので[書いてみた](https://www.growkudos.com/publications/10.1063%252F5.0138733/reader)。

Kudosって何かと思ったが、英国発ベンチャーで、多くの出版社と提携しているらしい。10年ほど前にベータ版に参加してくれ、というメールが来てた。

KudosとORCiD連携する時に出てくる「認証済みのアクセス」「アクセスを拒否」って、何を直訳したものなんだろうと調べてみたら「Authorize access」と「Deny access」だった。なぜか「Authorize access」が「Authorize「d」 access」として訳されているっぽい。Google翻訳でもDeepLでも普通に「アクセスを許可する」になるんだけど、ローカライズに古い翻訳ソフトを使って、そのままになってるのかな？

VSCodeのスニペットが効かなくなって困っていたが、単に開くフォルダを間違えていただけだった。ローカルの`.vscode`に登録されているので、別のフォルダを開くと使えなくなってしまう。

途中まで書いた講義ノートのRe:VIEW化メモ。

* Dockerを立ち上げる。
* Re:VIEW用のディレクトリを掘る(reviewがあったので、今回はbuildに)
* 既存のRe:VIEWディレクトリからconfig.ymlをコピーして、タイトルなどを修正
* css, lib, layouts, styなどのディレクトリをコピー
* style.cssをコピー
* Rakefileをコピー
* review-ext.rbもコピー
* cancelが使えなかった→ sty/mystyle.styでusepackage{cancel}で解決

とりあえず目次だけでもなんとかなるように書いた。今の所B5で63ページ。進捗度50%くらい？ヤバい。
