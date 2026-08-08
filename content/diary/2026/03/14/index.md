---
title: "2026年3月14日"
date: 2026-03-14T00:00:00+09:00
lastmod: 2026-03-14T00:00:00+09:00
type: diary
source_month: "d202603.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

品岡さんに「ChatGPT Plus契約してたらcodex使えますよ」と言われて確認する。

まず、nvmを入れる。うちの環境ではすでに入っていた。

次にNode 22を入れる。

```sh
nvm install 22
```

```sh
$ node -v
v22.22.1
```

入ったな。デフォルトに固定しておく。

```sh
nvm alias default 22
```

次、codexのインストール。

```sh
npm i -g @openai/codex
```

```sh
$ codex -V
codex-cli 0.114.0
```

codexを実行。

```sh
$ codex
  Welcome to Codex, OpenAI's command-line coding agent

  Sign in with ChatGPT to use Codex as part of your paid plan
  or connect an API key for usage-based billing

> 1. Sign in with ChatGPT
     Usage included with Plus, Pro, Business, and Enterprise plans

  2. Sign in with Device Code
     Sign in from another device with a one-time code

  3. Provide your own API key
     Pay for what you use

  Press Enter to continue
```

するといくつか選択肢が出るので「> 1. Sign in with ChatGPT」を選ぶ・・・と固まる。ChatGPTに聞いたら、WSLでブラウザ経由の認証が通らないのは[既知の問題](https://github.com/openai/codex/issues/7908)らしい。

仕方ないのでデバイスコード認証にする。事前にブラウザ側でデバイスコード認証を開いておく必要がある。

```sh
codex login --device-auth
```

を実行。あとは指示に従う。具体的には指示されたURLをブラウザで開き、ターミナルに表示されているone-time codeをブラウザに入力すればOK。

これで僕もAgentic Codingデビュー。

物理学会Jrセッション審査。みなさん発表上手ですね。
