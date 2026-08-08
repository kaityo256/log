---
title: "2026年1月2日"
date: 2026-01-02T00:00:00+09:00
lastmod: 2026-01-02T00:00:00+09:00
type: diary
source_month: "d202601.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室のウェブサーバにhttpsで接続できずに焦る。

curlで見てみる。

```sh
$ curl -Iv https://calc.appi.keio.ac.jp/
*   Trying 133.167.114.81:443...
* TCP_NODELAY set
* Connected to calc.appi.keio.ac.jp (133.167.114.81) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* ALPN, server did not agree to a protocol
* Server certificate:
*  subject: CN=www.calc.appi.keio.ac.jp
*  start date: Dec 26 18:02:40 2025 GMT
*  expire date: Mar 26 18:02:39 2026 GMT
*  subjectAltName does not match calc.appi.keio.ac.jp
* SSL: no alternative certificate subject name matches target host name 'calc.appi.keio.ac.jp'
* Closing connection 0
* TLSv1.2 (OUT), TLS alert, close notify (256):
curl: (60) SSL: no alternative certificate subject name matches target host name 'calc.appi.keio.ac.jp'
More details here: https://curl.haxx.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
```

証明書が`www.calc.appi.keio.ac.jp`になってる。これで接続すれば良いのか。Chromeがwww.を表示しないので、`calc.appi.keio.ac.jp`だと思ってたわ。

っていうか、サーバが古いのでなんとかしなければならない。卒論・修論シーズンが終わったらやる。でもその後春の学校が・・・

体調がいまいち。

懸念事項だったガレージの掃除をした。

雪が降った。

修論2編チェックした。
