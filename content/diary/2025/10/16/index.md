---
title: "2025年10月16日"
date: 2025-10-16T00:00:00+09:00
lastmod: 2025-10-16T00:00:00+09:00
type: diary
source_month: "d202510.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

一応メモ。

ある大学のキャッチコピーに「I am I.」と書いてあり、それが文法的におかしい、さすがFランみたいなつぶやきを見かけた。実はI am I.というのは(少し古めかしく聞こえるが)文法的に正しい。

リチャード三世のAct 5, シーン5にこんな記述がある。

> The lights burn blue. It is now dead midnight.
> Cold fearful drops stand on my trembling flesh.
> What do I fear? Myself? There’s none else by.
> Richard loves Richard; that is, **I am I**.
> Is there a murderer here? No. Yes, I am.
> Then fly! What, from myself? Great reason. Why:
> Lest I revenge. Myself upon myself?
> Alack, I love myself. Wherefore? For any good
> That I myself have done unto myself?
> O no, alas, I rather hate myself
> For hateful deeds committed by myself.
> I am a villain.

[King John](https://shakespeare.mit.edu/john/full.html
)にもある。

> Madam, by chance but not by truth; what though?
> Something about, a little from the right,
> In at the window, or else o'er the hatch:
> Who dares not stir by day must walk by >night,
> And have is have, however men do catch:
> Near or far off, well won is still well shot,
> And **I am I**, howe'er I was begot.

あとは、オクスフォード大学の神学教授、Henry Scott Hollandによる「Death Is Nothing At All」にも

> Everything remains exactly as it was.
> **I am I**, and you are you,
> and the old life that we lived so fondly together is untouched, unchanged.
> Whatever we were to each other, that we are still.

という用例が見られる。

まぁ、「Fラン」とバカにした人に教養がなかったというだけの話なんだけど、人を馬鹿にするのはやめようね。

Tahoeになってから、ウィンドウに切り替わりが遅い。具体的には、ブラウザからVSCodeに切り替える時に1秒くらい固まることがある。

これ、どうもElectronの問題らしい。少なくとも、GPUの利用率が100%近くなる問題があったらしい。しかし、迅速なバージョンアップにより修正されたはず。しかし、まだ重いな。

Electron製のアプリに影響するので、VS CodeやSlackなどが影響を受けるっぽい。うーむ。

普段使いのWindows PCのディスク容量が足りずに不具合がおき始めた。いろいろアプリをアンインストールしてもだめ。

わかった。仮想記憶領域vhdファイルが大きくなりすぎてるんだ。vhdを圧縮しても小さくならない。

急遽、異なるPCのセットアップに入る。うーん。

以下、メモ：

* Google Chrome インストール
* PowerShellで `wsl --install`再起動
* Microsoft StoreでUbuntu 24.04をインストール
* Subversionのインストール

```sh
sudo apt update
sudo apt upgrade -y
sudo apt install -y subversion
```

公開鍵を登録し、すぐにサーバからリポジトリを一括でcheckout。いまどきSubversion管理・・・と思わなくはないが、研究教育関連が全部一つのリポジトリに突っ込んであるので、こうして一括で復活できるのは楽だ。

* Microsoft 365をインストール。
* Adobe Readerをインストール(あまり入れたくないのだが)。
* VSCodeをインストール
* Git for Windowsをインストール

UbuntuとGit Bashの公開鍵をGitHubに登録。

GitHubでパスキーQRコードをスマホで撮影してもサポートされていないと表示される原因がわかった。スマホの写真アプリではダメで、Google Lensを使う必要があった。

とりあえず新しいWindows PCセットアップ完了。明日の講義に間に合った・・・

そして論文修正ができてない・・・
