---
title: "2026年4月28日"
date: 2026-04-28T00:00:00+09:00
lastmod: 2026-04-28T00:00:00+09:00
type: diary
source_month: "d202604.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

MacにSlidevをインストール。

まず、nodeとnpmがあることを確認。

```sh
$ node -v
v22.22.1
$ npm -v
11.11.1
```

Slidevをグローバルにインストール。

```sh
$ npm install -g @slidev/cli
$ slidev --version
52.14.2
```

あとは`npm create slidev@latest`してプロジェクト名決めるだけ。自動でブラウザが立ち上がる。

次からは、当該プロジェクトディレクトリで

```sh
npm run dev
```

でOK。

スライドはSubversionで管理していたんだけど、Slidevとの相性が非常に悪い。しかしpptxなどをGit管理したくない。

・・・ということをChatGPTに相談したらGit LFSを使っては？とのこと。ふむ。動画などの管理にはよさそう。

オンライン会議。なぜかビデオがオンにならず焦ってわけわからないことを話してしまった。Windowsを再起動したらつながった。何がおきたんだろう？

AIを使って専門家と議論する話、別にAIを使った知識ブーストで専門家と話すことがまずいんじゃなくて、何か人に言われた時に「いや、でもAIはこう言っていますよ」というのは、「私はあなたの意見よりもAIを信じます」という意思表明であって、それならずっとAIと話していてください、としか・・・

まぁ、そもそも僕は「議論」は意味があまりないと思っている。人とのコミュニケーションで有益なのは、専門知識を持った人から持っていない人への一方的な情報提供。しかし、情報をもらうだけでは駄目だ。僕は他の専門家から情報をもらう。だから僕も誰かに情報を提供できる側でありたい。

VSCodeのMarkdownでLaTeXの補完をしたい。LaTeX Workshopが入っている状態で

```json
"[markdown]": {
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  }
}
```

を設定。これでいけた。

Markdown+LaTeX記法ハンズオン。

なんかまだバタバタしている。
