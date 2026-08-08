---
title: "2024年3月15日"
date: 2024-03-15T00:00:00+09:00
lastmod: 2024-03-15T00:00:00+09:00
type: diary
source_month: "d202403.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Pythonのパッケージを作ってGitHubで公開する方法を確認した。

NumpyとCupyの共存。

```py
try:
    import cupy as np
    has_GPU = True
except ImportError:
    import numpy as np
    has_GPU = False
```

共通命令しか使っていなければこれでいけるはず。
