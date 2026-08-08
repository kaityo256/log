---
title: "2023年10月20日"
date: 2023-10-20T00:00:00+09:00
lastmod: 2023-10-20T00:00:00+09:00
type: diary
source_month: "d202310.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

体がめちゃくちゃ重い。ひたすら寝ていた。

重い仕事を済ませた。


1on1 x 4

メール処理。

GitHub演習。

物理情報工学ソフトウェア開発演習レポート、第三回まで完了。

年末調整。多分できた。

金融機関から送られてくる残高証明書の他に、税務署からの申請書が必要で、それは電子データでの送付を希望したので「令和X年分住宅借入金等特別控除証明書_yymmdd.xml」というファイルをe-taxからダウンロード、簡単年調でアップロードすることで完了。ふぅ。

昨年は自分で確定申告したのだが、おそらく特別控除証明書はe-taxの連携で自動で確認してくれたのだろう。やれやれだ。

来年まで覚えている自信がない。

nodeのバージョンが古い?

```sh
$ sudo npm install -g npm@10.2.1
npm ERR! code EBADENGINE
npm ERR! engine Unsupported engine
npm ERR! engine Not compatible with your version of node/npm: npm@10.2.1
npm ERR! notsup Not compatible with your version of node/npm: npm@10.2.1
npm ERR! notsup Required: {"node":"^18.17.0 || >=20.5.0"}
npm ERR! notsup Actual:   {"npm":"8.13.2","node":"v14.15.4"}
```

```sh
sudo npm install n -g 
sudo n stable  
sudo apt purge -y nodejs npm
```
