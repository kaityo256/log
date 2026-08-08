---
title: "2022年3月10日"
date: 2022-03-10T00:00:00+09:00
lastmod: 2022-03-10T00:00:00+09:00
type: diary
source_month: "d202203.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Zoom API。慶応のアカウントではJWTは使えないらしい。ログイン後に「ソリューション」→「開発者プラットフォーム」を選ぶと[https://developers.zoom.us](https://developers.zoom.us)にログイン状態で飛ぶが、それだとKeio IDで入れない。謎。

ZoomのDeveloperページに飛んだら、右上の「BUILD APP」をクリック。OAuthを選んでCreate。

App Nameは適当に。app typeはよくわからないので User-managed appを選ぶ。App Marketplaceではpublishしない。で、Create。

App credentials: Client IDとClient secretを取得。Redirect URLは「<http://localhost:8080」にしてみる。OAuth> allow listはとりあえず無しでcontinue。

Scopesで、最低一つScopeを指定しないといけない。とりあえず「meeting:read」だけ指定してみる。

杉山雄規先生最終講義。Optimal Velocity Modelで、相互作用が非対称だから、エネルギーが保存しない。したがって、必ず散逸項が必要になる。OV Modelでは、「自分の希望する速度と、現在の速度の差」が加速度となるが、この「現在の速度」が散逸項の役割を果たす。なるほど。

二次元OV模型も、いろいろ遊べそうだなぁ。

サイエンスカフェの返事だした。
