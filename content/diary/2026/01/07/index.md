---
title: "2026年1月7日"
date: 2026-01-07T00:00:00+09:00
lastmod: 2026-01-07T00:00:00+09:00
type: diary
source_month: "d202601.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

採点した実験レポートを提出。これで一段落。

あ、来週の研究室ミーティング、会議とぶつかっている。予定を調節しなければ・・・

あまりに集中力がなくて、机の上の整理とかはじめちゃった。

ガイダンスの準備。

* [渡辺研Slackの使い方](https://speakerdeck.com/kaityo256/slack-local-rule)の内容を更新した。
* esaはURLで共有することにする。
* 研究室Google Calendarの招待メール送った。

研究室ガイダンス。居室の紹介とナンバーキーの使い方の説明を忘れてた。esaの「新メンバーにやることリスト」を追加。

時間厳守の、しかもまぁまぁ作業量が多い依頼が締め切りの42時間前に送られてくるってのはどうなのか？

Todoistに2ヶ月近く塩漬けになっていた、Zennのタイポを修正。単に「zennの頂点の座標が間違ってる」としか書いておらず、どこがミスになっているかを探すのに少し時間がかかった。すぐにやらないと駄目だな。

2023年4月openのissueを閉じた。3年・・・。

重い腰をついにあげてWordPressの移行準備。とりあえずwp-contentのダウンロードとmysql(MariaDB)のダンプの取得。

```sh
mysqldump -u root -p wordpress > wordpress.sql 
```

うぅ、wp-contentが5GBあるので、Git管理は無理。NASにバックアップして、.gitignoreして、Dockerで表示確認とかだな。でも、これで最低限、サーバが死んでも復活可能のはず・・・？(Dockerで見てみないとわからないが)。

また査読みたいな奴の対応。まずは準備。

Boxのバックアップ確認。たぶん大丈夫かな。多分いらないけど、念の為いくつかダウンロードしておいた。
