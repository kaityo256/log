---
title: "2023年10月13日"
date: 2023-10-13T00:00:00+09:00
lastmod: 2023-10-13T00:00:00+09:00
type: diary
source_month: "d202310.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

外に出られない問題、Gatewayが192.168.1.1ではなく192.168.1.2だったからだった。アホすぎる。

Ubuntuのネットワーク管理、netplanとかいうものになっててよくわからない。

```sh
Attaching to webui-docker-auto-1
Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error running hook #0: error running hook: exit status 1, stdout: , stderr: Auto-detected mode as 'legacy'
nvidia-container-cli: initialization error: nvml error: driver not loaded: unknown
```

`/etc/nvidia-container-runtime/config.toml`の中の

```toml
no-cgroups = false
```

を有効にしてDocker再起動。

```sh
nvidia-container-cli: initialization error: nvml error: driver not loaded: unknown
```

ダメですね。

```sh
$ nvidia-smi
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
```

うげ、そもそもドライバを認識してないぞ。

```sh
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 20.04.6 LTS
Release: 20.04
Codename: focal
```

```sh
sudo apt update -y
sudo apt upgrade
sudo apt install -y ubuntu-drivers-common
```

ドライバを調べる。

```sh
$ ubuntu-drivers devices | grep recommended | awk '{print $3}'
nvidia-driver-535-server-open
```

```sh
$ lspci | grep -i nvidia
c1:00.0 VGA compatible controller: NVIDIA Corporation GA106 [RTX A2000 12GB] (rev a1)
c1:00.1 Audio device: NVIDIA Corporation GA106 High Definition Audio Controller (rev a1)
```

```sh
sudo apt --fix-broken install && sudo apt upgrad
```

ダメ。

```sh
$ sudo apt install nvidia-driver-535
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 nvidia-driver-535 : Depends: libnvidia-gl-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: libnvidia-compute-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: libnvidia-extra-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: nvidia-compute-utils-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: libnvidia-decode-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: libnvidia-encode-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: nvidia-utils-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: xserver-xorg-video-nvidia-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: libnvidia-cfg1-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: libnvidia-fbc1-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Recommends: libnvidia-compute-535:i386 (= 535.113.01-0ubuntu0.20.04.1)
                     Recommends: libnvidia-decode-535:i386 (= 535.113.01-0ubuntu0.20.04.1)
                     Recommends: libnvidia-encode-535:i386 (= 535.113.01-0ubuntu0.20.04.1)
                     Recommends: libnvidia-fbc1-535:i386 (= 535.113.01-0ubuntu0.20.04.1)
                     Recommends: libnvidia-gl-535:i386 (= 535.113.01-0ubuntu0.20.04.1)
E: Unable to correct problems, you have held broken packages.
```

Recommendsを一個ずつ入れていくか。

```sh
sudo apt install -y libnvidia-compute-535 libnvidia-decode-535 libnvidia-encode-535 libnvidia-fbc1-535 libnvidia-gl-535
```

```sh
$ nvidia-smi
-bash: /usr/bin/nvidia-smi: No such file or directory
```

状況悪化。

```sh
$ sudo apt install nvidia-driver-535
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 nvidia-driver-535 : Depends: libnvidia-extra-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: xserver-xorg-video-nvidia-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
                     Depends: libnvidia-cfg1-535 (= 535.113.01-0ubuntu0.20.04.1) but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```

```sh
sudo apt install -y xserver-xorg-video-nvidia-535  libnvidia-cfg1-535
```

まだダメ。

```sh
$ sudo ubuntu-drivers autoinstall
(snip)
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
Processing triggers for linux-image-5.4.0-164-generic (5.4.0-164.181) ...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 5.4.0-164-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-5.4.0-164-generic
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
/etc/kernel/postinst.d/zz-update-grub:
Sourcing file `/etc/default/grub'
Sourcing file `/etc/default/grub.d/init-select.cfg'
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-5.4.0-164-generic
Found initrd image: /boot/initrd.img-5.4.0-164-generic
Found linux image: /boot/vmlinuz-5.4.0-128-generic
Found initrd image: /boot/initrd.img-5.4.0-128-generic
Adding boot menu entry for UEFI Firmware Settings
done
```

```sh
sudo apt install -y nvidia-driver-535-server
```

```sh
$ nvidia-smi
Fri Oct 13 11:43:25 2023       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.113.01             Driver Version: 535.113.01   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA RTX A2000 12GB          Off | 00000000:C1:00.0 Off |                  Off |
| 30%   53C    P0              N/A /  70W |      1MiB / 12282MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```

通った！！

UbuntuにChromeインストール。

```sh
cd build
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

stable-diffusion-webui-dockerが動いた。

後のためにまとめておこう。DHCP配下にあるマシンを、固定IPアドレスにして研究室サーバにぶら下げた。すると、ログインはできるが、git cloneができない。nslookupもできない。そもそも外にpingが通らない。sshはできているから、ネットワークに問題はないと考えた(これが敗因)。

まずありそうなのが、ファイアウォール。同じプライベート空間の他のマシンが大丈夫なので、マシン独自のファイアウォールが走っていることを疑うが、動いていない。

名前がひけないので、DNSを疑った。いろいろやったが、DNSを明示的に指定してnslookupしても届かない。ここでおかしいと思い始める。

最終的に、`ping 8.8.8.8`が通らないことで、絶対に変だと想う。ゲートウェイも少し疑ったのだが、netstat -rでは他のマシンのGatewayが

```sh
$ netstat -r
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         gateway         0.0.0.0         UG        0 0          0 em1
192.168.1.0     0.0.0.0         255.255.255.0   U         0 0          0 em1
```

と、IPアドレスが見えないので、間違いに気づかなかった。

最終的に、無事なマシンで

```sh
$ sudo cat /etc/sysconfig/network-scripts/ifcfg-em1
(snip)
GATEWAY=192.168.1.2 # ←あっ！
```

要するに、デフォルトゲートウェイのIPアドレスが間違っていた。プライベートアドレス空間では問題なく通信できて、外に出られないのだから、真っ先にデフォルトゲートウェイを疑うべきだったな。

まぁ、今の僕の知識ではこれに最初から気づくのは無理だっただろう。SEは経験ですね。

論文紹介用の論文を探す x 2。

書籍。5章まで書いた。演習問題はまだ。
