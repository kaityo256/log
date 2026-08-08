---
title: "2023年4月26日"
date: 2023-04-26T00:00:00+09:00
lastmod: 2023-04-26T00:00:00+09:00
type: diary
source_month: "d202304.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

機能のSudoku minlex、ちゃんと確認したら普通にバグってる。Windowsの問題かと思ったら、linuxでもMacでもバグってるので普通にバグだな。

PRMLの輪講、明日当番(というか教員による本読み輪講の模範演技)なので準備。再現コードをほとんどChatGPTに書かせた。簡単なコードなら、ほぼ3.5で用が足りるなぁ。

続けて明日のハンズオンの準備。protobufのバージョン不一致により動かない。仕方なく

```sh
python3 -m pip install protobuf==3.20.*
```

とバージョン指定で上書きインストールで回避。

また、GitHub Pagesで実行していたのを、VSCodeのLive serverで対応するように修正。あと、なぜかfashon_mnist_checkのindex.htmlがおかしくなっていたので修正。
