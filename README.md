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

`
opkg update
opkg install git
opkg install git-http
opkg install python

git clone https://github.com/tommcm1200/heatermeter-aws-iot.git
mkdir ./heatermeter-aws-iot/certs/
`
copy certs and keys to your Heatermeter
`
scp *.key root@192.168.1.37:/root/heatermeter-aws-iot/certs
scp *.pem root@192.168.1.37:/root/heatermeter-aws-iot/certs
`

## Notes:
opkg print-architecture
opkg 
/etc/opkg/distfeeds.conf
src/gz reboot_core http://downloads.lede-project.org/snapshots/targets/brcm2708/bcm2708/packages
src/gz reboot_base http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/base
# src/gz reboot_linkmeter http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/linkmeter
# src/gz reboot_luci http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/luci
src/gz reboot_packages http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/packages


opkg install http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/packages/git_2.19.1-1_arm_arm1176jzf-s_vfp.ipk

opkg install http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/packages/git-http_2.19.1-1_arm_arm1176jzf-s_vfp.ipk

opkg install http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/packages/python-light_2.7.15-1_arm_arm1176jzf-s_vfp.ipk



https://zzz.buzz/2016/02/20/using-git-on-opkg-powered-systems/ 


https://openwrt.org/packages/pkgdata/python

pip install sseclient

https://github.com/w4ilun/edison-guides/wiki/Installing-Git-on-Intel-Edison




Hi.

I'm a new owner of a Heatermeter v4.3 and kicking off a little IoT project to enhance some of the features.  

I'm wanting to install Git and Python packages to help facilitate with some mods but have an issue with installing packages.  Any guidance from anyone who has attempted this before would be much appreciated.

Results: 
root@HEATERMETER:~# opkg update
*** Failed to download the package list from http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/linkmeter/Packages.gz

root@HEATERMETER:~# wget http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/linkmeter/Packages.gz
Downloading 'http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/linkmeter/Packages.gz'
Connecting to 148.251.78.235:80
HTTP error 404

Browsing to http://downloads.lede-project.org/snapshots/packages/arm_arm1176jzf-s_vfp/ I see no "linkmeter" folder.

Has the package list been moved?  What's the best package URL should I use instead?  

Thx.