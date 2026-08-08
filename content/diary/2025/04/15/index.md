---
title: "2025年4月15日"
date: 2025-04-15T00:00:00+09:00
lastmod: 2025-04-15T00:00:00+09:00
type: diary
source_month: "d202504.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

sshfsの代替、rcloneが良いらしい。ただし、[Homebrewでいれられるrcloneはmountに非対応](https://github.com/rclone/rclone/issues/5373)。うーむ。

どうもrcloneがmacFUSEに依存しており、それをHomebrewが嫌っているから、らしい。

いやしかし、sshfsはなぜ開発終了したのかをChatGPTに聞いたらしれっと嘘をついてきた(開発者がこう行っています→ソースは？→ソースはありませんでした)。昔は正しいことを言ってきたら驚いたが、今は明らかな嘘をついたら驚くようになったな。進歩が早い。
