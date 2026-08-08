---
title: "2025年10月13日"
date: 2025-10-13T00:00:00+09:00
lastmod: 2025-10-13T00:00:00+09:00
type: diary
source_month: "d202510.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

リモート作業中にうっかり、

```sh
sudo nmcli con down eno1
sudo nmcli con up eno1
```

をやってしまって接続が切れたノード、物理ログインしてリブートしたら固定IPだけになった。そして、ypbindが走ってるので/homeでpermission denied。まず固定IPを指定してリブート、が最初の作業だな。

まずはNFSのマウント確認。

```sh
$ sudo mount -t nfs 192.168.1.20:/home /mnt/home_nfs
Created symlink /run/systemd/system/remote-fs.target.wants/rpc-statd.service → /usr/lib/systemd/system/rpc-statd.service.
```

この状態で、

```sh
$ cd
-bash: cd: /home/watanabe: 許可がありません
$ cd /mnt/home_nfs/watanabe/
$ 
```

NISでアカウント共有しているので、/homeはpermission deniedだが、/mnt/home_nfs/watanabe/はちゃんと見れる。正しくNIS共有+NFSできてますね。よしよし。

```sh
sudo umount /mnt/home_nfs/
sudo mount -t nfs 192.168.1.20:/home /home
cd
```

/home通った。dfで確認。

```sh
$ df | grep home
192.168.1.20:/home  46872928256 27035027456 19837900800   58% /home
```

よしよし。`/etc/fstab`を以下のように修正。

```sh
/dev/mapper/rl-root     /                       xfs     defaults        0 0
UUID=1a0defb8-f376-4254-8e56-3a9a9cbe949f /boot                   xfs     defaults        0 0
UUID=DD5A-1F2D          /boot/efi               vfat    umask=0077,shortname=winnt 0 2
#/dev/mapper/rl-home     /home                   xfs     defaults        0 0
/dev/mapper/rl-swap     none                    swap    defaults        0 0
192.168.1.20:/home      /home                   nfs     defaults,_netdev  0  0
```

リブート。ここまでで、

* ホストベース認証
* NIS共有
* NFS

まで通った。

次、slurmのインストール(クライアント)。

`/etc/selinux/config`で

```sh
SELINUX=disabled
```

にしてからreboot。

mungeのインストール

```sh
sudo dnf -y install munge
```

リブートしたら外に繋がらんくなった。なんでだよ・・・

yagami02のdefault gatewayが192.168.1.2なのに、yagami03が192.168.1.1になってた。コマンド履歴を見ると192.168.1.2を指定しているんだけどなぁ。

```sh
sudo ip route del default
sudo ip route add default via 192.168.1.2 dev eno1
```

により通ったので、

```sh
sudo nmcli con mod eno1 ipv4.gateway "192.168.1.2"
sudo nmcli con up eno1
```

で永続化。

あと、nameserverはNetworkManagerが自動生成するので、/etc/resolv.confを手で書いても上書きされてしまう。

```sh
sudo nmcli con mod eno1 ipv4.dns "1.1.1.1"
sudo systemctl restart NetworkManager
```

これで/etc/resolv.confが修正されていることを確認。

改めてmungeのインストール。

ログインノードから計算ノードにmunge.keyのコピーをする必要があるが、/homeを共有しているのでそこを経由して。

```sh
sudo cp /etc/munge/munge.key .
sudo cp munge.key /etc/munge/
sudo chown munge:munge /etc/munge/munge.key
```

追記：chownを忘れてた

```sh
sudo dnf install slurm slurm-slurmd munge
```

slurm.confにyagami03を追加。

ログインノードのslurm.confを/home経由でコピー。

```sh
sudo cp slurm.conf /etc/slurm/
```

計算ノードは6818をあける必要がある。

```sh
sudo firewall-cmd --permanent --add-port=6818/tcp
sudo systemctl restart firewalld
```

追記：firewallの再起動を忘れて、つながらなかった。

ディレクトリの作成と所有者の修正。

