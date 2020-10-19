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


ID=[]
for i in a:
    ID.append(i.getAttribute('id'))
for j in ID:
    l=re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z_\-]{1,19}\.[com,cn,net,org]{1,3}$',j)
    if l:
        m=ID.index(j)
        print(lst[m].toxml().split('\n')[0])
