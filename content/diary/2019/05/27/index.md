---
title: "2019年5月27日"
date: 2019-05-27T00:00:00+09:00
lastmod: 2019-05-27T00:00:00+09:00
type: diary
source_month: "d201905.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Google ColabでMeCabを使う方法。

```py
!apt install aptitude
!aptitude install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y
!pip install mecab-python3==0.7
```

これでMeCabが使えるようになる。以下は日本語の名詞だけ抜き出すサンプル。

```py
node = m.parseToNode("貴社の記者は、貴社の汽車で帰社した。")
while node:
  a = node.feature.split(",")
  if a[0] == u"名詞":
      print(a[6])
  node = node.next
```

```sh
貴社
記者
貴社
汽車
帰社
```

できたっぽい。

MacローカルにもMeCabを入れる。

```sh
brew install mecab mecab-ipadic  
```

これでいけた。おそらくgitやxz、curlも必要だが、もともと入ってたっぽい。
Pythonから使うためのバインディングも入れる。

```sh
pip install --upgrade pip
```
