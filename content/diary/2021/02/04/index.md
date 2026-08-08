---
title: "2021年2月4日"
date: 2021-02-04T00:00:00+09:00
lastmod: 2021-02-04T00:00:00+09:00
type: diary
source_month: "d202102.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

いい加減ここの日付を書くのに手書きはアホ過ぎるのでスニペットを作ろう。まず、ローカル設定にしたいので、ローカルの.vscodeに作る。以下の内容で`.vscode/md.code-snippets`を作った。

```json
{
  "Print to console": {
    "scope": "markdown, md",
    "prefix": "date",
    "body": [
      "## [$CURRENT_MONTH月$CURRENT_DATE日($CURRENT_DAY_NAME_SHORT)](#$CURRENT_DATE) <a id=\"$CURRENT_DATE\"></a>",
      "$2"
    ],
    "description": "diary header"
  }
}
```

また、デフォルトではMarkdownでスニペット呼び出しができないので、`.vscode/settings.json`に以下を追加。

```json
{
  "[markdown]": {
    "editor.quickSuggestions": true
  },
}
```

これで「date(タブ)」と入力すると`## [02月04日(Thu)](#04) <a id="04"></a>`みたいな文字列が出てくるようになった。「木」ではなく「Thu」が出てしまったりするが、まぁ良いことにしよう。dateで出るのが鬱陶しくなったらprefix変えよう。

Macでなぜかnpmが動かない。

```sh
$ npm init --yes
dyld: Library not loaded: /usr/local/opt/icu4c/lib/libicui18n.64.dylib
  Referenced from: /usr/local/bin/node
  Reason: image not found
zsh: abort      npm init --yes
```

最近これ系(ダイナミックリンクライブラリがらみ)のエラー多いな。

```sh
$ brew install npm
(snip)
Error: node 12.9.1 is already installed
To upgrade to 15.8.0, run:
  brew upgrade node
```

ほほう。

```sh
$  brew upgrade node
==> Upgrading 1 outdated package:
node 12.9.1 -> 15.8.0
==> Upgrading node 12.9.1 -> 15.8.0 
==> Downloading https://homebrew.bintray.com/bottles/node-15.8.0.big_sur.bottle.
Already downloaded: /Users/watanabe/Library/Caches/Homebrew/downloads/9bf57615654f850ea19d76c53dee4b63bc00f11a242813b95b8450e45942a12b--node-15.8.0.big_sur.bottle.tar.gz
==> Pouring node-15.8.0.big_sur.bottle.tar.gz
🍺  /usr/local/Cellar/node/15.8.0: 3,336 files, 55.9MB
Removing: /usr/local/Cellar/node/12.9.1... (4,629 files, 53.4MB)
```

できたかな？

```sh
$ npm
(snip)
npm notice 
npm notice New patch version of npm available! 7.5.0 -> 7.5.2
npm notice Changelog: https://github.com/npm/cli/releases/tag/v7.5.2
npm notice Run npm install -g npm@7.5.2 to update!
npm notice 
```

ふむ。

```sh
npm install -g npm@7.5.2
```

もう一度。

```sh
npm install zenn-cli 
```

無事に通った。

```sh
$ npx zenn preview
👀Preview on http://localhost:8000
```

これで`http://localhost:8000`を見たらちゃんと見えた。よしよし。

ついでにhttpサーバの確認。

```sh
$ telnet localhost 8000
Trying ::1...
Connected to localhost.
Escape character is '^]'.
HEAD / HTTP/1.0

HTTP/1.1 200 OK
X-Powered-By: Next.js
ETag: "159e-WBZEF7rtwOl9mxryAKtsz2EiX+8"
Content-Type: text/html; charset=utf-8
Content-Length: 5534
Cache-Control: private, no-cache, no-store, max-age=0, must-revalidate
Vary: Accept-Encoding
Date: Thu, 04 Feb 2021 04:12:16 GMT
Connection: close

Connection closed by foreign host.
```

`Next.js`で動いているみたいですね。しかし、最近の若人はこういうの、何で調べてるんだろ？

WSL2でapt-get updateができない問題、日付がずれているのが原因だった。

```sh
date
2021年　1月 30日 土曜日 04:03:43 JST
```

なんでやねん。

```sh
sudo hwclock -s
```

で治った。これでnpmやzenn-cliを入れたところ、WLS2でnpx zenn previewが通った。全部WSL2の日付の問題であったらしい。
