---
title: "2022年1月26日"
date: 2022-01-26T00:00:00+09:00
lastmod: 2022-01-26T00:00:00+09:00
type: diary
source_month: "d202201.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

よく国際研究会のメールが届く。全部が全部そうとは言わないが、結構なものが「商業研究会」であり、うっすい研究会で参加費をとって運営が儲ける、参加者は「国際会議でInvite Speakerになった」という実績を得る、ようするにpredatory journalの研究会版である。と思ったら、「Predatory conference」という名前が既にあるらしい。

で、今回来た国際研究会は結構すごかった。Invited Speakerのうち、二人だけH Indexが書いてある。誇らしげに。しかも「The Scientistt」って、「The Scientist Magazine」のパクリだな。キャッチコピーも酷似。

っていうかなんで創薬の会議に情報理論の専門家が参加しているのよ。

Qiitaのホーム、完全に死んでる。少なくとも僕の食指が動くような記事が全くでてこない。百歩譲ってホームは「育て」ないといけないとしても「トレンド」も死んでしまっている。昔は毎日、一つか二つは興味のある記事があったのだが、今は・・・

これ、アルゴリズムが僕に合わなくなったのか、それとも執筆者が引っ越しをしてしまったのか・・・

Xbyakハンズオン、英訳した。しかし、Dockerイメージのビルドに失敗するようになった。エラーメッセージはこれ。

```txt
error: pam: signature from "Levente Polyak (anthraxx) <levente@leventepolyak.net>" is unknown trust
```

検索したら、[Keyringを更新しろ](https://bbs.archlinux.org/viewtopic.php?id=221435)とのこと。

```sh
pacman -Sy --noconfirm archlinux-keyring
```

を追加してみた。

```sh
$ make no-cache
docker build -t kaityo256/xbyak_aarch64_handson . --no-cache
[+] Building 149.8s (23/23) FINISHED       
```

できた。
[Xbyakハンズオンの英訳](https://github.com/kaityo256/xbyak_aarch64_handson)終了。どこで宣伝すればいいのかな。[dev.to](https://dev.to/)くらいしか知らないんだけど。とりあえずdev.toにアカウントだけ作った。GitHubで接続。
