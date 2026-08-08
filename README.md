# LOG

[kaityo256](https://github.com/kaityo256) の日記のようなものです。

- 公開サイト: <https://kaityo256.github.io/log/>
- ライセンス: [CC-BY](LICENSE)

## 必要な環境

- Python 3.12以降（追加パッケージ不要）
- Hugo Extended 0.159.2
- GNU Make

HugoはローカルとCIで同じバージョンを使用します。インストール後、次のコマンドで確認できます。

```sh
make version
```

## 日記を書く

月別Markdownの `log/dYYYYMM.md` が原稿の正本です。生成される `content/diary/` と `data/split-manifest.json` はGit管理せず、直接編集しません。

月の先頭と各日の日付は次の形式で記述します。

```markdown
# 2026年8月

## 8月9日(日)

本文
```

VS CodeではMarkdownファイルで `date` と入力して補完すると日付見出しを挿入できます。

## ローカルで確認する

```sh
make serve
```

変更された月だけを日別Markdownへ分割し、`http://localhost:1313/log/` でHugoの開発サーバーを起動します。ファイルを保存するとブラウザーが自動更新されます。

1313番ポートが使用中の場合は、URLとポートを同時に変更できます。

```sh
make serve LOCAL_BASE_URL=http://localhost:14131/log/ LOCAL_PORT=14131
```

個別の操作は以下のとおりです。

```sh
make generate  # 変更月だけを分割
make generate-all # 全月を分割
make test      # 分割スクリプトの単体テスト
make check     # 生成物の検証とproduction build
make build     # public/へproduction build
make clean     # Hugoの公開物とキャッシュを削除
```

特定の月だけを明示的に変換する場合は、スクリプトを直接実行します。

```sh
python3 scripts/split_diary.py --month 2026-08
```

全月を再生成する場合は次のとおりです。

```sh
make generate-all
```

## 生成と検証の仕組み

ローカルでは `data/split-manifest.json` に月別原稿のSHA-256を記録します。内容が変わっていない月は生成先へ書き込まないため、日別ファイルの更新時刻も変わりません。このmanifestと生成先はGit管理せず、GitHub Actionsではクリーンなcheckoutから全月を生成します。

変換時には以下を検証します。

- ファイル名、月見出し、日付見出しの年月が一致すること
- 日付が実在すること
- レベル2見出しがすべて日付形式であること
- Markdownのコードフェンスが閉じていること
- 生成物とmanifestが最新であること

曜日の不一致と同じ日付の重複は警告します。重複した日付の本文は記載順を保って一つの日別記事へ結合します。

## 公開

Pull Requestでは、GitHub Actionsが全月の分割、分割処理のテスト、生成物検証、Hugoのproduction build、内部リンクとRSSの検査を行います。`main`へのpushでは同じ処理後、生成した `public/` をGitHub Pagesへデプロイします。

公開URLは以下の構成です。

- 日別: `/log/YYYY/MM/DD/`
- 月別: `/log/YYYY/MM/`
- 年別: `/log/YYYY/`
- RSS: `/log/index.xml`

従来の `/log/dYYYYMM.html#DD` からも、対応する日別ページへ移動できる互換ページを生成します。

## トラブルシュート

生成物が古いと表示された場合は、まず変更月を生成します。

```sh
make generate
make check
```

変換エラーには原稿のファイル名と行番号が表示されます。該当する月見出しまたは日付見出しを修正してから再実行してください。Hugoのバージョンが異なる場合は、0.159.2へ合わせてください。
