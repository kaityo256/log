---
title: "2024年12月10日"
date: 2024-12-10T00:00:00+09:00
lastmod: 2024-12-10T00:00:00+09:00
type: diary
source_month: "d202412.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

令和の時代にプリンターのセットアップに1時間以上かかった。これはOKIのUIも悪い。

まず、USBを刺しても自動認識しない。OKIの設定アプリからじゃないと認識しない。USB認識時の音もならないから、ケーブルが死んでるかと思って違うケーブルを探しにいってしまった。

あと、プリンターのセットアップアプリが、ユーザの入力待ちになっているのに「推定、あと15分」というプログレスバーがアニメーションしているため、こちらがアクションしなければならない状態であることに気が付かなかった。

もっと言えば、セットアップアプリ系はモーダルにして手前に表示しないとだめでしょう。起動時にエディタの後ろに隠れてどこにあるかわからなかった。

いつの間にかWSLのopenコマンドが使えなくなった。cmd.exeからUbuntu上のファイルが開けなくなったようだ。結局全部explorer.exeにした。

```sh
function open() {
    if [ $# != 1 ]; then
        explorer.exe .
    else
        if [ -e $1 ]; then
            explorer.exe $(wslpath -w $1) 2> /dev/null
        else
            echo "open: $1 : No such file or directory" 
        fi
    fi
}
```
