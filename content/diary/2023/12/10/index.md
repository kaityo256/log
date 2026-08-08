---
title: "2023年12月10日"
date: 2023-12-10T00:00:00+09:00
lastmod: 2023-12-10T00:00:00+09:00
type: diary
source_month: "d202312.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

WSLのターミナルで`code .`と入力したらエラー。

```sh
$ code .
Updating VS Code Server to version af28b32d7e553898b2a91af498b1fb666fdebe0c
Removing previous installation...
Installing VS Code Server for x64 (af28b32d7e553898b2a91af498b1fb666fdebe0c)
Downloading: 100%
Failed
--2023-12-10 00:50:11--  https://update.code.visualstudio.com/commit:af28b32d7e553898b2a91af498b1fb666fdebe0c/server-linux-x64/stable
update.code.visualstudio.com (update.code.visualstudio.com) をDNSに問いあわせています... 13.107.246.46, 13.107.213.46, 2620:1ec:bdf::46, ...
update.code.visualstudio.com (update.code.visualstudio.com)|13.107.246.46|:443 に接続しています... 接続しました。
エラー: update.code.visualstudio.com の証明書(発行者: `CN=Microsoft Azure RSA TLS Issuing CA 08,O=Microsoft Corporation,C=US')の検証に失敗しました:
  発行された証明書はまだ有効ではありません。
update.code.visualstudio.com に安全の確認をしないで接続するには、`--no-check-certificate' を使ってください。
ERROR: Failed to download https://update.code.visualstudio.com/commit:af28b32d7e553898b2a91af498b1fb666fdebe0c/server-linux-x64/stable to /home/watanabe/.vscode-server/bin/af28b32d7e553898b2a91af498b1fb666fdebe0c-1702137011.tar.gz
Please install missing certificates.
Debian/Ubuntu:  sudo apt-get install ca-certificates
```

証明書が有効でないというエラー。あれ？と思ってChatGPTに証明書の有効性を確認するコマンドを聞いて実行。

```sh
$ openssl s_client -servername update.code.visualstudio.com -connect update.code.visualstudio.com:443 | openssl x509 -noout -dates
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root G2
verify return:1
depth=1 C = US, O = Microsoft Corporation, CN = Microsoft Azure RSA TLS Issuing CA 08
verify return:1
depth=0 C = US, ST = WA, L = Redmond, O = Microsoft Corporation, CN = update.code.visualstudio.com
verify error:num=9:certificate is not yet valid
notBefore=Dec  9 18:17:28 2023 GMT
verify return:1
depth=0 C = US, ST = WA, L = Redmond, O = Microsoft Corporation, CN = update.code.visualstudio.com
notBefore=Dec  9 18:17:28 2023 GMT
verify return:1
notBefore=Dec  9 18:17:28 2023 GMT
notAfter=Jun  6 18:17:28 2024 GMT
```

「verify error:num=9:certificate is not yet valid」。まだ有効でない？ここで、さっきのメッセージに「発行された証明書は **まだ** 有効ではありません。」と書いてあったことに気づく。WSLの時計がずれてたんだ。

```sh
sudo /usr/sbin/hwclock -s
```

これで動いた。10分毎に実行するようcronに入れてたんだけど、実行されてないっぽいなぁ。

JCPのProof見た。「Fig. 10 (a)」みたいな奴、わざわざ「Fig.~\ref{fig:label}~(a)」と、括弧前に空白を入れてたんだけど、Proofでは消されている。

塩漬け仕事、一つ片付けた。すぐ終わるんだけど、なんか腰が重いんだ。

1. 届いた荷物を片付けるため、遠い部屋に行く
1. 鍵を居室に忘れたことに気づいて戻る
1. 居室で鍵を探し、また遠い部屋に行く
1. 違う鍵を持ってきたことに気づき、居室に戻る
1. 居室で鍵を探したら、さっき持っていいた鍵が正しい鍵であることがわかる。

今日はもう駄目だ。多分何してもミスる。