```sh
sudo mkdir -p /var/spool/slurm/d /var/log/slurm /var/run/slurm
sudo chown -R slurm:slurm /var/spool/slurm /var/log/slurm /var/run/slurm
sudo chmod 755 /var/spool/slurm /var/log/slurm /var/run/slurm
```

mungeとslurmdを起動。自動起動も追加。

```sh
sudo systemctl start munge
sudo systemctl start slurmd
sudo systemctl enable --now munge
sudo systemctl enable --now slurmd
```

ログインノードで、slurmdctldの再起動。

```sh
sudo systemctl restart slurmctld
sudo scontrol reconfigure
```

sinfoで確認。OK。

その後yagami03を再起動したらまた死んだ。

```sh
sudo systemctl enable --now munge
sudo systemctl enable --now slurmd
```

を設定して自動起動をONにしていなかったのが原因。起動してからログインノードで以下を実行したら復活。

```sh
sudo scontrol update nodename=yagami03.appi.keio.ac.jp state=resume
```

新たにyagami01をセットアップ。今度こそ手順完全版を作る。

USBでRockey Linux 9.6をインストール

`/etc/hosts`の内容をyagami02からコピー

ホスト名の設定。

```sh
sudo hostnamectl set-hostname yagami01
```

これで`hostname`と`hostname -f`が想定通りになることを確認。

固定IPをふり、かつDNSやDefault GWを設定。

```sh
sudo nmcli connection modify eno1 ipv4.addresses 192.168.1.11/24
sudo nmcli connection modify eno1 ipv4.gateway 192.168.1.2
sudo nmcli connection modify eno1 ipv4.dns "1.1.1.1"
sudo nmcli connection modify eno1 ipv4.method manual
sudo nmcli connection modify eno1 ipv6.method ignore
sudo nmcli connection up eno1
```

を実行してから念のためreboot(NetworkManagerだけで良いかもしれないが、接続中だと変な設定が残ることがあるので)。

ホストベース認証。

まずはSELinuxを無効に。

```sh
sudo setenforce 0
```

```sh
sudo vim /etc/selinux/config
```

で、

```sh
SELINUX=disabled
```

に。

ログインノード側で

```sh
ssh-keyscan -t ed25519 yagami01 | sudo tee -a /etc/ssh/ssh_known_hosts
```

計算ノード側で、

```sh
ssh-keyscan -t ed25519 watanabe-login.appi.keio.ac.jp | sudo tee -a /etc/ssh/ssh_known_hosts
```

`/etc/ssh/shosts.equiv`を以下の内容に。

```sh
watanabe-login.appi.keio.ac.jp
yagami01
yagami02
yagami03
yagami04
```

`/etc/ssh/sshd_config`を以下のように修正。

```txt
HostKey /etc/ssh/ssh_host_ed25519_key
IgnoreUserKnownHosts no
HostbasedAuthentication yes
UseDNS yes
```

計算ノードに2222を開けてsshdを2222で起動。

```sh
sudo firewall-cmd --add-port=2222/tcp
sudo /usr/sbin/sshd -d -p 2222
```

ログインノードから接続確認。

```sh
ssh -o PreferredAuthentications=hostbased yagami01 -p 2222
```

接続できたら、計算ノードでsshdをrestart。

```sh
sudo systemctl restart sshd
```

ログインノードから通常ポートで接続。

```sh
ssh -o PreferredAuthentications=hostbased yagami01
```

接続できたらホストベース認証完成。

次、NISの設定。

DNFのアップデート。

```sh
sudo dnf update -y
```

別ノードで作った以下の3つのRPMをコピーしてインストール。

```sh
mkdir build
cd build
scp yagami03:build/*.rpm .
sudo dnf localinstall -y ~/build/ypbind-2.7.2-2.el9.x86_64.rpm ~/build/nss_nis-3.2-8.el9.x86_64.rpm ~/build/yp-tools-4.2.3-2.el9.x86_64.rpm
```

`/etc/yum.conf`に以下を追加。

```txt
exclude=ypbind nss_nis yp-tools authselect-libs autofs
```

```sh
sudo ypdomainname watanabe-group
```

`/etc/yp.conf`を以下のように修正。

```txt
domain watanabe-group server watanabe-login
```

ypbind起動。

