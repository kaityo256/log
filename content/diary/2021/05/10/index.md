---
title: "2021年5月10日"
date: 2021-05-10T00:00:00+09:00
lastmod: 2021-05-10T00:00:00+09:00
type: diary
source_month: "d202105.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

というわけで日記merge。さらに職場でもpush忘れ防止プロンプト利用。

push忘れは`git status -b`を使う。

以下、再チェックが必要。

上流ブランチなし。

```sh
$ git status -sb
## main
```

未プッシュなし、未コミットあり。

```sh
$ git status -sb
 M log/d202105.md
```

↓コミット

未プッシュあり、未コミットなし。

```sh
$ git status -sb
## main...origin/main [ahead 1]
```

↓プッシュ

未プッシュなし、未コミットなし。

```sh
$ git status -sb
## main...origin/main
```

多分これだけで未プッシュコミットがあるか確認できる気がするが、念の為`git log`で未プッシュログがあるかどうかを確認している。

```sh
git log origin/main..main
```

この表示があるかないかで未プッシュコミットがあるかどうか調べることができる。これ、やっぱりいらん気がするな。
