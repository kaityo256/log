---
title: "2021年4月9日"
date: 2021-04-09T00:00:00+09:00
lastmod: 2021-04-09T00:00:00+09:00
type: diary
source_month: "d202104.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

なんかsvnでコミットに失敗する。

```sh
$ svn ci -m ""
svn: E155010: コミットに失敗しました (詳しい理由は以下のとおりです):                   
svn: E155010: '/Users/watanabe/svn/study/2021/tokubetsu/ガイダンス資料.pdf' は追加準備 
状態となっていますが、存在しません
```

日本語で検索してもよくわからんので、エラーメッセージを英語にしよう。

```sh
$ LANG=C svn ci -m ""
svn: E155010: Commit failed (details follow):
svn: E155010: '/Users/watanabe/svn/study/2021/tokubetsu/{U+30AB}{U+30A4}{U+30BF}{U+30F3}{U+30B9}{U+8CC7}{U+6599}.pdf' is scheduled for addition, but is missing
```

```sh
$ svn st
?       ガイダンス資料.pdf
!       ガイダンス資料.pdf
```

あるのに無い。ふむ。とりあえずrevertしてみる。

```sh
$ svn revert ガイダンス資料.pdf
'ガイダンス資料.pdf' を元に戻しました
```

他の場所では大丈夫なのに、このディレクトリだけ、「svn add ガイダンス資料.pdf」とすると、?と!状態になってしまう。ファイルを一度別ディレクトリにコピーし、そのファイルを消して、またコピーして戻したら普通にできた。全く謎。

GitHub演習、問題からの復帰を一回やりたいな。するとこんな感じかなぁ。

* Gitの基本操作
* GitHubのアカウント作成と基本操作
* Gitの問題復帰 (rebaseとmergeを中心に)
* GitHubを用いたソフトウェア開発

4回だとあんまり深いところまで行けないかもしれない。

第一回物理情報工学特別講義。なんとかちゃんとできたかな。後で動画編集しないと。

秋の安全管理講習やった。名簿も出した。

物性研スパコンのアカウント申請だした。ハンズオンの準備をしなければ。
