---
title: "2023年9月26日"
date: 2023-09-26T00:00:00+09:00
lastmod: 2023-09-26T00:00:00+09:00
type: diary
source_month: "d202309.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

講義準備。K-LMSにページを作ったり、ファイルをアップロードしたり。

なんかK-LMS、コピペすると二重に貼り付けられてしまったり、モジュール名を変えようとすると変換が極めて遅くなったり(ブラウザ側で予測変換している？)して、地味にストレス。

K-LMSに貼り付けをして、二重に貼り付けられた場合、すぐにCtrl+zを押すと一つキャンセルできる。

レポート課題提出ページとオンデマンド動画ページを14回分作るのにものすごい時間かかった。一つ作って、ページ一覧で重複して修正していくと少しはマシだが。

プログラミング基礎同演習のページ作った。2時間かかった。

ついでに反応拡散方程式の回でFitzHugh-Nagumoをやろうとしたが、なんかうまくいかない。前回、パラメータは以下の論文を参照したようだが。

* [A. Hagberg and E. Meron, Phys. Rev. Lett. vol. 72, pp. 2494 (1994)](https://doi.org/10.1103/PhysRevLett.72.2494)

昔の日記、リファレンスが間違ってた。研究者の風上にもおけない。

研究室ウェブサーバのSSL証明書の有効期限確認。

```sh
$ echo | openssl s_client -connect calc.appi.keio.ac.jp:443 2>/dev/null | openssl x509 -noout -dates 
notBefore=Sep  8 18:02:28 2023 GMT
notAfter=Dec  7 18:02:27 2023 GMT
```

9月8日から12月7日まで有効と。Let's Encryptだと有効期限3ヶ月なのか。

```sh
$ echo | openssl s_client -connect www.google.com:443 2>/dev/null | openssl x509 -noout -dates
notBefore=Jan  1 00:00:00 2015 GMT
notAfter=Jan  1 00:00:00 2030 GMT
```

Googleは15年有効と。

こんなの、ChatGPTがすぐ答えてくれるんだもんなぁ。すごい時代だ。

重い腰をあげて研究室の電話交換、及び酸素濃度計の撤去の手配をした・・・ら、すぐに施設の人が来てくれた。仕事が超早い。

明日の会議の準備。

今日の会議の準備。
