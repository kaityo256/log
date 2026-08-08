---
title: "2023年6月20日"
date: 2023-06-20T00:00:00+09:00
lastmod: 2023-06-20T00:00:00+09:00
type: diary
source_month: "d202306.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

数理物理、毎回講義の後に質問の列ができて「真面目だなぁ」と思ってたんだけど、単に僕の講義がわかりにくいだけ、という可能性も・・・

計算サーバのノードが死んでる件、どうしようもないので、とりあえず生きているノードだけで回すことにする。まず、

```sh
qmgr -c 'p n hostname'
```

で現在の設定を調べて保存。その上で、つながらないノードを、

```sh
sudo qmgr -c "set node hostname state = offline"
```

で一時的に停止。復活は

```sh
sudo qmgr -c "set node hostname state = free"
```

全状態を調べるには、

```sh
pbsnodes -a
```

毎回調べてる気がするが。とりあえず2ノードだけ活かす設定に変更。これでハンズオンできるはず。
