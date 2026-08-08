---
title: "2023年10月5日"
date: 2023-10-05T00:00:00+09:00
lastmod: 2023-10-05T00:00:00+09:00
type: diary
source_month: "d202310.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

気温が急激に下がった。体調を崩したか？

Markdown→Re:VIEW→(LaTeX)→PDFという形で執筆しているのだが、図の参照をして欲しい、という要望。Markdownには図の参照機能がないが、Re:VIEWにはある。Re:VIEWでは、

```re
//image[vcs_history][vcs_history]{}
```

という形で図を読み込み、

```re
@<img>{vcs_history}
```

という形で参照する。面倒なので、Markdown側で

```md
![vcs_history](fig/vcs_history.png)

簡単にバージョン管理システムの歴史を見てみよう(@<img>{vcs_history})。
```

としてそのまま突っ込んだらうまくいった。とりあえずこれでやって、エラーが出たら考えよう。

なんかRe:VIEWの図の参照機能、公式ドキュメント読んでもよくわからず、結局ChatGPTに聞いた。ChatGTPすごい。

というわけで書籍の執筆を進める。もともとがわりと無理やり詰め込んだ講義ノートだったので、本にしようと思うといろいろ気になるところが出てくるなぁ。
