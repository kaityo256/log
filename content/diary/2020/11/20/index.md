---
title: "2020年11月20日"
date: 2020-11-20T00:00:00+09:00
lastmod: 2020-11-20T00:00:00+09:00
type: diary
source_month: "d202011.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

レポートの採点。やっぱり数時間かかってしまう。

とりあえずこのログをレスポンシブに対応してみた。具体的には画像とコードがはみ出さないように修正。

Kaggleもくもく会。いい加減Titanicにあきたので、Getting Startedから家の値段を調べる奴に挑戦。とりあえず回帰してみたが全然ダメだった。次は過学習してもいいからget_dummiesで全部のせでやってみるかな。

`np.tensordot`で、潰した軸が一番右にずれるの忘れてた。

```py
import numpy as np

A = np.zeros((2, 3, 4))
B = np.zeros((2, 5))
C = np.tensordot(A, B, (0, 0))
print(C.shape)  # => (3,4,5)
```

最後、shapeが(5,3,4)になることが期待されるところ、(3,4,5)と移動してしまっている。

「卒論の書き方」のスライド作りはじめた。
