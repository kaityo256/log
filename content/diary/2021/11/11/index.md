---
title: "2021年11月11日"
date: 2021-11-11T00:00:00+09:00
lastmod: 2021-11-11T00:00:00+09:00
type: diary
source_month: "d202111.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室ミーティング。三人発表。

なぜか急にプリンタがネットワークに繋がらなくなった。無線経由だとどうしても駄目。仕方なく有線でつないだ。このせいで必要な書類が印刷できずにしばらく困った。

いろいろと予定がやばい。論文に手をつけることができない。

論文を更新しようとlatexdiffを使ってみたが、なぜか通らない。別のやつなら通る。何が問題なんだ？

まず、latexindentが動かない。VSCodeの「出力」の「LaTeX Workshop」を見ると、`Log::Log4perl`が無いせいっぽい。[この記事](https://qiita.com/khys/items/332c3a3f34a82acf7a7a)に従ってインストール。

駄目だ。Macだと動かないが、WSLだと普通に動く。そっちで続きをやるか。

```sh
sudo apt update
sudo apt upgrade
sudo apt install latexdiff
```

WindowsもMacもアップデートにすげー時間がかかってる。非本質的なところで時間がかかって非常にイヤな感じ。

WSL2ではうまくlatexdiffできた。まずはMacを諦める。

WSL2のUbuntuにlatexindentを入れる。

```sh
sudo apt install texlive-extra-utils
```

これでインデントはできるようになった。なぜかon saveでフォーマッタが走らないけど、まぁいいや。WSL2ではlatexdiffも問題なく動いた。よしよし。
