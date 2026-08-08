---
title: "2024年12月16日"
date: 2024-12-16T00:00:00+09:00
lastmod: 2024-12-16T00:00:00+09:00
type: diary
source_month: "d202412.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Subversionでトラブった時、もはや手動で治すの無理だなぁ。

```txt
以下の解決方法。svn: E155010: コミットに失敗しました (詳しい理由は以下のとおりです):
svn: E155010: 'hoge.pdf' は追加準備状態となっていますが、存在しません
```

というエラーが出て、修正ができなくなった。ChatGPTに聞いて以下のようにして解決。

```sh
svn revert hoge.pdf
```

これで、

```sh
$ svn st
!M hoge.pdf
```

となる。`!M`は、ファイルが紛失している状態。revertで復活できなかったので削除。

```sh
svn delete hoge.pdf
svn commit -m "delete hoge.pdf"
```

これで解決。
