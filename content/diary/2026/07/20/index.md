---
title: "2026年7月20日"
date: 2026-07-20T00:00:00+09:00
lastmod: 2026-07-20T00:00:00+09:00
type: diary
source_month: "d202607.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

数理物理。今日は微分形式。講義前の空き時間になんとか講義準備を済ませる。最後まで順序を迷ったところがあるが、昨年の流れに準じることにした。

これで今年度の数理物理はおしまい。何もみないで黒板ガリガリ90分一本勝負の講義が毎週2回回ってくるのは本当にしんどい。来年からは週1になるが、2年生向けに作り直さないといけないので、それもまたしんどい。

しかし、昨年の自分の講義動画をちゃんと見て、改善点をリストアップしてまた講義に望む、という姿勢は非常に良かった。講義がうまくなった気がする。

期末テスト作った。なんか解答用紙のWordがMacでずれる。仕方ないのでWindowsでPDFにして持ってくる。うーむ。

この日記のGitHub Actionsがだいぶ古くなっていたので更新。どうすればよいかわからなかったので、ほとんどCodexに任せた。

＜ココカラ＞

もともとの`.github/workflows/main.yml`はこんな感じ。

```yaml
# This is a basic workflow to help you get started with Actions

name: Deploy GitHub Pages

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the main branch
on:
  push:
    branches: [ main ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2

      # Runs a single command using the runners shell
      - name: install make and pandoc
        run: sudo apt-get install -y make pandoc
      - name: Run a one-line script
        run: make
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
```

`actions/checkout@v2`が古いのと、`apt-get update`せずに`pandoc`を入れているのが少し気になった。また、`peaceiris/actions-gh-pages`で`docs`を`gh-pages`ブランチにpushする方式だったが、今ならGitHub公式のPages Actionsを使う方が素直らしい。

修正後はこう。

```yaml
name: Deploy GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Install pandoc
        run: |
          sudo apt-get update
          sudo apt-get install -y pandoc

      - name: Build
        run: make

      - name: Disable Jekyll
        run: touch docs/.nojekyll

      - name: Configure Pages
        uses: actions/configure-pages@v6

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v5
        with:
          path: docs

  deploy:
    runs-on: ubuntu-latest
    needs: build

    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v5
```

変更点としては、まず`actions/checkout`を`v2`から`v6`に上げた。デプロイは`peaceiris/actions-gh-pages`をやめて、`configure-pages`、`upload-pages-artifact`、`deploy-pages`の公式構成に変更した。これに伴って、GitHub Pagesの公開元も`gh-pages`ブランチではなくworkflowに切り替えた。

また、`permissions`で`contents: read`、`pages: write`、`id-token: write`を明示した。`deploy-pages`ではPagesデプロイ用の権限とOIDCトークンが必要になるらしい。`workflow_dispatch`も追加したので、pushだけでなく手動でもデプロイできる。`concurrency`はPagesデプロイが重ならないようにする設定。

最初は`configure-pages@v5`、`upload-pages-artifact@v4`、`deploy-pages@v4`にしたところ、Node.js 20に関するwarningが出た。そこでそれぞれ`v6`、`v5`、`v5`に上げたらwarningは消えた。`git push`後にActionsを監視し、buildとdeployが成功するところまで確認した。

＜／ココマデ＞

正直、作業内容を理解できなかったので、上記の＜ココカラ＞・・・＜／ココマデ＞の間はCodexに書いてもらった。おそらく他の場所を読んで記述の癖を僕に寄せている。「・・・はこんな感じ。」のあたりとか。Codexが公式ドキュメントを調べて確定的な情報を得てから書いているのに「OIDCトークンが必要になるらしい。」と、まるで僕が試行錯誤したように書いているのも怖い。

とりあえずpush時のdeployが明らかに早くなった気がする。

自分の個人的な日記すらAIに書いてもらう世界。星新一のショートショートでそういうのあったな・・・
