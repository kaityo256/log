---
title: "2024年12月24日"
date: 2024-12-24T00:00:00+09:00
lastmod: 2024-12-24T00:00:00+09:00
type: diary
source_month: "d202412.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

```sh
npm install -g npm@11.0.0
npm error code EBADENGINE
npm error engine Unsupported engine
npm error engine Not compatible with your version of node/npm: npm@11.0.0
npm error notsup Not compatible with your version of node/npm: npm@11.0.0
npm error notsup Required: {"node":"^20.17.0 || >=22.9.0"}
npm error notsup Actual:   {"npm":"10.8.3","node":"v20.9.0"}
```

ありゃ。

```sh
$ nvm install node
$ node -v 
v23.5.0
$ npm install -g npm@latest
```

自分がbrewではなくnvm使ってたのを忘れてた。
