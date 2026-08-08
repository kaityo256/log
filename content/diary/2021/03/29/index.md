---
title: "2021年3月29日"
date: 2021-03-29T00:00:00+09:00
lastmod: 2021-03-29T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

pushし忘れかと思ってた変更、そもそもコミットもしてなかった。うーむ。

Macでlatexが通らない。gsがおかしいらしい。単に実行すると

```txt
$ gs
GPL Ghostscript 9.50: Can't find initialization file gs_init.ps.
```

と言われる。

```sh
$ which gs
/usr/local/bin/gs
```

[X11のとぶつかっているとの噂](https://qiita.com/a_yasui/items/cf69961a0e5801295b9f)。

```sh
brew link --overwrite ghostscript
```

で治った。感謝。
