---
title: "2024年5月18日"
date: 2024-05-18T00:00:00+09:00
lastmod: 2024-05-18T00:00:00+09:00
type: diary
source_month: "d202405.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

川島先生還暦記念会＆BBQ。懐かしい面々。皆さんお久しぶりです。

研究室ウェブサイトまた死んだ。死んでいる状態でmysqldにpidofする。

```sh
$ /usr/sbin/pidof mysqld;echo $?
1

$ sudo service mariadb restart

$ /usr/sbin/pidof mysqld;echo $?
25188
0
```

というわけで、死んでいる状態ならpidofの返り値が1、そうでなければ0となるので、これを使って監視することに。
