---
title: "2025年10月10日"
date: 2025-10-10T00:00:00+09:00
lastmod: 2025-10-10T00:00:00+09:00
type: diary
source_month: "d202510.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

故障したサーバにRockeyを入れ直す。別の計算ノードでバージョン確認。

```sh
$ cat /etc/redhat-release 
Rocky Linux release 9.6 (Blue Onyx)
```

9.6ですね。

MacのターミナルからRockey Linux release 9.6のブータブルUSBを作ろうとしたが、ddを使ったりして危ないな。
ChatGPTにBalena Etcherというのを紹介されたが、ここは大人しくWindowsでRufasを使うか。

[https://rufus.ie/ja/](https://rufus.ie/ja/)からRufasをダウンロード。

[Rocky-9.6-x86_64-dvd.iso](https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9.6-x86_64-dvd.iso)をダウンロード、しようとしたが、公式サイトからは重すぎる。

[理研のミラー](https://ftp.riken.jp/Linux/rocky/9.6/isos/x86_64/)からダウンロード。

作業ログ。

* USBブートして計算ノードにRockeyを再インストール。
* rootパスワード指定
* インストール終了後再起動。USBを抜く。
* 起動後、最初に自分のユーザアカウントを追加
* 自分をsudoersに追加
* ホスト名の設定

  ```sh
  $ hostnamectl
    Static hostname: (unset)                           
  Transient hostname: localhost
          Icon name: computer-server
            Chassis: server 🖳
          Machine ID: 203813d2d4d548c5a2fa0799e8e79eaf
            Boot ID: ff05f843ffa64940916e346d133e6e97
    Operating System: Rocky Linux 9.6 (Blue Onyx)       
        CPE OS Name: cpe:/o:rocky:rocky:9::baseos
              Kernel: Linux 5.14.0-570.17.1.el9_6.x86_64
        Architecture: x86-64
    Hardware Vendor: Dell Inc.
      Hardware Model: PowerEdge R640
    Firmware Version: 2.8.1

  $ sudo hostnamectl set-hostname yagami03

  $ hostnamectl
  Static hostname: yagami03
        Icon name: computer-server
          Chassis: server 🖳
        Machine ID: 203813d2d4d548c5a2fa0799e8e79eaf
          Boot ID: ff05f843ffa64940916e346d133e6e97
  Operating System: Rocky Linux 9.6 (Blue Onyx)       
      CPE OS Name: cpe:/o:rocky:rocky:9::baseos
            Kernel: Linux 5.14.0-570.17.1.el9_6.x86_64
      Architecture: x86-64
  Hardware Vendor: Dell Inc.
    Hardware Model: PowerEdge R640
  Firmware Version: 2.8.1
  ```

  `hostnamectl`で現状確認、`hostnamectl set-hostname`で名前設定。
* ネットワークを固定IPに。
    * `nmcli connection show`で現状確認。

    ```sh
    $ nmcli connection show
    NAME  UUID                                  TYPE      DEVICE 
    eno1  97a43ef0-4f9d-39ba-b999-8213ca8b2f38  ethernet  eno1   
    lo    9e831b82-81ee-4317-b89e-1faf308b3e3b  loopback  lo     
    eno2  ae6e89b9-e5aa-462e-b45f-dcf149d13056  ethernet  --     
    eno3  46292068-2837-4836-916d-9b4477bf5b68  ethernet  --     
    eno4  fc161a70-08b3-4f82-ab17-d2f854f084b6  ethernet  -- 
    ```

    * DEVICEに出てきたのでeno1で接続していることがわかる。
    * eno1に192.168.1.13を設定(192.168.1.12を参考に)

    ```sh
    sudo nmcli connection modify eno1 ipv4.addresses 192.168.1.13/24
    sudo nmcli connection modify eno1 ipv4.gateway 192.168.1.2
    sudo nmcli connection modify eno1 ipv4.dns "1.1.1.1"
    sudo nmcli connection modify eno1 ipv4.method manual
    sudo nmcli connection modify eno1 ipv6.method ignore
    ```

    * ネットワーク再起動

    ```sh
    sudo systemctl restart NetworkManager
    ```

    * 別窓から新しいIPで接続して成功したことを確認。
* NISのインストールをソースから
    * Gitのインストール

    ```sh
    sudo dnf update -y
    sudo dnf install -y git
    ```

    * [ここ](https://web.chaperone.jp/w/index.php?NIS/rockylinux9)の通りに実行

    ```sh
    mkdir build
    cd build
    git clone https://github.com/thkukuk/ypbind-mt
    cd ypbind-mt
    git checkout v2.7.2
    cd ..
    tar --exclude-vcs --transform 's/ypbind-mt/ypbind-mt-2.7.2/' -cvzf ypbind-mt-2.7.2.tar.gz ypbind-mt
    ```

    これで`ypbind-mt-2.7.2.tar.gz`が作られる。
    * ypbindの作成

    ```sh
    curl -O http://dl.rockylinux.org/pub/rocky/8/AppStream/source/tree/Packages/y/ypbind-2.5-2.el8.src.rpm
    rpm -Uvh ypbind-2.5-2.el8.src.rpm
    vi ~/rpmbuild/SPECS/ypbind.spec # ブログ記事を参考に修正
    ```

    ```sh
    dnf --enablerepo=devel install -y dbus-glib-devel libnsl2-devel libtirpc-devel systemd-devel
    cd build
    cp ypbind-mt-2.7.2.tar.gz ~/rpmbuild/SOURCES/
    sudo dnf install -y rpm-build
    sudo dnf install -y autoconf automake gettext-devel docbook-style-xsl
    sudo dnf groupinstall -y "Development Tools"
    rpmbuild -bb ~/rpmbuild/SPECS/ypbind.spec
    ``` 

    * nss_nis

    ```sh
    cd
    cd build
    git clone https://github.com/thkukuk/libnss_nis
    cd libnss_nis
    git checkout v3.2
    cd ..
    tar --exclude-vcs --transform 's/libnss_nis/libnss_nis-3.2/' -cvzf libnss_nis-3.2.tar.gz libnss_nis
    ```

    ibnss_nis-3.2.tar.gzができる。
    * rpm作成

    ```sh
    curl -O http://dl.rockylinux.org/pub/rocky/8/BaseOS/source/tree/Packages/n/nss_nis-3.0-8.el8.src.rpm
    rpm -Uvh nss_nis-3.0-8.el8.src.rpm
    vi ~/rpmbuild/SPECS/nss_nis.spec  # ブログ記事を参考に修正
    cp libnss_nis-3.2.tar.gz ~/rpmbuild/SOURCES/
    rpmbuild -bb ~/rpmbuild/SPECS/nss_nis.spec
    ```

    できたかどうか確認。

    ```sh
    $ ls ~/rpmbuild/RPMS/x86_64/nss_nis-*
    /home/watanabe/rpmbuild/RPMS/x86_64/nss_nis-3.2-8.el9.x86_64.rpm
    /home/watanabe/rpmbuild/RPMS/x86_64/nss_nis-debuginfo-3.2-8.el9.x86_64.rpm
    /home/watanabe/rpmbuild/RPMS/x86_64/nss_nis-debugsource-3.2-8.el9.x86_64.rpm
    ```

    * yp-tools

    ```sh
    cd
    cd build
    curl -O http://dl.rockylinux.org/pub/rocky/8/AppStream/source/tree/Packages/y/yp-tools-4.2.3-2.el8.src.rpm
    rpmbuild --rebuild yp-tools-4.2.3-2.el8.src.rpm
    ```

    できたかどうか確認

    ```sh
    $ ls ~/rpmbuild/RPMS/x86_64/yp-tools-*
    /home/watanabe/rpmbuild/RPMS/x86_64/yp-tools-4.2.3-2.el9.x86_64.rpm
    /home/watanabe/rpmbuild/RPMS/x86_64/yp-tools-debuginfo-4.2.3-2.el9.x86_64.rpm
    /home/watanabe/rpmbuild/RPMS/x86_64/yp-tools-debugsource-4.2.3-2.el9.x86_64.rpm
    ```

    * できたRPMのインストール。

    ```sh
    sudo dnf localinstall -y ~/rpmbuild/RPMS/x86_64/ypbind-2.7.2-2.el9.x86_64.rpm ~/rpmbuild/RPMS/x86_64/nss_nis-3.2-8.el9.x86_64.rpm ~/rpmbuild/RPMS/x86_64/yp-tools-4.2.3-2.el9.x86_64.rpm
    ```

    * /etc/yum.confに以下を追加。

    ```txt
    exclude=ypbind nss_nis yp-tools authselect-libs autofs
    ```

    * ypbind起動。

    ```sh
    sudo systemctl enable ypbind --now
    ```

    失敗。
    * `rpcinfo -p NISサーバ名` が通らない。/etc/hostsをyagami02と同じものに書き換えたら、通った。
    * ypdomainnameをwatanabe-groupに

    ```sh
    sudo ypdomainname watanabe-group
    ```

    * /etc/yp.confを以下のように修正。

    ```sh
    domain watanabe-group server watanabe-login
    ```

    * 動作確認

    ```sh
    sudo systemctl start ypbind
    ypwhich
    ```

    ypwhichまでは通るがgetnetできない。
    * `/etc/nsswitch.conf`をNISを先に見るように直接編集(あまりよくないが)

  ```sh
    passwd:     nis files sss systemd
    group:      nis files [SUCCESS=merge] sss [SUCCESS=merge] systemd
    shadow:     nis files
  ```

  getentが通ることを確認。
* ホストベース認証
    * サーバ側で

    ```sh
    ssh-keyscan -t ed25519 yagami03 | sudo tee -a /etc/ssh/ssh_known_hosts
    ```

    * クライアント側で

    ```sh
    ssh-keyscan -t ed25519 watanabe-login.appi.keio.ac.jp | sudo tee -a /etc/ssh/ssh_known_hosts
    ``` 

    /etc/ssh/sshd_configで

    ```txt
    HostKey /etc/ssh/ssh_host_ed25519_key
    IgnoreUserKnownHosts no
    HostbasedAuthentication yes
    UseDNS yes
    ```

    にする。
    その上で、`/etc/ssh/shosts.equiv`にホストベース認証したいホストをずらずら書く(今回これを忘れていた)。

    ホスト側(計算ノード)で

    ```sh
    sudo firewall-cmd --add-port=2222/tcp
    sudo /usr/sbin/sshd -d -p 2222
    ```

    クライアント側(ログインノード)で

    ```sh
    ssh -o PreferredAuthentications=hostbased yagami03
    ```

    を実行し、通ればOK。sshdをrestart。

疲れたなぁ。

yagai03にNFSのインストール。

```sh
sudo dnf install -y nfs-utils
cd /mnt
sudo mkdir home_nfs
```

失敗する。firewall?

```sh
sudo firewall-cmd --permanent --add-service=nfs
sudo firewall-cmd --permanent --add-service=rpc-bind
sudo firewall-cmd --permanent --add-service=mountd
sudo firewall-cmd --reload
```

ChatGPTの言う通りに作業してて、

```sh
sudo nmcli con down eno1
sudo nmcli con up eno1
```

を叩いてしまい、ネットワーク接続が切れてリモートから作業ができなくなってしまった。アホすぎる。
