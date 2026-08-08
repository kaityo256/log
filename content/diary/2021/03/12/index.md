---
title: "2021年3月12日"
date: 2021-03-12T00:00:00+09:00
lastmod: 2021-03-12T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

論文の図の修正。共著者さんの結果を自分の結果に入れ替え。ものすごく時間かかったぞ。

追加計算用コードを書いてスパコンに投げた。cos(4π/3)の符号を間違えていたせいでしばらく混乱していた。ひどいもんだ。

WSL2でtmuxを使うと激重になるの、Windowsのパスが通っているせいだったらしい。[ここ](https://amaya382.hatenablog.jp/entry/2019/12/27/120057)の記述にしたがって`/etc/wsl.conf`に

```txt
[interop]
appendWindowsPath = false
```

と書いてログインしなおせばかなり早くなる。ただし、当然のことながらWindowsから引き継いだパスに由来するコードが使えなくなるので、自分で設定するかシンボリックリンクが必要。特に`code`が使えなくなるのが面倒。他にも副作用がありそうなので、とりあえず元に戻した。tmuxはしばらくあきらめよう。

tmuxとの関連は不明だが、なんかシェルが死んで、WSLを再起動したら

```sh
zsh: corrupt history file /home/myusername/.zsh_history
```

とか言われてzshが動かなくなった。[ここ](https://superuser.com/questions/957913/how-to-fix-and-recover-a-corrupt-history-file-in-zsh)の記述の通り、

```sh
mv .zsh_history .zsh_history_bad
strings .zsh_history_bad > .zsh_history
```

で解決。
