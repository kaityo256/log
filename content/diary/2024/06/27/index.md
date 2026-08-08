---
title: "2024年6月27日"
date: 2024-06-27T00:00:00+09:00
lastmod: 2024-06-27T00:00:00+09:00
type: diary
source_month: "d202406.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

数理物理中間テスト代替。来年はやらない予定。

VSCodeのDraw.ioがpdfを吐けないことの対応。

いちいち

```sh
draw.io -xf pdf -o filename.pdf filename.drawio
```

と入力したくない。

> 「d2pdf filename.drawio」
> と入力したら
> 「draw.io -xf pdf -o filename.pdf filename.drawio」
> と展開されるbash aliasもしくは関数を定義してください。

というわけでできたのがこちら。

```sh
d2pdf() {
    local input_file="$1"
    local output_file="${input_file%.drawio}.pdf"
    draw.io -xf pdf -o "$output_file" "$input_file"
}
```

こういう作業はChatGPTの方が圧倒的に速い。

WSLのUbuntuにも入れたいが、snapdがないためインストールできない。一応回避策はあるが、どうするかな。

輪講。

研究室ミーティング。

とても重い(研究とは全く関係ない)仕事をようやくひとつ片付けた。

最近、外に出せない仕事ばかりでしんどい。
