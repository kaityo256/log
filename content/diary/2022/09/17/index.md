---
title: "2022年9月17日"
date: 2022-09-17T00:00:00+09:00
lastmod: 2022-09-17T00:00:00+09:00
type: diary
source_month: "d202209.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

メモ。「Stable Diffusion」のWebUI+Docker版。

[stable-diffusion-webui-docker](https://github.com/AbdBarho/stable-diffusion-webui-docker)

研究室のGPUマシンで試してみたい。

学生さんが踏んだスパコンのエラー、UCXに起因するらしい。UCXとはUnited Communication X Frameworkの略で、UC-S、UC-T、UC-Pなどのコンポーネントからなる。踏んだエラーは[これ](https://github.com/openucx/ucx/pull/7353)だな。大量の通信パケットがあると、パケットの順番が前後してしまうことがあるらしく、それでAssertion Failedしてしまう模様。上流では対応が完了しており、スパコンでも次のメンテでアップデート予定とのこと。

こういうのがあると、「スパコンの研究室」って感じがしてきて良いですね。
