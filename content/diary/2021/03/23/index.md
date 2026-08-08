---
title: "2021年3月23日"
date: 2021-03-23T00:00:00+09:00
lastmod: 2021-03-23T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

家のマシンにBLASやLAPACKが入っておらず、原田さんのBSAが動かなかったので入れる。

```sh
sudo apt install libblas-dev
sudo apt -y install libatlas3-base libatlas-base-dev
```

これでBSA/CC2がビルドできた。
