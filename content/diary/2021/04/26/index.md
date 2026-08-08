---
title: "2021年4月26日"
date: 2021-04-26T00:00:00+09:00
lastmod: 2021-04-26T00:00:00+09:00
type: diary
source_month: "d202104.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

いろいろ気合いれてメールする。

今週から学生さんとの1on1ミーティングが始まった。オンラインは便利ではあるが、こういうのは対面でやりたいよなぁ。

柔道部の会長面談。公認の承認。

物理情報工学特別講義のレポート採点した。採点手順もまとめた。

企業との共同研究、参考にしようと思って積極的に共同研究している研究室のページ(他大)を見たんだけど、こんなに強気なの？って価格設定でびっくりした。

学内ESETライセンス申請した。

Linuxマシン、DHCPクライアントがIPアドレスをもらえない。

```sh
sudo dhclient -r
sudo dhclient
```

ダメだ、ダメだとやっていたが、問題は単にケーブルを間違ったところに指していたからだった。アホすぎだろ。

物理情報工学講義のムービー低画質版作成。AMD EPYCマシンはアップデートに時間がかかって間に合わず。アップデート前に試すべきだった。

```sh
time ffmpeg -i aiyoshi02.mp4 -crf 24 aiyoshi02_low.mp4
```

講義編集してアップロードした。後でチェックして公開。

僕は自己肯定感が強い方だと思うけれど、それでもたまに「この人なんでこんなに自信があるんだろう」と思う人を結構見かけるなぁ。自信があるのは良いことだと思うけど、なんというか、「自分は(いろんな意味で)重要人物である」という認識が強い。例えば「他の人にとって、自分が重要な人物だと思われている」ということを前提にした言動であるとか。

SNSとかで反応されているうちにそういう認識にいたるのかな。SNSでなにかいうと、基本的には「そのとおり！」「よく言ってくれた」「さすが先生」みたいな反応があるので、それで勘違いするとか。もちろん批判的な意見も来るけど、それは「反論」で潰してるように見える。

ミネソタの件、研究室のPIから[お詫びメール](https://lore.kernel.org/lkml/CAK8KejpUVLxmqp026JY7x5GzHU2YJLPU8SzTZUNXU2OXC70ZQQ@mail.gmail.com/)が飛んでる。Gregはほぼ完全にスルー。

「Fella」という単語を知った。「Fellow」の砕けた言い方で、「みんな」「奴」みたいな言葉。「Hey Guys」「You guys」のguyみたいな使い方をする。例のミネソタの論文の[Joke PR](https://github.com/QiushiWu/qiushiwu.github.io/pull/6)で見つけた。興味深いので[引用](https://github.com/QiushiWu/qiushiwu.github.io/pull/6#issuecomment-824785220)。

> Fellas, you are reading too much into a joke PR. The paper would have been a great venture into OSS vulnerabilities. **had it not been in the stable branch of the largest OS in the world that billions of people rely on.** Obviously the insights gained are very interesting and I would have liked if it had taken place legitimately w/o wasting days of volunteer time to look at patches and afterwards reverse the damage.

げ、zenn-contentをgit fetch;mergeしたら、package-lock.jsonがconflictした。これ、適当にやるとまずそうなので、ちゃんと理解してから触ることにする。とりあえずは明日に延期。


NOP

朝早く娘に起こされたので、その時間でZennに記事書いた。[ルジャンドル変換と双対の話](https://zenn.dev/kaityo256/articles/legendre_dual)。一ヶ月くらい前の輪講の余談だったかな。

クレジットカード会社から連絡。カードの不正利用の疑いがあり、確認したかったとのこと。以前、家族カードの情報が漏れたという連絡があったが、それが悪用されたらしい。最初にカードが有効か確認の登録があり、その後モバイルＳｕｉｃａで換金したらしい。心当たりがないとのことで、カードは即時停止、モバイルＳｕｉｃａの分は保証してくれるとのこと。対応が早くて助かった。そんなことがあるんですね。
