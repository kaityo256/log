---
title: "2022年4月26日"
date: 2022-04-26T00:00:00+09:00
lastmod: 2022-04-26T00:00:00+09:00
type: diary
source_month: "d202204.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

実験。

ミーティング。

スライドは53ページまで。ヤバくない？

直前にコミットしたはずなのに、GitHubのログが「4days ago」とかになっていて、調べたらWSL2の時計が恐ろしく狂っていた。なんとかしないといけない。

まずはcrontabで`hwclock -s`を実行したいが、これにはroot権限が必要だ。というわけで`/etc/sudoers`に

```sh
watanabe AL=NOPASSWD: /usr/sbin/hwclock
```

を追加。これで、`sudo hwclock -s`がパスワードなしになった。あとはこれをwatanabe権限のcronで実行すればよいだけのはず？

WSLでcronはデフォルトで走っていない。

```sh
sudo service cron start
```

では走らせることができる。これをWindows起動時に自動でやっても良いが、確認自体は

```sh
$ service cron status
* cron is not running
```

で調べることができるので、ログイン時に確認して、cronが動いてなければ動かす、で良い気がする。
