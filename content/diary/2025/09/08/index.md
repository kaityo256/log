---
title: "2025年9月8日"
date: 2025-09-08T00:00:00+09:00
lastmod: 2025-09-08T00:00:00+09:00
type: diary
source_month: "d202509.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

小林さんのRBM論文がarXivに出た。

[https://arxiv.org/abs/2509.04899](https://arxiv.org/abs/2509.04899)

RBMライブラリも公開。

[https://github.com/watanabe-appi/simple_rbm](https://github.com/watanabe-appi/simple_rbm)

RBMが作曲した曲や和音進行が聞けるサイトも作成。

[https://watanabe-appi.github.io/rbm-music-demo/](https://watanabe-appi.github.io/rbm-music-demo/)

ずっとarXivでのコンパイルに苦労していたのだが、`graphicx`パッケージの`dvipdfmx`オプションが悪さをしていることが判明。

REVTeXなら、

```tex
\usepackage{graphicx}
```

として、JPSJなら`jpsj3.cls`の

```tex
\RequirePackage[dvipdfmx]{graphicx}
```

を

```tex
\RequirePackage{graphicx}
```

に変えて、コンパイラを`pdflatex`にしたらarXivでもすぐにビルドできて、図も正しく表示できるようになった。

これまで、PDFをepsに変えて対応していたのだが、これからはそれをしなくて良さそう。やれやれだ。

JPJSの著作権移譲書類、前回は忘れていたので、今回はすぐに返さないと。これ、ウェブでなんとかならんかなぁ。

2025年度秋学期安全教育実施報告した。

論文の査読への返事の準備をした。具体的にはリポジトリにディレクトリ掘って、`reply.tex`を作って、論点を`README.md`にまとめた。

自分の査読レポートの返事も返ってきたなぁ。

いずれにせよ、今日はようけ働いた。
