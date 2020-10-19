# $5001$ $Homework$ $1$
Operating System: Ubuntu 20.04 LTS
Python Version: Python 3.7
Package needed to install in Ubuntu: hwinfo
My Github: https://github.com/Piao-WU/MSDM-5001.git
## 1. Linux operating system and memory hierarchy
### 1.1
```linux
top
```
![](2020-10-19-00-32-51.png)

### 1.2
```shell
getconf -a | grep CACHE ## get the config of CACHE
sudo hwinfo --memory  ## show the information of main memory
cd  ## show the disk space
```
![](2020-10-19-15-58-23.png)
```shell
cd /; tree|head -n 15 ## show the first 15th rows of bin catalog
```
![](2020-10-19-16-00-35.png)

## 2. Bash Script
```shell
#!/bin/bash
for ((=1;i<101;i++)); do
        mkdir DDM$i
        cd DDM$i
        echo "nanoseconds since 1970-01-01 00:00:00 UTC: " > time_till_now.txt
        date "+%s" >> time_till_now.txt
        cd ..
done
```
Check the directions:
![](2020-10-19-17-10-39.png)

## 3. Regular Expression
###1.
```python
import re
import xml.dom.minidom as xm

doc=xm.parse('blocklist.xml')
a=doc.documentElement.getElementsByTagName('emItem')
b=doc.documentElement.getElementsByTagName('gfxBlacklistEntry')
lst=(a+b)
blockID=[]
for i in lst:
    blockID.append(i.getAttribute('blockID'))
for j in blockID:
    k=re.match('^i.*\d$|^g.*\d$',j)
    if k:
        n=blockID.index(j)
        print(lst[n].toxml().split('\n')[0])
```
Output
```shell
<emItem blockID="i334" id="{0F827075-B026-42F3-885D-98981EE7B1AE}">
<emItem blockID="i1211" id="flvto@hotger.com">
<emItem blockID="i576" id="newmoz@facebook.com">
<emItem blockID="i326" id="/^((support2_en@adobe14\.com)|(XN4Xgjw7n4@yUWgc\.com)|(C7yFVpIP@WeolS3acxgS\.com)|(Kbeu4h0z@yNb7QAz7jrYKiiTQ3\.com)|(aWQzX@a6z4gWdPu8FF\.com)|(CBSoqAJLYpCbjTP90@JoV0VMywCjsm75Y0toAd\.com)|(zZ2jWZ1H22Jb5NdELHS@o0jQVWZkY1gx1\.com))$/">
<emItem blockID="i258" id="helperbar@helperbar.com">
......
......
<gfxBlacklistEntry blockID="g208">
<gfxBlacklistEntry blockID="g202">
<gfxBlacklistEntry blockID="g1124">
<gfxBlacklistEntry blockID="g1217">
<gfxBlacklistEntry blockID="g200">
```
### 3
```python
ID=[]
for i in a:
    ID.append(i.getAttribute('id'))
for j in ID:
    l=re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z_\-]{1,19}\.[com,cn,net,org]{1,3}$',j)
    if l:
        m=ID.index(j)
        print(lst[m].toxml().split('\n')[0])
```

```shell
<emItem blockID="i1211" id="flvto@hotger.com">
<emItem blockID="i576" id="newmoz@facebook.com">
<emItem blockID="i258" id="helperbar@helperbar.com">
<emItem blockID="i218" id="ffxtlbr@claro.com">
<emItem blockID="i816" id="noOpus@outlook.com">
......
......
<emItem blockID="i1492" id="googlotim@gmail.com">
<emItem blockID="i1524" id="ext@alibonus.com">
<emItem blockID="89a61123-79a2-45d1-aec2-97afca0863eb" id="InternetProtection@360safe.com">
<emItem blockID="e16408c3-4e08-47fd-85a9-3cbbce534e95" id="WebProtection@360safe.com">
<emItem blockID="baf7f735-d6b6-410a-8cc8-25c60f7c57e2" id="adbeaver@adbeaver.org">
```
