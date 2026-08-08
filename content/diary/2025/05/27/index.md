---
title: "2025年5月27日"
date: 2025-05-27T00:00:00+09:00
lastmod: 2025-05-27T00:00:00+09:00
type: diary
source_month: "d202505.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

サーバの再インストールにより、再度ホストベース認証を通るようにした。ログインノードはFQDNによる指定が必要など、いくつか罠があったが、とりあえず作業メモは残した。

一番のポイントはsshdを別ポートでデバッグ用に開くこと。

サーバ側

```sh
sudo /usr/sbin/sshd -d -p 2222
```

クライアント側

```sh
ssh -o PreferredAuthentications=hostbased -vvv servername
```

これで、サーバのデバッグログが取れる、もとのsshdが壊れない(失敗するとログインできなくなる)というメリットがある。また、地味にクライアント側でホストベース認証のみに制限するとログが見やすくなって便利。

また査読が・・・　いろいろ重い。

解析力学の教科書が届いた。