```sh
sudo systemctl start ypbind
```

```sh
$ ypwhich
watanabe-login
```

`/etc/nsswitch.conf`をNISを先に見るように直接編集。

```sh
passwd:     nis files sss systemd
group:      nis files [SUCCESS=merge] sss [SUCCESS=merge] systemd
shadow:     nis files
```

getentが通ることを確認。

```sh
getent passwd 適当なユーザ名
```

通った。

次、NFS。

```sh
sudo dnf install -y nfs-utils
sudo mkdir -p /mnt/home_nfs
sudo mount -t nfs 192.168.1.20:/home /mnt/home_nfs
```

これでマウントできることを確認。

```sh
sudo umount /mnt/home_nfs
```

`/etc/fstab`を以下のように修正。

```txt
/dev/mapper/rl-root     /                       xfs     defaults        0 0
UUID=d35febed-3269-4ca5-b494-27d11a2d387f /boot                   xfs     defaults        0 0
UUID=9032-A23D          /boot/efi               vfat    umask=0077,shortname=winnt 0 2
#/dev/mapper/rl-home     /home                   xfs     defaults        0 0
/dev/mapper/rl-swap     none                    swap    defaults        0 0
192.168.1.20:/home      /home                   nfs     defaults,_netdev  0  0
```

リブート。`/home/`が正しくマウントできた。

次、slurm。

mungeのインストール。

```sh
sudo dnf -y install munge
```

既に/homeにmunge.keyがあるので共有。

```sh
sudo cp munge.key /etc/munge/
sudo chown munge:munge /etc/munge/munge.key
```

Slurmのインストール。

```sh
sudo dnf groupinstall "Development Tools" -y
sudo dnf install -y epel-release
sudo dnf install -y slurm slurm-slurmd
```

ログインノードの/etc/slurm/slurm.confにyagami01を追加。

```txt
# COMPUTE NODES
NodeName=watanabe-login.appi.keio.ac.jp CPUs=20 State=UNKNOWN
NodeName=yagami01.appi.keio.ac.jp CPUs=20 State=UNKNOWN
NodeName=yagami02.appi.keio.ac.jp CPUs=20 State=UNKNOWN
NodeName=yagami03.appi.keio.ac.jp CPUs=20 State=UNKNOWN
PartitionName=main Nodes=ALL Default=YES MaxTime=1-00:00:00 State=UP
```

ログインノードで/homeにコピー。

```sh
sudo cp /etc/slurm/slurm.conf .
```

計算ノードでローカルにコピー。

```sh
sudo cp slurm.conf /etc/slurm/
```

6818をあける。

```sh
sudo firewall-cmd --permanent --add-port=6818/tcp
sudo systemctl restart firewalld
```

slurmユーザの作成。

```sh
sudo groupadd -g 64030 slurm
sudo useradd -u 64030 -g slurm -m -d /var/lib/slurm -s /sbin/nologin -r slurm
```

```sh
sudo mkdir -p /var/spool/slurm/d /var/log/slurm /var/run/slurm
sudo chown -R slurm:slurm /var/spool/slurm /var/log/slurm /var/run/slurm
sudo chmod 755 /var/spool/slurm /var/log/slurm /var/run/slurm
```

mungeとslurmdを起動。

```sh
sudo systemctl enable --now munge
sudo systemctl enable --now slurmd
sudo systemctl start munge
sudo systemctl start slurmd
```

計算ノードでslurmctldを再起動して再読み込み。

```sh
sudo systemctl restart slurmctld
sudo scontrol reconfigure
```

計算ノードを認識した。

あとはすべての計算ノードで、

```sh
sudo dnf install -y openmpi openmpi-devel
```

とかやってから、/etc/bashrcに

```sh
export PATH=/usr/lib64/openmpi/bin:$PATH
```

を追加しないとmpirunにパスが通らない。

```sh
export PATH=$PATH:/home/apps/lammps
mpirun -np 20 lmp < collision.input 
```

が全てのノードで通ることを確認。
終わったぞ〜！！！

もう一つの懸案だった、学科ウェブに学生さんの受賞情報を掲載するのもやった。
