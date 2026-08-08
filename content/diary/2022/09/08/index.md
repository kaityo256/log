---
title: "2022年9月8日"
date: 2022-09-08T00:00:00+09:00
lastmod: 2022-09-08T00:00:00+09:00
type: diary
source_month: "d202209.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室ミーティング。

4:15分にiMacの修理が終わったというメールを見て生協にかけつけたが、4時で営業終了だった。

zshのヒストリが壊れた。

```txt
zsh: corrupt history file /home/username/.zsh_history
```

みたいなことを言われる。原因は`.zsh_history`におかしな文字列が含まれているため。`string`コマンドで修理できるらしいが、`vim`で直接なおした。

gitもおかしくなってる。

```sh
$ git log
error: object file .git/objects/55/72ef2d220b5f3a2142c7c09e057c2e95b69873 is empty
error: object file .git/objects/55/72ef2d220b5f3a2142c7c09e057c2e95b69873 is empty
fatal: loose object 5572ef2d220b5f3a2142c7c09e057c2e95b69873 (stored in .git/objects/55/72ef2d220b5f3a2142c7c09e057c2e95b69873) is corrupt
error: object file .git/objects/55/72ef2d220b5f3a2142c7c09e057c2e95b69873 is empty
error: object file .git/objects/55/72ef2d220b5f3a2142c7c09e057c2e95b69873 is empty
fatal: loose object 5572ef2d220b5f3a2142c7c09e057c2e95b69873 (stored in .git/objects/55/72ef2d220b5f3a2142c7c09e057c2e95b69873) is corrupt
```

どうもコミット時にファイルが壊れたっぽい。`.zsh_history`といい`git`といい、なんかファイルがおかしい。ハードディスクが不調なのか？怖すぎる。
