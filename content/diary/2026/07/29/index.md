---
title: "2026年7月29日"
date: 2026-07-29T00:00:00+09:00
lastmod: 2026-07-29T00:00:00+09:00
type: diary
source_month: "d202607.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

追試作った。当たり前だが、本試験と同じくらい時間がかかる。

打ち合わせしたりとか。

ネットで「望まれていないアドバイス」が話題になっていた。人命にかかわるようなことならともかく、単に趣味で「こんなの作ったよ〜」というものに「専門家」から「これはこうすべき」みたいなのが飛んできたらまぁイヤになるよな・・・

数理物理の成績(OCR結果)を確認。思ったより成績が良くて安心。

充電器を注文した。

慶應が契約しているNotion、ようやくログインした。早速事務処理について質問したが、なかなか良さそう。

RBMのKLダイバージェンスの計算方法を修正。

Pythonのリンター、Ruffがおすすめということで入れる。

```sh
brew install ruff
```

VSCodeでRuff拡張機能をインストール。そのうえで以下をsettings.jsonに追加。

```json
    "[python]": {
        "editor.formatOnType": true,
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": true
    },
    // Ruffを有効化
    "ruff.nativeServer": "on",
```

動作が早くていい感じ。

なんか物性研でもuvが問題なく動いたので、READMEで`uv`を使う例も追加。来年のPythonについては`uv`メインで仮想環境構築ハンズオン作るか。

久しぶりに研究っぽいことをした。論文までたどり着けていないが。

いやしかし、AI使うようになると変数名とか関数名とかコミットメッセージとか考えなくて良くなるのは楽だよな。
