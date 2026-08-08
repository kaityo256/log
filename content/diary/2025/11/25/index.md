---
title: "2025年11月25日"
date: 2025-11-25T00:00:00+09:00
lastmod: 2025-11-25T00:00:00+09:00
type: diary
source_month: "d202511.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

午前中はD論予備審査。

午後、1on1したりとか。

土日の疲れが溜まっており、全く頭が働かない。

計算ノードにImageMagick入れた。

ずっとファイルサーバにログインできなかったのをなんとかした。rootパスワードを引っ張り出す。そして入って調べた。ログインできなかった理由は、ファイルサーバにユーザがなかったため。ファイルサーバなので`/home`は存在していてNFS exportしている。それとgidやuidを無矛盾に作らないといけない。
自分のアカウントのログインノードでのuid, gidは1001なので、

```sh
groupadd -g 1001 watanabe
useradd \
  -u 1001 \
  -g 1001 \
  -d /home/watanabe \
  -s /bin/bash \
  watanabe
```

これでできた。あとはsudoersに追加したり、パスワードを設定したり。これでファイルサーバにアクセスできるようになった。

これで、ログインノード、計算ノード x N、ファイルサーバという構成を作る記事を書く準備はできた。書くのか？令和にもなってNIS+NFS+ホストベース認証+Slurmという記事を？

頭が全く働かず、論文修正までいけない。
