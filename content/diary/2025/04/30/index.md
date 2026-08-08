---
title: "2025年4月30日"
date: 2025-04-30T00:00:00+09:00
lastmod: 2025-04-30T00:00:00+09:00
type: diary
source_month: "d202504.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

昨日もっと忙しかったよなぁ、と思い返してみたら、査読レポート書いて返してたわ。なんかもうTodoistに書いていないことは全く覚えてない。
TodoistというかLogistになっている。

教科書の著者プロフィールのチェック。「博士課程」ではなく「博士後期課程」ではないか？という指摘で調べてみた。少なくとも2025年現在の募集要項を確認すると、東京大学大学院理学系研究科は「博士課程」、東京大学大学院工学系研究科は「博士後期課程」と書いてある。

学位記には「博士課程」って書いてあるんだけどなぁ。

重い腰を上げてGoをインストールする。

```sh
brew install go
```

```sh
mkdir ooxmlgrep
cd ooxmlgrep
go mod init github.com/kaityo256/ooxmlgrep
```

GoのBuild方法がよくわからない。タスクを使ってみる。

```sh
brew install go-task/tap/go-task
```

これで`task build`でビルドできるようになった(そうなるようにTaskfile.ymlを作る)。

```sh
brew install goreleaser
```

```sh
goreleaser release --snapshot --clean
```

でリリース準備ができることを確認(READMEとかLICENSEが必要)。

```sh
git tag v0.1.0
git push origin v0.1.0
```

GitHub側でPublish Release。

ghを入れてなかったのでインストール。

```sh
brew install gh
```

```sh
gh auth login
export GITHUB_TOKEN=$(gh auth token)
```

あとは

```sh
goreleaser release --clean
```

で最新のTagについて勝手にリリースを作ってくれる。

というわけでpptxgrepのGo版ができたぞ。あっという間だったなぁ・・・

[github.com/kaityo256/ooxmlgrep](https://github.com/kaityo256/ooxmlgrep)

```sh
go install github.com/kaityo256/ooxmlgrep@latest
```

でインストール可能。簡単、便利、動作もD言語版より圧倒的に早い！(なんでだろ？)

いやしかし、D言語版があったとはいえ、Go全く未経験の状態から、Goへの移植、プロジェクトの作成、複数プラットフォームへの対応、リリースまで1時間半ですか。今回はChatGPTを使ったのでコピペベースだったが、MCPを使えばより早くなっただろう。AI時代の開発速度はほんとうに目まぐるしいな。

明日の発表スライド作った。結構時間かかったな。
