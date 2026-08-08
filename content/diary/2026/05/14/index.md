---
title: "2026年5月14日"
date: 2026-05-14T00:00:00+09:00
lastmod: 2026-05-14T00:00:00+09:00
type: diary
source_month: "d202605.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

シミュレーション工学、講義の感想に返事。感想が減ってきて悲しいね。

ハンズオンの準備。Macでサーバ越しにVMDを起動できない(OpenGLがおかしい)のが面倒だ。

まず、Macで

```sh
$ glxinfo  
name of display: /private/tmp/com.apple.launchd.C9pbzRLXL1/org.xquartz:0
X Error of failed request:  BadValue (integer parameter out of range for operation)
  Major opcode of failed request:  129 (Apple-DRI)
  Minor opcode of failed request:  2 ()
  Value in failed request:  0x600003
  Serial number of failed request:  22
  Current serial number in output stream:  22
```

なんかApple-DRIを使おうとして死んでいるらしい。

```sh
defaults write org.xquartz.X11 enable_iglx -bool true
defaults write org.xquartz.X11 nolisten_tcp -bool false
```

研究室ミーティング。今日は「Diplomacy」というゲームのAIの紹介と、PPOの紹介。すっかりゲーム＆機械学習の研究室になりつつあるな・・・

ずっと積んでた旅費の申請した。

なんかいろいろ片付けたんだけど、研究が進んでないのが悲しいなぁ。

散髪した。
