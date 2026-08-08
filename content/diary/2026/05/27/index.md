---
title: "2026年5月27日"
date: 2026-05-27T00:00:00+09:00
lastmod: 2026-05-27T00:00:00+09:00
type: diary
source_month: "d202605.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

学会のパンフレット関連でQRコードがほしかったのだが、ウェブで見つかる無料のQRコード生成サイトがいろいろひどい。すぐに全画面広告が出てくるのはまだ良いとして、QRコードを生成したら、まずそのサイトに一瞬飛んでからリダイレクトで目的のサイトに飛ぶという、かなりevilなサイトがあったので自作した。

[QRコード生成](https://kaityo256.github.io/qr-code-generator/)

で、これを作るためにChatGPTやCodexといろいろ対話したので、その記録も残しておいた。

[AIエージェントを使ってQRコード生成ページを作る](https://kaityo256.github.io/qr-generator-with-ai-agent)

おそらくこのようなコードの書き方もすぐにobsoleteになるのであろう。その記憶として。

どうでも良いが、QRコードを作成したら短縮URLを作って、一度そのサイトに飛んでからリダイレクトさせるevilなサイト、いま探したら見つからないな。Google BANされたか？それとも僕の勘違いだったのだろうか？

ついでにfaviconも作った。

```sh
magick robo.png -resize 32x32 favicon-32x32.png
magick robo.png -resize 16x16 favicon-16x16.png
magick robo.png -resize 180x180 apple-touch-icon.png
magick robo.png -define icon:auto-resize=16,32,48 favicon.ico
```

学生さん論文その1のカバーレターも作った。

[APS Open Science](https://journals.aps.org/apsos/)というジャーナルがLaunchされたらしい。2026年からのオープンアクセス誌。High Impact追求ではなく、科学的に妥当なら掲載する、というスタンス。どこかで見たな。

しばらく前に査読した論文の、もう一人の査読者の査読レポートをようやく真面目に読んだ。自分がかなり厳しいレポートを書いたのに、もう一人はポジティブだった、みたいに日記に書いたのだが、もう一人の査読者も(口調が柔らかいだけで)かなり厳しかった。まぁそうだよな。少し安心。

作業量的に重いタスクを1つ、気分的に重いタスクを1つ片付けた。だいぶ軽くなってきたぞ。

シミュレーション工学のレポートを公開。

数理物理のモジュール公開。
