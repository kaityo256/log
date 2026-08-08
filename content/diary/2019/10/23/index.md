---
title: "2019年10月23日"
date: 2019-10-23T00:00:00+09:00
lastmod: 2019-10-23T00:00:00+09:00
type: diary
source_month: "d201910.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物性研にジョブを投げた。g=0.55のジョブ。
様子見でサンプル数は少なめ。96サンプル* 18色。
時間を測定している。うまくいったらより多くのサンプルを取る。
緩和時間が短いかもしれない。

4ノード、L=128で10000ループで40秒。サンプル数を96とすると1分程度。
100倍で100分。L=256まではいける？とりあえずループ数10倍の

```txt
ThermalizationLoop = 100000
ObservationLoop = 100000
```

で様子見(g=0.55/g=0.70ともに)。

g = 0.55では、低温で明らかに緩和不足。0.7は低温過ぎる。最低でも0.75からにしたほうが良い。
0.9は不要。0.85までで良い。
0.75から0.85まで100点程度あれば十分。

g = 0.70では1.2から1.4まで100点あればよさそう。

g=0.55、L=64,128,256のジョブを投げた。

g = 0.55のデータ。

```yaml
ND: 100
tmin: 0.75
tmax: 0.85
g: 0.55
SamplingNumber: 32
ObservationLoop: 1000000
ThermalizationLoop: 1000000
```

g = 0.70のデータ。

```yaml
ND: 100
tmin: 1.2
tmax: 1.4
g: 0.70
SamplingNumber: 32
ObservationLoop: 1000000
ThermalizationLoop: 1000000
```
