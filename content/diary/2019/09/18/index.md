---
title: "2019年9月18日"
date: 2019-09-18T00:00:00+09:00
lastmod: 2019-09-18T00:00:00+09:00
type: diary
source_month: "d201909.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

GitHub Actionsで、pandocのインストールはできるが、お片付けができていない。

```txt
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
##[error]Process completed with exit code 100.
```

sudo つけたらうまくいった。

GitHub ActionsによるGitHub Pagesへのデプロイに失敗。
おそらくTOKEN関連。これは面倒だ・・・。
