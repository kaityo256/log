---
title: "2023年1月18日"
date: 2023-01-18T00:00:00+09:00
lastmod: 2023-01-18T00:00:00+09:00
type: diary
source_month: "d202301.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Granger causality、statsmodelsをインストールして、

```sh
python3 -m pip install statsmodels   
```

必要なものをインポートして、

```py
from statsmodels.tsa.stattools import grangercausalitytests
```

適当にデータを作ってgrangercausalitytestsに食わせると

```py
grangercausalitytests(data, maxlag=[1])
```

結果が出てくる。楽ちんすぎる。dataは、`[N, 2]`の形の二次元配列で、二番目の変数が一番目の配列のデータにcausalityがあるかどうかを出力する。逆向きを調べたければ、

```py
grangercausalitytests(data[:, [1,0]], maxlag=[1])
```

でOK。VARモデルのtest_causalityだと、単なる乱数同士でもcausalityが出てしまう(棄却できない)。
