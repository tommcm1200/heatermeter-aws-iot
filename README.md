# heatermeter-aws-iot

## Required Libraries
sseclient 0.0.19
https://pypi.org/project/sseclient/





## Setup and Install


### AWS Configuration
Log in to AWS Console and head to IOT Core

Select SECURE --> CERTIFICATES
Select the certificate you have just created and downloaded.
Take note of the Certificate ARN to be used as a parameter int ehCloudformation Tempalte.

-----
### Heatermeter Configuration
check /etc/opkg/distfeeds.conf and update dist feeds as needed.

```
opkg update
opkg upgrade openssl-util libopenssl
opkg install git-http
opkg install python
git clone https://github.com/tommcm1200/heatermeter-aws-iot.git
mkdir ./heatermeter-aws-iot/certs/
```
copy certs and keys to your Heatermeter
`
scp *.key root@192.168.1.37:/root/heatermeter-aws-iot/certs
scp *.pem root@192.168.1.37:/root/heatermeter-aws-iot/certs
`

## Notes:
vi /etc/opkg/distfeeds.conf
```
src/gz reboot_core http://downloads.lede-project.org/snapshots/targets/brcm2708/bcm2708/packages
src/gz reboot_base http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/base
# src/gz reboot_linkmeter http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/linkmeter
# src/gz reboot_luci http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/luci
src/gz reboot_packages http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/packages
```


-----
python-pyopenssl
python3


https://zzz.buzz/2016/02/20/using-git-on-opkg-powered-systems/ 


https://openwrt.org/packages/pkgdata/python

pip install sseclient

https://github.com/w4ilun/edison-guides/wiki/Installing-Git-on-Intel-Edison

https://relayr.readthedocs.io/en/latest/openwrt.html


root@LEDE:~# python -c "import ssl"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/lib/python2.7/ssl.py", line 98, in <module>
ImportError: Error relocating /usr/lib/python2.7/lib-dynload/_ssl.so: SSL_CTX_set_next_proto_select_cb: symbol not found
root@LEDE:~# ldd /usr/lib/python2.7/lib-dynload/_ssl.so
	ldd (0x7f58b000)
	libssl.so.1.0.0 => /usr/lib/libssl.so.1.0.0 (0xb6e9f000)
	libcrypto.so.1.0.0 => /usr/lib/libcrypto.so.1.0.0 (0xb6d72000)
	libpython2.7.so.1.0 => /usr/lib/libpython2.7.so.1.0 (0xb6c02000)
	libgcc_s.so.1 => /lib/libgcc_s.so.1 (0xb6be8000)
	libc.so => ldd (0x7f58b000)
	libz.so.1 => /usr/lib/libz.so.1 (0xb6bc6000)
Error relocating /usr/lib/python2.7/lib-dynload/_ssl.so: SSL_CTX_set_next_proto_select_cb: symbol not found
Error relocating /usr/lib/python2.7/lib-dynload/_ssl.so: SSL_CTX_set_next_protos_advertised_cb: symbol not found
Error relocating /usr/lib/python2.7/lib-dynload/_ssl.so: SSL_get0_next_proto_negotiated: symbol not found

-----
https://bugs.openwrt.org/index.php?do=details&task_id=1205

opkg list-upgradable
opkg upgrade libopenssl

https://openwrt.org/docs/guide-user/luci/getting-rid-of-luci-https-certificate-warnings

root@LEDE:/etc/ssl# openssl req -x509 -nodes -days 730 -newkey rsa:2048 -keyout mycert.key -out mycert.crt -config myconfig.con
f
Error relocating /usr/bin/openssl: SSL_CTX_set_srp_strength: symbol not found
Error relocating /usr/bin/openssl: SSL_set_srp_server_param: symbol not found
Error relocating /usr/bin/openssl: SRP_create_verifier: symbol not found
Error relocating /usr/bin/openssl: SRP_check_known_gN_param: symbol not found
Error relocating /usr/bin/openssl: SRP_VBASE_init: symbol not found
Error relocating /usr/bin/openssl: SSL_get_srp_g: symbol not found
Error relocating /usr/bin/openssl: SSL_CTX_set_srp_cb_arg: symbol not found
Error relocating /usr/bin/openssl: SRP_VBASE_get1_by_user: symbol not found
Error relocating /usr/bin/openssl: SSL_CTX_set_srp_username_callback: symbol not found
Error relocating /usr/bin/openssl: SRP_user_pwd_free: symbol not found
Error relocating /usr/bin/openssl: SSL_CTX_set_next_proto_select_cb: symbol not found
Error relocating /usr/bin/openssl: SRP_VBASE_new: symbol not found
Error relocating /usr/bin/openssl: SSL_CTX_set_srp_username: symbol not found
Error relocating /usr/bin/openssl: SSL_CTX_set_next_protos_advertised_cb: symbol not found
Error relocating /usr/bin/openssl: SRP_get_default_gN: symbol not found
Error relocating /usr/bin/openssl: SSL_get_srp_username: symbol not found
Error relocating /usr/bin/openssl: SSL_CTX_set_srp_client_pwd_callback: symbol not found
Error relocating /usr/bin/openssl: SSL_get_srp_N: symbol not found
Error relocating /usr/bin/openssl: SSL_get0_next_proto_negotiated: symbol not found
Error relocating /usr/bin/openssl: SSL_CTX_set_srp_verify_param_callback: symbol not found


----

Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-15xc0q/sseclient/

 File "/usr/lib/python2.7/site-packages/pip/basecommand.py", line 215, in main
  File "/usr/lib/python2.7/site-packages/pip/commands/install.py", line 342, in run
  File "/usr/lib/python2.7/site-packages/pip/req/req_set.py", line 784, in install
  File "/usr/lib/python2.7/site-packages/pip/req/req_install.py", line 851, in install
  File "/usr/lib/python2.7/site-packages/pip/req/req_install.py", line 1064, in move_wheel_files
  File "/usr/lib/python2.7/site-packages/pip/wheel.py", line 345, in move_wheel_files
  File "/usr/lib/python2.7/site-packages/pip/wheel.py", line 323, in clobber
  File "/usr/lib/python2.7/shutil.py", line 98, in copyfile
  File "/usr/lib/python2.7/shutil.py", line 66, in copyfileobj
IOError: [Errno 28] No space left on device

-----

https://raspberrypi.stackexchange.com/questions/499/how-can-i-resize-my-root-partition


https://oldwiki.archive.openwrt.org/doc/howto/pywws?s[]=python&s[]=pip

wget https://bootstrap.pypa.io/ez_setup.py
python ez_setup.py
git clone https://github.com/btubbs/sseclient.git
cd ./sseclient/
python setup.py install