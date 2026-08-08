---
title: "2022年12月27日"
date: 2022-12-27T00:00:00+09:00
lastmod: 2022-12-27T00:00:00+09:00
type: diary
source_month: "d202212.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

年内最後の講義。

卒論チェック。

学生さんのMacでscpする時にワイルドカードが使えない問題、原因がわかった。[ZshのGlobbing](https://zsh.sourceforge.io/Doc/Release/Options.html#Expansion-and-Globbing)が問題。もしコマンドラインに何にもマッチしないglobbing expressionが含まれていた場合、Zshはデフォルトでエラーを出す。しかし、scpなどでリモートにファイルがある場合は、実際にはファイルがあるのにマッチしないと判断されてしまう。いろいろ細かい制御ができるっぽいが、とりあえずマッチしなかった時にエラーをださないように

```sh
setopt nonomatch
```

を設定すればOK。scpでのワイルドカードの他、Gitの`HEAD^`などにも影響が出るようだ。

しかしこのglob、英単語だと思ってたら、もともとUNIXの`/etc/glob`というコマンド由来で、このコマンド名はglobalの略だとのこと。初期のUNIXのシェルはワイルドカード展開を`/etc/glob`に依存しており、そのために`*`や`?`といったワイルドカードを`globs`や`globbing`と呼ぶようになったらしい。昔「glob」ってなんだろうと思ってLDOCEで調べたら[存在していた](https://www.ldoceonline.com/jp/dictionary/glob)ので、その単語由来だと思ってた。そちらの方のglobは、なんか液体か泥の塊のことらしい。「a glob of ketchup(ケチャップ一山)」みたいに使う。
