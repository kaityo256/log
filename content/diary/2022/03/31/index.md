---
title: "2022年3月31日"
date: 2022-03-31T00:00:00+09:00
lastmod: 2022-03-31T00:00:00+09:00
type: diary
source_month: "d202203.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Ubuntu側でPowerShellを呼び出す。

```sh
$ cat test.ps1
echo Hello

$ powershell.exe ./test.ps1
./test.ps1 : ファイル \\wsl.localhost\Ubuntu\home\watanabe\test.ps1 を読み込めません。ファイル \\wsl.localhost\Ubuntu\home\watanabe\test.ps1 はデ
ジタル署名されていません。このスクリプトは現在のシステムでは実行できません。スクリプトの実行および実行ポリシーの設定の詳細については、「about_Exe
cution_Policies」(https://go.microsoft.com/fwlink/?LinkID=135170) を参照してください。
発生場所 行:1 文字:1
+ ./test.ps1
+ ~~~~~~~~~~
    + CategoryInfo          : セキュリティ エラー: (: ) []、PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

うまくいかない。

Powershell側でセキュリティポリシーにBypassを指定。

```sh
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
```

WSL側でもう一度実行。

```sh
$ powershell.exe ./test.ps1
Hello
```

実行できた。

テンポラリファイルの作成は`mktemp`

```sh
$ mktemp
/tmp/tmp.zmT3f40DJj

$ mktemp
/tmp/tmp.H5kr0JbakZ
```

これにps1つければよさそうだな。

```sh
echo `mktemp`.ps1
/tmp/tmp.qkOuZhtCSi.ps1
```

PowerShell側で引数受け取りやファイル名抽出やって完成。備忘録として[記事](https://zenn.dev/kaityo256/articles/make_shortcut_from_wls)にしておいた。

研究室ミーティング。トラブルにより輪講は延期。

片桐さんと大島さんの教科書、[書評書いた](https://note.com/kaityo256/n/n557d337ce71f)。比較のために数値解析の基礎 (篠原 能材著 理工学基礎シリーズ 日新出版)を引っ張り出したが、付箋がいっぱいついてる。結構がんばって読んでたんだな。

Amazonでの[このレビュー](https://www.amazon.co.jp/gp/customer-reviews/R95V53KX30B4O/ref=cm_cr_arp_d_rvw_ttl?ie=UTF8&ASIN=4817300973)、多分著者本人だな・・・

家に帰る際、急に猛烈な吐き気。家に帰って吐いてしまった。
