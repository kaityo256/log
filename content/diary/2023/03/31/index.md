---
title: "2023年3月31日"
date: 2023-03-31T00:00:00+09:00
lastmod: 2023-03-31T00:00:00+09:00
type: diary
source_month: "d202303.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

3月が終わってしまう。

朝、カラスがミスタードーナツのハニーディップと思しきドーナツ(無傷)をくわえてた。大物を捕まえましたね。

VSCodeのスニペットの`$CURRENT_DAY_NAME_SHORT`が「金」ではなく「Fri」になってしまう問題、VSCodeを日本語化したらなおった。っていうかいつのまにかVSCodeの日本語化拡張がおかしくなってた。uninstallしてinstallして再起動したらなおった(パソコンしぐさ)。

[筑波大学を退職します（a.k.a acadexit）](https://note.com/takefumihiraki/n/nf036cd8a54a4)

筑波大学の恵まれたテニュアトラック助教の職にある若手が大学をやめる、いわゆるacadexitの話。いろいろ考えてしまう……

Subversionで、svn addした後で、commitする前にファイルを消してしまうと、「〜は追加準備状態となっていますが、存在しません」と表示されてコミットできなくなる。対応するためには、対象のファイルをrevertすれば良い。

```sh
svn revert hoge.pdf
```

なんか日本語で検索しても良い情報が得られず、わざわざ

```sh
LANG=C svn ci -m ""
```

みたいにして英語のエラーメッセージを出して、それで検索する、みたいなことをした。うーん。

懇親会費締めた。

2023年度春学期の研究室所属学生名簿提出した。

集中力を欠いた。講義準備が進まなかった。タスクも何個か落とした。厳しいなぁ。
