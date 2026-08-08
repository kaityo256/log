---
title: "2025年6月17日"
date: 2025-06-17T00:00:00+09:00
lastmod: 2025-06-17T00:00:00+09:00
type: diary
source_month: "d202506.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

木曜日のスライドを作る。

授業準備も。


latexindentが死んでる。

```sh
$ latexindent -vv
Attempt to call undefined import method with arguments ("@logFileLines") via package "LatexIndent::Logger" (Perhaps you forgot to load the package?) at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 28.
Attempt to call undefined import method with arguments ("$ifElseFiBasicRegExp") via package "LatexIndent::IfElseFi" (Perhaps you forgot to load the package?) at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Special.pm line 25.
```

なんかChatGPTが「TeXLiveは毎年更新」という恐ろしいことを言ってるんだけど。

TexLiveの最新版をインストール。

```sh
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar xvzf install-tl-unx.tar.gz
cd install-tl-20250616
sudo ./install-tl --no-interaction
```

パスが更新されなかった。

```sh
sudo /usr/local/texlive/2025/bin/universal-darwin/tlmgr path add 
```

```sh
$ ls -la /usr/local/bin/latex
lrwxr-xr-x  1 root  admin  50  6 17 19:48 /usr/local/bin/latex@ -> /usr/local/texlive/2025/bin/universal-darwin/latex
```

された。

```sh
$ latexindent -v 
3.24.5, 2025-03-13
```

latexindentも直った。でもVSCodeのlatexindentが.latexindent/defaultSettings.yamlを読んでくれない。

輪講。今日はネーターの定理。ネーターの定理ってハミルトン形式でやったほうが楽だと思うんだけど、この本は徹底的にラグランジアンで議論しているっぽいな。
