---
title: "2021年11月7日"
date: 2021-11-07T00:00:00+09:00
lastmod: 2021-11-07T00:00:00+09:00
type: diary
source_month: "d202111.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Windows 11になって、Win+Shift+Sによるスクリーンショットがとれなくなり、IMEが2回以上変換できなくなり、さらに旧バージョンに戻しても変換にタイムラグがある問題、[証明書の期限切れ](https://docs.microsoft.com/en-us/windows/release-health/status-windows-11-21h2#november-2021)が原因だったらしい。これは緊急パッチ[KB5008295](https://support.microsoft.com/ja-jp/topic/2021-%E5%B9%B4-11-%E6%9C%88-5-%E6%97%A5-kb5008295-%E5%B8%AF%E5%9F%9F%E5%A4%96-5540f171-846c-4af0-b363-29b6f02a8935)の適用により修正される。実際に適用したら、Win+Shift+Sが使えるようになり、IMEもストレスない程度のレスポンスに改善。

証明書の期限は10月31日だったそうで、それならデバッグ中は問題が表面化せず、11月になってからアップデートしたユーザで不具合が出て気づく、というのは納得がいく。納得はいくが、わりと初歩的なミスなのでは・・・

それはそれとして、Windows 10でできて11でできないことは[結構あるようだ](https://answers.microsoft.com/en-us/windows/forum/all/list-of-changed-or-removed-featuresfunctionalities/1151c688-462a-4579-9164-8d11c78652c8)。

特にタスクバーは[UWP (Universal Windows Platform)](https://docs.microsoft.com/ja-jp/windows/uwp/get-started/universal-application-platform-guide)という基盤でスクラッチから書き直されたため、以下のようにかなり機能が減っている。

* 2つ目のディスプレイに時計が出ない
* タスクバーを動かせない
* スタートメニューにフォルダを作れない
* タスクバーにドラッグアンドドロップできない

Vistaと比較してしまったが、ガタガタだったVistaよりはまとまっており、障害対応もはやかった印象。それにしても、もう少し作り込んでからリリースしても良かったのでは、という気がしないでもない。
