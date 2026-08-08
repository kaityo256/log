---
title: "2025年11月20日"
date: 2025-11-20T00:00:00+09:00
lastmod: 2025-11-20T00:00:00+09:00
type: diary
source_month: "d202511.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

D論予備審査。

Cloudflareの障害の詳細が出ている。

[Cloudflare outage on November 18, 2025](https://blog.cloudflare.com/18-november-2025-outage/)

個人的にはこちらがわかりやすかった。

[Understanding the Cloudflare Outage: A Simple Explanation](https://medium.com/%40ajaygohil2563/understanding-the-cloudflare-outage-a-simple-explanation-be7b88f7d339)

GitLabのデータベースふっとばし事件を思い出した。

[GitLab.com database incident](https://about.gitlab.com/blog/gitlab-dot-com-database-incident/)

簡単なまとめ

* Cloudflareがセキュリティ対応のためデータベース権限を変更。これまでユーザから見えなかったデータベースが見えるようなった。
* しかし、クエリにデータベースの指定文を追加し忘れる
* 同じクエリに対して、複数のデータベースが答えを返し、結果が重複。Bot判定のための特徴量に関する情報が増えてしまう
* Bot判定(アクセスの人間らしさのスコア付与)は機械学習でやっていたが、その入力特徴量の上限を超えてしまい、エラーを返す
* Bot判定がエラーを返すことが想定されておらず、コアプロキシが5xxを返す
* 多くのサービスがコアプロキシに依存していたため、ドミノ倒し的に全滅

D論印刷してたらトナーが切れた。注文した。

* OKI 沖電気 トナーカートリッジ TC-C4E1 カラー４色セット (TC-C4EK1/C4EC1/C4EM1/C4EY1)

あと、ケースファイルも足りなかったので注文。

* コクヨ ファイル ケースファイル A4 3冊入り 緑 フ-950NG

論文の査読対応。すごく頑張ったがReviewer 2の返事まで。明日3の対応をする・・・時間あるかなぁ。

レポートの採点もあるんだけど、どうすんべ。

家に帰ってから歯を食いしばって査読対応完了させた。

論文は書くものじゃない。通すものだ。


プログラミング基礎同演習。部屋に戻ってから講義室にACアダプター忘れたことに気づく orz

しまった、来週は三田祭で講義休みだ。講義あるって言っちゃった。
大学院の講義カレンダーを見てて、「休みだけど講義あるよ」というマークがあるのを見てすっかりあると思ってた。学部は講義ないんだ。
あわててアナウンスする。

1on1の後、論文直したかったけど、ACアダプター取りに日吉へ。もうPC室が閉まってて入れなかった orz
