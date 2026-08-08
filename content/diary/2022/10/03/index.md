---
title: "2022年10月3日"
date: 2022-10-03T00:00:00+09:00
lastmod: 2022-10-03T00:00:00+09:00
type: diary
source_month: "d202210.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

PandocのMathJaxが働かない。テンプレートの

```txt
$if(math)$
  $math$
$endif$
```

が正しくないっぽい。手動でMathJax指定したら動いたが、Pandocのバージョン上げるのが正しいよな。

```txt
pandoc 2.5
Compiled with pandoc-types 1.17.5.4, texmath 0.11.2.2, skylighting 0.7.7
Default user data directory: /home/watanabe/.pandoc
Copyright (C) 2006-2018 John MacFarlane
Web:  http://pandoc.org
This is free software; see the source for copying conditions.
There is no warranty, not even for merchantability or fitness
for a particular purpose.
```

```txt
pandoc 2.5
Compiled with pandoc-types 1.17.5.4, texmath 0.11.2.2, skylighting 0.7.7
Default user data directory: /home/watanabe/.pandoc
Copyright (C) 2006-2018 John MacFarlane
Web:  http://pandoc.org
This is free software; see the source for copying conditions.
There is no warranty, not even for merchantability or fitness
for a particular purpose.
```

apt upgradeしても変わらんな。結局直接

```html
<script type="text/javascript" id="MathJax-script" async
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
```

と書いた。
