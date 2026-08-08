---
title: "2026年8月5日"
date: 2026-08-05T00:00:00+09:00
lastmod: 2026-08-05T00:00:00+09:00
type: diary
source_month: "d202608.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

スパコン一週間、パワポの英訳をしようとしてChatGPTに聞いたら、「まず対訳表を作ると良いですよ」と言われたので、対訳表を作るようにPLANS.mdを更新してcodexに投げる。するとPythonのpython-pptxパッケージを使って日本語を取得、対訳表をCSVで作って僕がそれを確認、OKを出したらPowerPointが翻訳された。すげぇ。

なんかGitHubにDependabotというボットからプルリクエストが来ている。最初、SPAMかと思ったが、GitHubの機能らしい。

いろいろ調べた(というかCodexに聞いた)が、マージできる奴とできない奴があるので、マージできる奴はマージ、できない奴はbotに無視しろとコメントすることに。っていうか、Codexにghコマンドの権限渡して「はいはい」って言うだけ。

Botに無視しろといったPRは[これ](https://github.com/kaityo256/sevendayshpc/pull/29)。

AIに作らせたGitHub Actionに、GitHubのbotがプルリクを作り、それをAIにレビューさせてAIが「ignore this major version」と(僕を通じて)返事をして、botが「OK, I won't notify you about version 7.x.x again, unless you re-open this PR.」と返事をしてきた。

もう近未来とかそういう雰囲気を超えている。

っていうか、Codexが.github/dependabot.ymlを作成しているな。これでbotが反応したのか。

```yaml
version: 2
updates:
  - package-ecosystem: npm
    directory: /
    schedule:
      interval: weekly

  - package-ecosystem: github-actions
    directory: /
    schedule:
      interval: weekly
```

論文のイントロ書き直した。全体をチェックしてから共著者に送った。もうすぐ再投稿できるはず。

学生さんのジョブも投げた。

理事の仕事までは手をつけられなかった・・・
