---
title: "2023年11月30日"
date: 2023-11-30T00:00:00+09:00
lastmod: 2023-11-30T00:00:00+09:00
type: diary
source_month: "d202311.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

11月が終わってしまう。

[【11/24更新】サム・アルトマン氏 OpenAI解任報道まとめ。マイクロソフト入社から一転、電撃復帰へ](https://aismiley.co.jp/ai_news/sam-altman-openai-retirement/)

メモ。おそらくあとで歴史になるから。僕らは歴史の証人になりつつある。

研究室ミーティング。「Pythonを使っている人向けのC/C++解説」。面倒くさそうだから公開はしません。

輪講。大変素晴らしい発表。

教科書を書くためにtextlintを導入したが、プロジェクトローカルにtextlintをインストールした上で、VSCodeにはtextlint-vscodeを入れてしまったため、textlintが入ってないディレクトリで不具合が生じた。仕方ないのでグローバルにインストールする。

```sh
nvm use v20.9.0
npm install -g textlint
npm install -g npm@10.2.4 
```

これで警告は減ったが、まだ`.textlintrc`が無いよと言われる。ルートディレクトリに`.textlintignore`を置いても駄目。各ディレクトリで`touch .textlintrc`を実行。これ、良い方法ないかなぁ。

nvmがログインのたびに古いバージョンを見てしまう問題、

```sh
 nvm alias default 20.9.0 
```

で解決した。

渡辺研配属面接の案内流した。

課題研究発表会の要旨提出確認した。

卒論の日程を確認した。修論も確認しないとな。

あー、学科分け説明会の準備ができていない。
