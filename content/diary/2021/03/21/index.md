---
title: "2021年3月21日"
date: 2021-03-21T00:00:00+09:00
lastmod: 2021-03-21T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

しばらく前に「Let's Encrypt Expiry Bot」というのからLet's encriptの期限が切れるよ、という連絡が来ていたので調べる。

```sh
$ sudo certbot renew
(snip)
ongratulations, all renewals succeeded. The following certs have been renewed:
  /etc/letsencrypt/live/domainname/fullchain.pem (success)
```

あ、期限を確認しようとして更新しちゃった。

確認方法はこちら。

```sh
sudo openssl x509 -in /etc/letsencrypt/live/domainname/fullchain.pem -noout -dates
notBefore=Mar 21 04:43:17 2021 GMT
notAfter=Jun 19 04:43:17 2021 GMT
```

notAfterの日付が証明書の有効期限。今日更新したから、90日後になっているように見える。

しかし、cronで毎月更新しているはずなのに、なんでうまくいかなかったんだろう？単に実行だけしていたのを、ログも残すようにしよう。

```sh
00 04 * * * certbot renew >> /home/username/log/certbot.log
```

毎月にしていたのを毎日にして、ログを残すようにした。
