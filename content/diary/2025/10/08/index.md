---
title: "2025年10月8日"
date: 2025-10-08T00:00:00+09:00
lastmod: 2025-10-08T00:00:00+09:00
type: diary
source_month: "d202510.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

会議。

来年度に向けて、博士号取得のスケジュール確認をするなどした。

[デロイトがオーストラリア連邦政府から受託した報告書をAIを使って書いたのがバレて返金](https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report)

存在しない参考文献でバレたとのこと。デロイトは「報告内容には変更はない」と言っているけれど、「主要な部分もAIで書いたのでは？」と思われるよね・・・

研究室ミーティング。シアシックニングと格闘ゲームの強化学習。今日から本格的に英語での発表です。

NIS共有の設定続き。うまくNIS共有できなかったのはサーバ側のポートが閉じていたから。

サーバ側で

```sh
sudo firewall-cmd --permanent --add-port=861/tcp
sudo firewall-cmd --permanent --add-port=861/udp
sudo firewall-cmd --permanent --add-port=111/tcp
sudo firewall-cmd --permanent --add-port=111/udp
sudo firewall-cmd --reload
```

を実行することでポートが通った。

クライアント側で

```sh
sudo /usr/sbin/ypbind -d
```

を実行することでどこでこけているかがわかる。ypwhichやgetentが通るようになった時点で

```sh
sudo systemctl start ypbind
```

で通った。

クライアントでypbindが自動起動するか確認。

```sh
$ sudo systemctl is-enabled ypbind
enabled
```

大丈夫ですね。

Slurmのインストール途中で時間切れ。

ノーベル化学賞が日本人受賞でバタバタ・・・
