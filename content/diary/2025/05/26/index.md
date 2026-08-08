---
title: "2025年5月26日"
date: 2025-05-26T00:00:00+09:00
lastmod: 2025-05-26T00:00:00+09:00
type: diary
source_month: "d202505.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

1on1の日程、全て非公開になってた・・・ orz
自分からは見えるので気づかなかった。

ChatGPTに聞いたら、Google Cloud Console を使う方法を提案されたが、どうも有料っぽいので別のを聞いたらGAS (Google Apps Script)が使えるそうなので、それを実行した。

こんなの。

```js
function setVisibilityToDefaultFor1on1() {
  const calendarId = 'your_calendar_id@group.calendar.google.com'; // ← あなたのカレンダーIDに変更
  const calendar = CalendarApp.getCalendarById(calendarId);

  const now = new Date();
  const oneYearLater = new Date();
  oneYearLater.setFullYear(now.getFullYear() + 1);

  // 1年間のイベントを取得
  const events = calendar.getEvents(now, oneYearLater);

  let updatedCount = 0;

  for (const event of events) {
    const title = event.getTitle();
    if (title.includes('1on1') && event.getVisibility() !== CalendarApp.Visibility.DEFAULT) {
      event.setVisibility(CalendarApp.Visibility.DEFAULT);
      Logger.log(`Updated: ${title}`);
      updatedCount++;
    }
  }

  Logger.log(`Total updated events: ${updatedCount}`);
}
```

これをGoogle Drive を開く → 「新規」→「その他」→「Google Apps Script」に貼り付けて、カレンダーIDを修正してから実行。できた。

シミュレーション工学。時間ギリギリ。もう少し減らした方が良いかも。

FS報告書提出。

タイヤ交換電話。

その他もろもろ。
