---
title: "2022年1月31日"
date: 2022-01-31T00:00:00+09:00
lastmod: 2022-01-31T00:00:00+09:00
type: diary
source_month: "d202201.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

おお、１月が終わってしまう。

Google Chrome、Windows版はBASIC認証を覚えてくれるんだけど、Mac版が覚えてくれない。原因不明。

そろそろ3年生向けのハンズオンを始めたい。昨年はどういう順序で何をやったか覚書。

* 3/4 論文の読み方、探し方
* 3/11 Vimハンズオン
* (事前にXを飛ばせるようにしておいた？)
* (PythonとVSCodeのハンズオンは飛ばした？)
* 3/18 Dockerハンズオン 
* 3/25 gnuplotハンズオン
* 4/1 Gitハンズオン
* 4/8 GitHubハンズオン
* 4/15 LammpsとVMDハンズオン
* 4/22 MarkdownとLaTeX記法ハンズオン
* 5/5 物性研スパコンハンズオン
* 5/12 GNU makeハンズオン
* 5/20 PBS ハンズオン (バッチシステム)
* 5/27 ParaViewハンズオン
* 6/3 機械学習ハンズオン (TensorFlowでFashion-MNISTを学習させてウェブで読み込む)

去年やっていないのは以下のヤツかな。

* Pythonのインストール
* VSCodeのインストール
* LastPassと多要素認証 (今年はやりたい)
* SSHエージェント転送の設定 (WSLの記述を修正する必要あり) (今年はやりたい)
* X Window Systemのインストール(Winだけ)
* C++のコンパイルとSIMDの確認
* LaTeXのインストール (今年はやりたい)

どこかでSSHとエージェント転送について説明を入れたいなぁ。昨年、LaTeXの説明を忘れてて、卒論直前にやることになったから、これは早めにやっておきたい。MarkdownとLaTeX記法のハンズオンの後が良いかな。

後で情報を整理しておかないと。

プログラミング基礎同演習採点終了。

Ashkin-Teller模型勉強続き。G. Delfino, P. Grinza /Nuclear Physics B 682 (2004) 521–550を読んでる。

Ashkin-Teller模型は、staggered 8-vertex modelにmapできる(Wegner 1972)。これはa,b,c,dのウェイトのうち、cとdがA-sublatticeとB-sublatticeで交代する、というもの。従って、c=dの場合はunstaggered 8-vertex modelになり、これは可解となる。となる。この、c=dに対応するのが、Ashkin-Tellerではsinh(2J)=exp(-2K)。従って、この線上ではずっとcriticalとなる。

ただ、この対応がまだわからない・・・
