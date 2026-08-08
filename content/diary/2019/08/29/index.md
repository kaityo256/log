---
title: "2019年8月29日"
date: 2019-08-29T00:00:00+09:00
lastmod: 2019-08-29T00:00:00+09:00
type: diary
source_month: "d201908.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

CentOSでgnuplotでunable to open DISPLAY的なこと言われるなぁ、と思ってたら、そもそもX11入ってなかった。

```sh
sudo yum -y groupinstall "X Window System"
```
