---
title: "2025年4月16日"
date: 2025-04-16T00:00:00+09:00
lastmod: 2025-04-16T00:00:00+09:00
type: diary
source_month: "d202504.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Markdown→Re:VIEW→LaTeXでうまく動かない奴。`\left|`と`\right|`のせいだった。Re:VIEWの文中数式が`@<m>|hoge|`と、縦棒をデリミタとして使っているため。とりあえず文中の`\left|`、`\right|`を`\lvert`、`\rvert`にすることで対応。

rcloneをWSLにインストール。

```sh
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

実行に数分かかる。ダウンロード後に表示が止まるので不安になる。しばらくまって以下の様な表示が出たらOK。

```txt
rclone v1.69.1 has successfully installed.
Now run "rclone config" for setup. Check https://rclone.org/docs/ for more details.
```

FUSE(Filesystem in Userspace)が必要だが、WSL2にはデフォルトで入っている模様。

設定は`rclone config`で対話的にもできるが、非常に冗長なので、コマンドラインから一気にやるのが楽。

```sh
rclone config create server-name sftp host=hostname shell_type=unix
```

`servername`が今後使う名前。`hostname`がsshのホスト名。

これにより、`.config/rclone/rclone.conf`に必要な情報が書き込まれる。この後、

```sh
rclone ls server-name: --max-depth=1
```

で`ls`が通ったら成功。

WSL2でのマウントには「fusermount3」が必要。

```sh
sudo apt update
sudo apt install fuse3
```

```sh
which fusermount3
```

を実行し、`/usr/bin/fusermount3`と表示されればOK。

この状態で`server-name:temp`を`~temp`にデーモンモードでマウントするには、

```sh
rclone mount server-name:temp ~/temp --vfs-cache-mode writes --daemon
```

とすればOK。unmountは、

```sh
sudo umount temp
```

とする。エディタで開いた状態のままだと

```sh
umount: /home/watanabe/temp: target is busy.
```

などと言われるので、VSCodeを閉じてから`sudo umount temp`をやりなおす。

```sh
rclone config create server-name sftp host=hostname
rclone config update server-name user=watanabe
```

と二行に分けた方が分かりやすいな。

物性研を試す。

```sh
rclone config create ohtaka sftp host=ohtaka.issp.u-tokyo.ac.jp
rclone config update ohtaka user=k0xxxxx
rclone ls ohtaka: --max-depth=1 
mkdir ohtaka
rclone mount ohtaka: ~/ohtaka --vfs-cache-mode writes --daemon
```

`code .`はできないが、「フォルダーを開く」はいける。

```sh
rclone config create kugui sftp host=kugui.issp.u-tokyo.ac.jp
rclone config update kugui user=k0xxxxx
rclone ls kugui: --max-depth=1 
mkdir kugui
rclone mount kugui: ~/kugui --vfs-cache-mode writes --daemon
```

こっちもいけた。これで行こう。

Macにもインストール。

```sh
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

パスワード入力後、以下のような画面が出てしばらく止まる。

```txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  4734  100  4734    0     0   5010      0 --:--:-- --:--:-- --:--:--  5009
```

しばらく待って

```txt
rclone v1.69.1 has successfully installed.
Now run "rclone config" for setup. Check https://rclone.org/docs/ for more details.
```

と出ればOK。

次にmacFUSEのインストール。

[macfuseのサイト](https://macfuse.github.io/)に行ってdmgをダウンロード。
macFUSE 4.10.1をダウンロード。「Install macFUSE」をダブルクリックしてインストール。

「機能拡張がブロックされました」という表示が出るので「システム設定を開く」をクリック。

「プライバシーとセキュリティ」の画面で「開発元"Benjamin Fleischer"のシステムソフトウェアの読み込みがブロックされました。」というメッセージの下の「許可」ボタンを押す。再起動を求められるので再起動する。

一度`ssh ohtaka`でパスワードなしでログインできること(ssh-agentが起動して、秘密鍵を覚えていること)を確認する。

```sh
rclone ls ohtaka: --max-depth=1 
```

成功。

```sh
mkdir ohtaka
rclone mount ohtaka: ~/ohtaka --vfs-cache-mode writes --daemon
```

これでWindows, Mac両方ともrcloneでスパコンサイトをローカルマウントできた。

解析力学の著者校正返した。

今日、会議x4の合間に、cloneのWindows/Macの動作確認した上に250ページ近い本の著者校正返したの偉すぎない？
