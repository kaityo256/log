---
title: "2022年12月7日"
date: 2022-12-07T00:00:00+09:00
lastmod: 2022-12-07T00:00:00+09:00
type: diary
source_month: "d202212.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

在宅勤務。会議とか。

```sh
$ python3 -m pip install tensorflow
ERROR: Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
```

ん？

```sh
$ python3 -m pip uninstall pyyaml
Found existing installation: PyYAML 3.13
ERROR: Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
```

調べたら、これはcondaのせいだった。

```sh
conda uninstall pyyaml
```
