---
title: "2024年4月8日"
date: 2024-04-08T00:00:00+09:00
lastmod: 2024-04-08T00:00:00+09:00
type: diary
source_month: "d202404.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

sshfsのインストール。WSL

```sh
sudo apt -y update
sudo apt -y install sshfs
```

Mac。

```sh
brew install sshfs
```

マウント。

```sh
sshfs username@watanabe-login.appi.keio.ac.jp:path/to/dir ~/somedir
```

WSLでのアンマウント。

```sh
fusermount -u ~/somedir
```

Macでのアンマウント。

```sh
diskutil unmount somedir
```

なんかVSCodeのMarkdown Previewが変わってて見づらい。元に戻したい。

板書講義の録画用機材メモ。

* 人を追尾するWebカメラ(OBSBOT tinyかそれ系)
* ワイヤレスマイク（RODE wireless go + ピンマイク）

なんか普通に買うと10万以上するなぁ。これをつないでOBS Studioで録画し、編集してアップロードとか？


NOP
