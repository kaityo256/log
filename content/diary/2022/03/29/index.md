---
title: "2022年3月29日"
date: 2022-03-29T00:00:00+09:00
lastmod: 2022-03-29T00:00:00+09:00
type: diary
source_month: "d202203.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

WSLからWindowsにショートカットを作る。

`$HOME`にファイルを作る。

```sh
cd
echo "Hello" > test.txt
```

```ps1
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\Desktop\test.txtへのショートカット.lnk")
$Shortcut.TargetPath = "$Home\test.txt"
$Shortcut.Save()
```

これを実行すると、デスクトップに`test.txt`へのショートカットを作ることができる。

これは、コマンドラインからは実行できるが、`test.ps1`として実行すると、

```txt
./test.ps1 : このシステムではスクリプトの実行が無効になっているため、ファイル C:\Users\watanabe\test.ps1 を読み込むこと
ができません。詳細については、「about_Execution_Policies」(https://go.microsoft.com/fwlink/?LinkID=135170) を参照してく
ださい。
発生場所 行:1 文字:1
+ ./test.ps1
+ ~~~~~~~~~~
    + CategoryInfo          : セキュリティ エラー: (: ) []、PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

と言われてしまう。セキュリティの問題らしい。

現在のポリシーを知るには`Get-ExecutionPolicy`を実行する。

```ps1
$ Get-ExecutionPolicy
Restricted
```

スコープごとのポリシーの状態を調べるには`-List`を指定する。

```ps1
$ Get-ExecutionPolicy -List

        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser       Undefined
 LocalMachine       Undefined
```

未指定(Undefined)の場合はRestricted(全てのスクリプトの実行を許可しない)が適用される。ポリシー一覧は[こちら](https://docs.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2)。

ここでは、`RemoteSigned`を指定する。これはローカルなスクリプトは署名なしで実行できるが、インターネットからダウンロードされたスクリプトは署名を要求する。スコープは現在のユーザ(CurrentUser)を指定する。変更しようとすると警告が表示される。

```ps1
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

実行ポリシーの変更
実行ポリシーは、信頼されていないスクリプトからの保護に役立ちます。実行ポリシーを変更すると、about_Execution_Policies
のヘルプ トピック (https://go.microsoft.com/fwlink/?LinkID=135170)
で説明されているセキュリティ上の危険にさらされる可能性があります。実行ポリシーを変更しますか?
[Y] はい(Y)  [A] すべて続行(A)  [N] いいえ(N)  [L] すべて無視(L)  [S] 中断(S)  [?] ヘルプ (既定値は "N"): y
```

これで実行できるようになる。

```sh
./test.ps1
```

これをWSLから実行しようとすると「リモート」扱いになるために実行できない。

```sh
$ powershell.exe -File test.ps1
ファイル \\wsl.localhost\Ubuntu\home\username\temp\test.ps1 を読み込めません。ファイル \\wsl.localhost\Ubuntu\home\username\temp\test.ps1 はデジタル署名されていません。このスクリプトは現在のシステムでは実行できません。スクリプトの実行およ
び実行ポリシーの設定の詳細については、「about_Execution_Policies」(https://go.microsoft.com/fwlink/?LinkID=135170) を参
照してください。
    + CategoryInfo          : セキュリティ エラー: (: ) []、ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

`Unrestricted`にすると、毎回実行時に聞かれる。

```sh
$ powershell.exe -File test.ps1

セキュリティ警告
信頼するスクリプトのみを実行してください。インターネットから入手したスクリプトは便利ですが、コンピューターに危害を及ぼ
す可能性があります。このスクリプトを信頼する場合は、この警告メッセージが表示されないように、Unblock-File
コマンドレットを使用して、スクリプトの実行を許可してください。\\wsl.localhost\Ubuntu\home\watanabe\temp\test.ps1
を実行しますか?
[D] 実行しない(D)  [R] 一度だけ実行する(R)  [S] 中断(S)  [?] ヘルプ (既定値は "D"): R
```

`Bypass`にすると、聞かれないで実行されるが、危険なので非推奨。

あと、このままだと文字化けする。SJISで保存する必要がある。`nkf -s`で変換したらうまくいった。

署名の練習。まずはAllSignedにして、PowerShell上でも実行できないようにする。

```ps1
$ Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
$ ./test.ps1
./test.ps1 : ファイル C:\Users\watanabe\test.ps1 を読み込めません。ファイル C:\Users\watanabe\test.ps1 はデジタル署名さ
れていません。このスクリプトは現在のシステムでは実行できません。スクリプトの実行および実行ポリシーの設定の詳細について
は、「about_Execution_Policies」(https://go.microsoft.com/fwlink/?LinkID=135170) を参照してください。
発生場所 行:1 文字:1
+ ./test.ps1
+ ~~~~~~~~~~
    + CategoryInfo          : セキュリティ エラー: (: ) []、PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

[署名の仕方](https://docs.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_signing?view=powershell-7.2)。

```ps1
$params = @{
    Subject = 'CN=PowerShell Code Signing Cert'
    Type = 'CodeSigning'
    CertStoreLocation = 'Cert:\CurrentUser\My'
    HashAlgorithm = 'sha256'
}
$cert = New-SelfSignedCertificate @params
```

これで良いのか。しかし、署名しようとしたらUnknownErrorで失敗。原因不明。あとで調べる。
