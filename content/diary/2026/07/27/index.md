---
title: "2026年7月27日"
date: 2026-07-27T00:00:00+09:00
lastmod: 2026-07-27T00:00:00+09:00
type: diary
source_month: "d202607.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

数理物理の期末テスト。

その後、採点。18:00くらいからはじめて、採点が終わったのが20:45。マジか。途中休み休みやっていたとは言え、3時間弱かかるのか。90名弱に3時間。1時間で30枚と考えると、1枚2分。いや、これがんばったほうだな。うん。

MN-Core SDKを試す。まずは[Getting Started](https://dev.mn-core.com/getting-started/)から。

```sh
$ bash create_dev_ctr.sh -A
command not found readarray
```

うげ。なんか動かない。調べたら、readarrayは新しめのbashの組み込みだそうな。手元のbashのバージョンは3。古すぎ。homebrewで入れ直す。

```sh
$ bash create_dev_ctr.sh -A
Enumerating devices
find: /dev/fd/3: Not a directory
find: /dev/fd/4: Not a directory
find: /dev/fd/6: Not a directory
[WARN] No MN-Core device found. You can use emulator backend only
Starting container
docker: Error response from daemon: mounts denied: 
The path /opt/mncore_shared_semaphore is not shared from the host and is not known to Docker.
You can configure shared paths from Docker -> Preferences... -> Resources -> File Sharing.
See https://docs.docker.com/go/mac-file-sharing/ for more info.

Run 'docker run --help' for more information
```

なんかマウントに失敗したな。ここで時間切れ。後で詳細を確認。
