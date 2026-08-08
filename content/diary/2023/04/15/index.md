---
title: "2023年4月15日"
date: 2023-04-15T00:00:00+09:00
lastmod: 2023-04-15T00:00:00+09:00
type: diary
source_month: "d202304.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

家のWSL、起動したら「.wslconfigにswapという不明なキーがある」とかいうエラーがでる。ググってもよくわからなかったのでChatGPTに聞いてみたら、これはWSL2のスワップファイルを無効にする設定らしい。「WSL2 スワップ」で調べたら出てきた。

```txt
swap=0
```

となっていたのを

```txt
[wsl2]
swap=0
```

にしなければならなかったらしい。昔懐かしいINIファイル形式ですね。

```sh
$ free
              total        used        free      shared  buff/cache   available
Mem:        3971012      647168     2154684        2292     1169160     3088976
Swap:             0           0           0
```

うん、ちゃんとSwapがゼロになった。何かで`[wsl2]`が消えてしまったか、それとも仕様が変わったかな。
