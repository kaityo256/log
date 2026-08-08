---
title: "2025年8月5日"
date: 2025-08-05T00:00:00+09:00
lastmod: 2025-08-05T00:00:00+09:00
type: diary
source_month: "d202508.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

全く頭が回っていない。

論文を少しだけ進めた。

```sh
$ npm install -g npm@11.5.2
npm error code EBADENGINE
npm error engine Unsupported engine
npm error engine Not compatible with your version of node/npm: npm@11.5.2
npm error notsup Not compatible with your version of node/npm: npm@11.5.2
npm error notsup Required: {"node":"^20.17.0 || >=22.9.0"}
npm error notsup Actual:   {"npm":"10.9.0","node":"v20.9.0"}
npm error A complete log of this run can be found in: /home/watanabe/.npm/_logs/2025-08-05T13_33_39_019Z-debug-0.log
```

ありゃ。Node.jsが古い。

```sh
nvm install 22.9.0
nvm use 22.9.0
npm install -g npm@11.5.2
```
