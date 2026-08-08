---
title: "2021年5月18日"
date: 2021-05-18T00:00:00+09:00
lastmod: 2021-05-18T00:00:00+09:00
type: diary
source_month: "d202105.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

WSL2をすべてアップデートしたら学校のマシンでもできた。Macだとディスクイメージが作れないっぽい。WSL2で作ったイメージをロードしたらできた。あとでディスクユーティリティで

```sh
mkdir -p /Volumes/MIKAN\ OS/EFI/BOOT
cp BOOTX64.EFI /Volumes/MIKAN\ OS/EFI/BOOT
diskutil unmount /Volumes/MIKAN\ OS
```

としてアンマウントすると中身がおかしくなる？Finderからアンマウントすると大丈夫。どういうこっちゃ？

あと、dosfstoolsを入れたあと、`mkfs.fat`にデフォルトでパスが通らないの、なぜなんだぜ？
