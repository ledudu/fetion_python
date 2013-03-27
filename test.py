#encoding=utf-8
#import random
from xml.etree import ElementTree
import hashlib
from hashlib import sha1
import struct
from locale import atoi
from binascii import a2b_hex
import time
from datetime import date
import re
#nonce='105823CE77005E6C1A91825249404B75'
#key='B2C28349959452251DF2D3C3C9C012D52F19B9AFBA7F38F62A258F631197C56B80CFEEDE4723F7D6A0623F418D3DBC7496AE9F31058BBD52A3F230497F9D1C48C8F12BF50EC2DEE3EBF84D89E5323EA033696B48110C6937F2DAF7B0B42D20CCFD3D947895BAD6C6E75F5F48782E64322438AA63745B5E306684F289975B8C49010001'
#passeword
#
##def v4digest():
#    
##change form abcd to a group, a[0]=0xab, a[1]=0xcd
#def str2hex(str_in):
#    alist=list()
#    inlen=len(str_in)
#    for i in range(0, inlen/2):
#        data_i = string.atoi('0x'+str_in[2*i:2*i+1], 16)
#        chr(data_i)
#    return ''.join(alist)
#
#passeord='941a575e33318ddc1dc1da4d882ca3a2025744f7'
#pwd_form=str2hex(password)
#ase=random.getrandbits(32)

#print time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(time.time()))


#print hex(ord('\n'))
#import random
#print random.getrandbits(10) 

#print atoi('401')
#
#a='W: Digest algorithm="SHA1-sess-v4",nonce="105823CE77005E6C1A91825249404B75",key="B2C28349959452251DF2D3C3C9C012D52F19B9AFBA7F38F62A258F631197C56B80CFEEDE4723F7D6A0623F418D3DBC7496AE9F31058BBD52A3F230497F9D1C48C8F12BF50EC2DEE3EBF84D89E5323EA033696B48110C6937F2DAF7B0B42D20CCFD3D947895BAD6C6E75F5F48782E64322438AA63745B5E306684F289975B8C49010001",signature="D4E7C0AF81C86CB9E96E21E3A90200B0F732167A2FFD7943E611EC52DE40C6122EB9888301B91E3DE9E9149B13AD15FCA99FCDB4A44BE6B2F3A02FA861FBDD3E3EC6A029038CA4A548648F6E3A6FD8A1528617468D3BC8B1BA6FCF750B70E23B772A398097704D7BF12B68498BA16DE598741B434C54DA57E71736609133E667"'
#rwParse = a.split(",")
#if 4 != len(rwParse):
#    print -3
#DigAlg = rwParse[0][rwParse[0].find('"')+1:-1]
#nonce = rwParse[1][rwParse[1].find('"')+1:-1]
#key = rwParse[2][rwParse[2].find('"')+1:-1]
#signature = rwParse[3][rwParse[3].find('"')+1:-1]
#
#print DigAlg
#print nonce
#print key
#print signature
#a=1
#k='<results><client public-ip="10.0.0.1" login-place="" last-login-ip="10.0.0.1" last-login-place="" last-login-time="Sat, 23 Mar 2013 09:51:21 GMT" current-login-time="Sat, 23 Mar 2013 09:56:25 GMT" /><user-info><personal version="377727428" register-email="" user-id="202251968" sid="585917501" mobile-no="13810686793" uri="sip:585917501@fetion.com.cn;p=4007" name="" nickname="九月飞鹰" gender="0" impresa="天下没有白吃的午餐" portrait-crc="1379761855" birth-date="1900-01-01" birthday-valid="1" carrier="CMCC" carrier-status="0" carrier-region="CN.bj.10." user-region="" global-permission="identity=0;phone=0;email=1;birthday=1;business=0;presence=1;contact=1;location=3;buddy=2;ivr=2;buddy-ex=0;show=0;" sms-online-status="0.0:0:0" save-xeno-msg="0" email-binding-status="1" email-binding-alias="" set-pwd-question="0" alv2-version="1" alv2-warn="0" dynamic-version="0" birthday-lunar="0"/><configs><config name="weather-city">-1</config><config name="directsms-rec">0</config><config name="weather-region"></config><config name="addbuddy-app-sms">0</config><config name="private-presence"></config><config name="permission-request">0</config><config name="sms-notify">0</config><config name="schedule-sms-receipt">1</config><config name="weather-ip">1</config><config name="rev-offlinefile-sms">1</config><config name="send-offlinefile-sms">1</config><config name="group-invite-config">1</config><config name="sms-nickname-config">0</config><config name="autoreply-config"></config><config name="syncto-shequ-config">0</config><config name="lastest-contact"></config><config name="weather-regionex"></config><config name="lastest-contactv5"></config><config name="common-contact"></config><config name="v5airbladder-status">0</config><config name="cctosms-config">0</config><config name="alv2-setwarn">0</config><config name="push-client"></config><config name="win8-push">0</config></configs><custom-config version="389397248">H4sIAKOOok8EAHRW7W6jOhB9lX2BKmBsMIqF1M+7kZq2Kl31Z0XDJEEX7Aib5vL2dzCQmJDNnzDnnPHM2MNg8UdDfa/kttg1dWYKJRNxm+cbJU22MW+1qg4m8cRihol0r47PmQFt1qB1tgOdbLNSg1hcYaz6o6gQy6rD4w/U7VrvElM3g37OiUdpoP5QKch8ELqIuG2MeodD2T7K7LuEfIw+w8W61VBuV/K+L0A/F9oMK16lbLIvcByy/5S5W9mUEGfzRZli247SGS72yvwL7ZfGNSQcK707ov8N8WlEiB/4RCyuKsRbDRrM1fSvUuIdKmXgHTYgzcgMDlcp8Zxp86x2hexOIfFJHDES+px7zGOEc7GYCsRQGJ7EOh3rnWDnw1nJHP6zDTRFxLOSO5SmYEwhx064AMXT4+ptNHAN1xRHyMwe6pvikPhi4Vjis39+gG3WlONWXYC4q+qnkBtYPSTdPp6N+8K0+B+JxfAk0kr3LXr4PLXiFBOpUYfOTls9lc1w8U+tmsNDoQ9l1q5VDl1hM6xX3U0FgykunCd+jkEuSIJpQgkbA7nrMiR6hekGATaYHgO55sh1xV3wJ+ikUbWxQHDWjNCosQVa5MY/qc7gaalWbvoeXMyQLu6rLAsJQ2ej0bpv7pwUfa41PIDJilI7A8lFxeBj80FzcWEPTWXNl8xmN4dWdmNcfIh2hbB5DQVab6cKF3Z12F9u/i4qbo9Z+ypXeTketwM45LqQDY7thLmCERx06aYGkGmGY3qylouL1+222+ohwpD8FJxqfqum1gm5EPWouGs0BnhqyrIPMsSdweJF9UfcT9zPPchOM8j/QqLTZE7PvK6zwl2sa/6JLZ6yH1UXZmy2hHg+DzlO+iXxCPN8ElD7xDgLY/sU8Yiy7ikMYp9FS+Q8Lw4DtgxCSqIgQJb6fsgCj5MlYyGlMQ3iJU7Fi1iituP95rvJ8wIP7hTxF052SjkNSIRrd78l831KWMx8y3UoJjRw6MeZH9HQcmHgU+5FZ67Ps+c4iUPq+MUs9uKei4I4DClncYT8uZaR4/iJYUEUUX6u2HLc96OAUkIwAW7jMcqJzZMhEnHebacXsfNeWI4Rj+P6jMaRF3V+NPJiv+fiOCQhCdCmfZ79rv8av3jUD6PAC/CUWBBGmCe3fvgdJGHo+bgs5QHu+MUGi8fqUNTj2Q9XFRfqLgnfBaQmM41O+m3y7BXhjIq0qA4lTJX4Ks9RXA3yHpmEnMF2OtwVtdl/QrlRFbxhHzsjYkaJ33h/UHX7rrIKv7Ef7cHO9Suo+NhDBXdZWSolX5qqk11CourfnC9p0/nCy8wX2DvZOBH+LhD3DcasoLY3HPwy618LnKrzy+r/AAAA//8AAAAAwAoAAA==</custom-config><contact-list version="416184351"><buddy-lists><buddy-list id="1" name="我的好友"/><buddy-list id="2" name="同学"/></buddy-lists><buddies><b i="201868472" u="sip:648815422@fetion.com.cn;p=4002" n="李森" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="201922116" u="sip:135714950@fetion.com.cn;p=4001" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202065654" u="sip:610425981@fetion.com.cn;p=4003" n="" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="202470919" u="sip:616507810@fetion.com.cn;p=4009" n="" l="1" f="0" r="1" o="1" p="identity=0;"/><b i="202501234" u="sip:656863788@fetion.com.cn;p=4009" n="贾国瑞" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="202521750" u="sip:587625625@fetion.com.cn;p=4011" n="方圆" l="" f="0" r="1" o="0" p="identity=1;"/><b i="202543028" u="sip:997714930@fetion.com.cn;p=4012" n="耿晓燕" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="202555529" u="sip:587280154@fetion.com.cn;p=4011" n="火鸡" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="202558569" u="sip:568912261@fetion.com.cn;p=4012" n="" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="202560171" u="sip:650500416@fetion.com.cn;p=4012" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="202578745" u="sip:642086221@fetion.com.cn;p=4012" n="杜涛" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="202639157" u="sip:588656639@fetion.com.cn;p=4011" n="卫磊" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202654821" u="sip:568912584@fetion.com.cn;p=4013" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202785998" u="sip:589419428@fetion.com.cn;p=4015" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202812660" u="sip:633082500@fetion.com.cn;p=4015" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202851746" u="sip:655312180@fetion.com.cn;p=4016" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202959097" u="sip:685867459@fetion.com.cn;p=4018" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="204492438" u="sip:775596758@fetion.com.cn;p=5007" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="204516900" u="sip:659041189@fetion.com.cn;p=5008" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="207589670" u="sip:394576726@fetion.com.cn;p=1104" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="208903240" u="sip:677205621@fetion.com.cn;p=1129" n="王海波" l="" f="0" r="1" o="0" p="identity=1;"/><b i="209200581" u="sip:977138948@fetion.com.cn;p=1426" n="" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="211213384" u="sip:636081819@fetion.com.cn;p=2612" n="" l="1" f="320798847" r="1" o="1" p="identity=1;"/><b i="254745003" u="sip:659477077@fetion.com.cn;p=7003" n="葛文谦2" l="" f="0" r="1" o="1" p="identity=1;"/><b i="254786663" u="sip:977896187@fetion.com.cn;p=7003" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="254822785" u="sip:705675029@fetion.com.cn;p=30015" n="张东亚" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="255009635" u="sip:722319990@fetion.com.cn;p=7011" n="梁宏峰" l="" f="0" r="1" o="0" p="identity=1;"/><b i="259183424" u="sip:532258129@fetion.com.cn;p=372" n="雷洁梅" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="310715386" u="sip:782155510@fetion.com.cn;p=7105" n="" l="" f="0" r="1" o="0" p="identity=0;"/><b i="326125535" u="sip:748138917@fetion.com.cn;p=2235" n="翁萍" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="354791840" u="tel:13621510441" n="" l="1" r="1" o="1" p="identity=1;"/><b i="364273345" u="sip:743945963@fetion.com.cn;p=5966" n="火鸡南宁" l="1" f="333813229" r="1" o="1" p="identity=1;"/><b i="411653082" u="sip:690998796@fetion.com.cn;p=9470" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="415158808" u="sip:760951328@fetion.com.cn;p=10692" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="417227025" u="sip:771395462@fetion.com.cn;p=7302" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="463152518" u="sip:677292017@fetion.com.cn;p=11" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="463919415" u="sip:759551374@fetion.com.cn;p=265" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="464967379" u="sip:585529347@fetion.com.cn;p=664" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="465039599" u="sip:636568270@fetion.com.cn;p=666" n="赵伟" l="1" f="0" r="0" o="0" p="identity=1;"/><b i="465254006" u="sip:586801485@fetion.com.cn;p=889" n="" l="" f="326999133" r="1" o="0" p="identity=1;"/><b i="489496509" u="sip:875391300@fetion.com.cn;p=903" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="511425951" u="sip:796573461@fetion.com.cn;p=2618" n="陈强" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="525048078" u="sip:357842884@fetion.com.cn;p=6616" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="536773389" u="sip:808978796@fetion.com.cn;p=4002" n="陈永超" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="540050552" u="tel:13724271487" n="" l="1" r="1" o="1" p="identity=1;"/><b i="556449439" u="tel:15018532503" n="" l="" r="1" o="0" p="identity=1;"/><b i="1158581661" u="sip:681545999@fetion.com.cn;p=4612" n="" l="" f="0" r="1" o="0" p="identity=1;"/></buddies><chat-friends></chat-friends><blacklist><k i="654130134" u="sip:909431676@fetion.com.cn;p=12507" n=""/><k i="202207688" u="sip:573953305@fetion.com.cn;p=4006" n=""/><k i="291033022" u="sip:745046325@fetion.com.cn;p=1204" n=""/><k i="261110642" u="sip:832549316@fetion.com.cn;p=1072" n=""/><k i="444078065" u="sip:916745067@fetion.com.cn;p=9510" n=""/><k i="451362259" u="sip:295887111@fetion.com.cn;p=1708" n=""/><k i="212897613" u="sip:639044651@fetion.com.cn;p=3080" n=""/><k i="463919344" u="sip:759549351@fetion.com.cn;p=265" n=""/><k i="725929521" u="sip:990281453@fetion.com.cn;p=10566" n=""/><k i="652025261" u="sip:905644176@fetion.com.cn;p=9410" n=""/><k i="284629783" u="sip:646553412@fetion.com.cn;p=185" n=""/><k i="472843692" u="sip:781405411@fetion.com.cn;p=9008" n=""/><k i="230112868" u="sip:838977941@fetion.com.cn;p=4214" n=""/><k i="330392439" u="sip:734776140@fetion.com.cn;p=7142" n=""/></blacklist></contact-list><score value="6577" level="10" level-score="6577"/><services><service id="2015"/><service id="99"/></services><quotas><quota-limit><limit name="max-buddies" value="500"/><limit name="max-groupadmin-count" value="4"/><limit name="max-joingroup-count" value="20"/></quota-limit><quota-frequency><frequency name="send-sms" day-limit="1000" day-count="0" month-limit="15000" month-count="0"/><frequency name="free-direct-sms" day-limit="0" day-count="0" month-limit="0" month-count="0"/></quota-frequency></quotas><capability-list basic-caps="1ffff" contact-caps="ffffff" extended-caps="7301fff" restricted-caps="0"><contact carrier="HK.OTHER" contact-caps="0" /><contact carrier="SGSH" contact-caps="857c08" /><contact carrier="" contact-caps="a57008" /><contact carrier="CMCC" contact-caps="ffffff" /><contact carrier="CT" contact-caps="e57c1c" /><contact carrier="CUCC" contact-caps="e57c1c" /><contact carrier="CMHK" contact-caps="9ffc9f" /><contact carrier="SGST" contact-caps="857c08" /><contact carrier="CMPAK" contact-caps="857c08" /></capability-list></user-info><credentials kernel="DBIOAAC2pYwazJPaDI9pRS3XioR6VHq2/RcuwA1miza/8HebW/KlBYupr+O5X9yf1eXXjbzE4gbLzDAowaziPIAFGQDZDNCg8QFCdEL+3NF8kjKxzK0BI3o1vR990sCIuxb2LHYAAA=="><credential domain="fetion.com.cn" c="CRIOAABt/D6w0ftgM0EGvK8YjRod9Zyni/slsCHywat0xQYXS+BhFsLMLG6XQ7vmFSd/qaQcg4z87dQU/eYiLCCB2T107Ui78RaxIsHKh+UMJ5+qqqwkAhsbW/UI2uhLUiN+2gcAAA=="/><credential domain="m161.com.cn" c="CBAOAADqltaQmCkygIt/Enmzn2YXBmSZcyYbpVdazPLVxfCbQ03WD+oUK4mmvREuS3d2gwIeBaHDUwTjKCPTmOw8tVtPmwBgNmAQLZDPtckdb7DCCw=="/><credential domain="www.ikuwa.cn" c="ChAOAACKJMWOk0Gy8JlSypiXKGdUeS4i/Pf/qLX+TGwiW5E5LzkaH1yF0ocDbdWWvDumOemfwv41AINuxiaGro3r5HuCbnwwpqaFvJpuaNf2qZWrIg=="/><credential domain="games.fetion.com.cn" c="CrIEAACZm+M2Xax5iVza/CUrgV8jrextVERlbsNuRPRsY5DoNm/jzC/e/sD2qr/ZncITqxBUQF1USOjYu6c1nZiEzvt0R8HOvkcE0xybNOPmIHOgacdiu0HSmBYmtt/UQzNbTH4AAA=="/><credential domain="turn.fetion.com.cn" c="CrAEAACDzU0tgy0RzV+1HlJ1LOkVj2OoQLCHOSMsOa5QwyOESzFntVtSo2Fos6qQPlt0XZiPRdwf/V50wE4td1OI1//wP8uKExvX0NEZwEoqGxu0eQ=="/><credential domain="pos.fetion.com.cn" c="CbAEAACmQHnOlhqXEQwAtBJ/iwcYAZP0eZ8mBOiIePJ5pwAKuzWMl4miiiTknDAqXKoM3np+6Uiy4rdQwfjoKmMqgZTRfKHDxZpnu1o31MPvYePz1Q=="/><credential domain="ent.fetion.com.cn" c="CLIEAADxi1PzkpuR+AP7aUh0bDPxtOBurqEUYJxj/6kWwMe4U1qBO8rYkuf7OR0ZH5x79WWk+Hl+mc31pTG2xzGujZpdYR/f9kdAiNoq5cmuDumrVROQ5ksYOQyJ6d31m+iZjo4AAA=="/><credential domain="mms.fetion.com.cn" c="CbAEAADottbaKil0lISOka0wNofzY/JTH1z9KbxPDu8Bgtr/iCz2H06p/AmosLOswdJqxPCAOR25COtvgww9FW+gYnKfua0UmfjLLByaCsJ3ux5jkw=="/><credential domain="cf.fetion.com.cn" c="CLIEAAApBpipXHJ0xicAhTYsftdDB3KxPGGXoR6YM0L+8zqYpzKryoqyZIIpIp47Tfi00Y8m/8TlTYsO5jnvrE8orb5AIG0gKCS353TWJXIdXwd2sexxcsktAUxr6UE9TfT0lmUAAA=="/><credential domain="shequ.10086.cn" c="CbIEAAAjnu2dytBtsHcuGXs9HUWGCy9PHXuSleYvhOOgTiUO525IHs2A6yV0xnMZ1hY732sCU+fktcqLYC6W1Ra6TuGhl7fGAbQGvmaPowyinuSS15wAQ+R7l/8A0Y1CEKC4Xj0AAA=="/><credential domain="webim.fetion.com.cn" c="CVICAADvrD6A4R2JKGbQ981CbJGV1uMhkMFj0sHhWfbnIDx/0AAIOHuXA2xG8PChhanTVrSf19RAH9V9bhk5KYBnzfP8d+/R9NU5auSDdxrubqxDME1wCxgEQkSn+BPSEy0vVncAAA=="/></credentials></results>'
#print len(k)


#a='<results><client public-ip="10.0.0.1" login-place="" last-login-ip="10.0.0.1" last-login-place="" last-login-time="Sat, 23 Mar 2013 14:43:51 GMT" current-login-time="Sat, 23 Mar 2013 14:44:50 GMT" /><user-info><personal version="377727428" register-email="" user-id="202251968" sid="585917501" mobile-no="13810686793" uri="sip:585917501@fetion.com.cn;p=4007" name="" nickname="九月飞鹰" gender="0" impresa="天下没有白吃的午餐" portrait-crc="1379761855" birth-date="1900-01-01" birthday-valid="1" carrier="CMCC" carrier-status="0" carrier-region="CN.bj.10." user-region="" global-permission="identity=0;phone=0;email=1;birthday=1;business=0;presence=1;contact=1;location=3;buddy=2;ivr=2;buddy-ex=0;show=0;" sms-online-status="0.0:0:0" save-xeno-msg="0" email-binding-status="1" email-binding-alias="" set-pwd-question="0" alv2-version="1" alv2-warn="0" dynamic-version="0" birthday-lunar="0"/><configs><config name="weather-city">-1</config><config name="directsms-rec">0</config><config name="weather-region"></config><config name="addbuddy-app-sms">0</config><config name="private-presence"></config><config name="permission-request">0</config><config name="sms-notify">0</config><config name="schedule-sms-receipt">1</config><config name="weather-ip">1</config><config name="rev-offlinefile-sms">1</config><config name="send-offlinefile-sms">1</config><config name="group-invite-config">1</config><config name="sms-nickname-config">0</config><config name="autoreply-config"></config><config name="syncto-shequ-config">0</config><config name="lastest-contact"></config><config name="weather-regionex"></config><config name="lastest-contactv5"></config><config name="common-contact"></config><config name="v5airbladder-status">0</config><config name="cctosms-config">0</config><config name="alv2-setwarn">0</config><config name="push-client"></config><config name="win8-push">0</config></configs><custom-config version="389397248">H4sIAKOOok8EAHRW7W6jOhB9lX2BKmBsMIqF1M+7kZq2Kl31Z0XDJEEX7Aib5vL2dzCQmJDNnzDnnPHM2MNg8UdDfa/kttg1dWYKJRNxm+cbJU22MW+1qg4m8cRihol0r47PmQFt1qB1tgOdbLNSg1hcYaz6o6gQy6rD4w/U7VrvElM3g37OiUdpoP5QKch8ELqIuG2MeodD2T7K7LuEfIw+w8W61VBuV/K+L0A/F9oMK16lbLIvcByy/5S5W9mUEGfzRZli247SGS72yvwL7ZfGNSQcK707ov8N8WlEiB/4RCyuKsRbDRrM1fSvUuIdKmXgHTYgzcgMDlcp8Zxp86x2hexOIfFJHDES+px7zGOEc7GYCsRQGJ7EOh3rnWDnw1nJHP6zDTRFxLOSO5SmYEwhx064AMXT4+ptNHAN1xRHyMwe6pvikPhi4Vjis39+gG3WlONWXYC4q+qnkBtYPSTdPp6N+8K0+B+JxfAk0kr3LXr4PLXiFBOpUYfOTls9lc1w8U+tmsNDoQ9l1q5VDl1hM6xX3U0FgykunCd+jkEuSIJpQgkbA7nrMiR6hekGATaYHgO55sh1xV3wJ+ikUbWxQHDWjNCosQVa5MY/qc7gaalWbvoeXMyQLu6rLAsJQ2ej0bpv7pwUfa41PIDJilI7A8lFxeBj80FzcWEPTWXNl8xmN4dWdmNcfIh2hbB5DQVab6cKF3Z12F9u/i4qbo9Z+ypXeTketwM45LqQDY7thLmCERx06aYGkGmGY3qylouL1+222+ohwpD8FJxqfqum1gm5EPWouGs0BnhqyrIPMsSdweJF9UfcT9zPPchOM8j/QqLTZE7PvK6zwl2sa/6JLZ6yH1UXZmy2hHg+DzlO+iXxCPN8ElD7xDgLY/sU8Yiy7ikMYp9FS+Q8Lw4DtgxCSqIgQJb6fsgCj5MlYyGlMQ3iJU7Fi1iituP95rvJ8wIP7hTxF052SjkNSIRrd78l831KWMx8y3UoJjRw6MeZH9HQcmHgU+5FZ67Ps+c4iUPq+MUs9uKei4I4DClncYT8uZaR4/iJYUEUUX6u2HLc96OAUkIwAW7jMcqJzZMhEnHebacXsfNeWI4Rj+P6jMaRF3V+NPJiv+fiOCQhCdCmfZ79rv8av3jUD6PAC/CUWBBGmCe3fvgdJGHo+bgs5QHu+MUGi8fqUNTj2Q9XFRfqLgnfBaQmM41O+m3y7BXhjIq0qA4lTJX4Ks9RXA3yHpmEnMF2OtwVtdl/QrlRFbxhHzsjYkaJ33h/UHX7rrIKv7Ef7cHO9Suo+NhDBXdZWSolX5qqk11CourfnC9p0/nCy8wX2DvZOBH+LhD3DcasoLY3HPwy618LnKrzy+r/AAAA//8AAAAAwAoAAA==</custom-config><contact-list version="416184351"><buddy-lists><buddy-list id="1" name="我的好友"/><buddy-list id="2" name="同学"/></buddy-lists><buddies><b i="201868472" u="sip:648815422@fetion.com.cn;p=4002" n="李森" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="201922116" u="sip:135714950@fetion.com.cn;p=4001" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202065654" u="sip:610425981@fetion.com.cn;p=4003" n="" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="202470919" u="sip:616507810@fetion.com.cn;p=4009" n="" l="1" f="0" r="1" o="1" p="identity=0;"/><b i="202501234" u="sip:656863788@fetion.com.cn;p=4009" n="贾国瑞" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="202521750" u="sip:587625625@fetion.com.cn;p=4011" n="方圆" l="" f="0" r="1" o="0" p="identity=1;"/><b i="202543028" u="sip:997714930@fetion.com.cn;p=4012" n="耿晓燕" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="202555529" u="sip:587280154@fetion.com.cn;p=4011" n="火鸡" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="202558569" u="sip:568912261@fetion.com.cn;p=4012" n="" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="202560171" u="sip:650500416@fetion.com.cn;p=4012" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="202578745" u="sip:642086221@fetion.com.cn;p=4012" n="杜涛" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="202639157" u="sip:588656639@fetion.com.cn;p=4011" n="卫磊" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202654821" u="sip:568912584@fetion.com.cn;p=4013" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202785998" u="sip:589419428@fetion.com.cn;p=4015" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202812660" u="sip:633082500@fetion.com.cn;p=4015" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202851746" u="sip:655312180@fetion.com.cn;p=4016" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="202959097" u="sip:685867459@fetion.com.cn;p=4018" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="204492438" u="sip:775596758@fetion.com.cn;p=5007" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="204516900" u="sip:659041189@fetion.com.cn;p=5008" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="207589670" u="sip:394576726@fetion.com.cn;p=1104" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="208903240" u="sip:677205621@fetion.com.cn;p=1129" n="王海波" l="" f="0" r="1" o="0" p="identity=1;"/><b i="209200581" u="sip:977138948@fetion.com.cn;p=1426" n="" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="211213384" u="sip:636081819@fetion.com.cn;p=2612" n="" l="1" f="320798847" r="1" o="1" p="identity=1;"/><b i="254745003" u="sip:659477077@fetion.com.cn;p=7003" n="葛文谦2" l="" f="0" r="1" o="1" p="identity=1;"/><b i="254786663" u="sip:977896187@fetion.com.cn;p=7003" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="254822785" u="sip:705675029@fetion.com.cn;p=30015" n="张东亚" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="255009635" u="sip:722319990@fetion.com.cn;p=7011" n="梁宏峰" l="" f="0" r="1" o="0" p="identity=1;"/><b i="259183424" u="sip:532258129@fetion.com.cn;p=372" n="雷洁梅" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="310715386" u="sip:782155510@fetion.com.cn;p=7105" n="" l="" f="0" r="1" o="0" p="identity=0;"/><b i="326125535" u="sip:748138917@fetion.com.cn;p=2235" n="翁萍" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="354791840" u="tel:13621510441" n="" l="1" r="1" o="1" p="identity=1;"/><b i="364273345" u="sip:743945963@fetion.com.cn;p=5966" n="火鸡南宁" l="1" f="333813229" r="1" o="1" p="identity=1;"/><b i="411653082" u="sip:690998796@fetion.com.cn;p=9470" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="415158808" u="sip:760951328@fetion.com.cn;p=10692" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="417227025" u="sip:771395462@fetion.com.cn;p=7302" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="463152518" u="sip:677292017@fetion.com.cn;p=11" n="" l="" f="0" r="1" o="1" p="identity=1;"/><b i="463919415" u="sip:759551374@fetion.com.cn;p=265" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="464967379" u="sip:585529347@fetion.com.cn;p=664" n="" l="1" f="0" r="1" o="1" p="identity=1;"/><b i="465039599" u="sip:636568270@fetion.com.cn;p=666" n="赵伟" l="1" f="0" r="0" o="0" p="identity=1;"/><b i="465254006" u="sip:586801485@fetion.com.cn;p=889" n="" l="" f="326999133" r="1" o="0" p="identity=1;"/><b i="489496509" u="sip:875391300@fetion.com.cn;p=903" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="511425951" u="sip:796573461@fetion.com.cn;p=2618" n="陈强" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="525048078" u="sip:357842884@fetion.com.cn;p=6616" n="" l="" f="0" r="1" o="0" p="identity=1;"/><b i="536773389" u="sip:808978796@fetion.com.cn;p=4002" n="陈永超" l="1" f="0" r="1" o="0" p="identity=1;"/><b i="540050552" u="tel:13724271487" n="" l="1" r="1" o="1" p="identity=1;"/><b i="556449439" u="tel:15018532503" n="" l="" r="1" o="0" p="identity=1;"/><b i="1158581661" u="sip:681545999@fetion.com.cn;p=4612" n="" l="" f="0" r="1" o="0" p="identity=1;"/></buddies><chat-friends></chat-friends><blacklist><k i="654130134" u="sip:909431676@fetion.com.cn;p=12507" n=""/><k i="202207688" u="sip:573953305@fetion.com.cn;p=4006" n=""/><k i="291033022" u="sip:745046325@fetion.com.cn;p=1204" n=""/><k i="261110642" u="sip:832549316@fetion.com.cn;p=1072" n=""/><k i="444078065" u="sip:916745067@fetion.com.cn;p=9510" n=""/><k i="451362259" u="sip:295887111@fetion.com.cn;p=1708" n=""/><k i="212897613" u="sip:639044651@fetion.com.cn;p=3080" n=""/><k i="463919344" u="sip:759549351@fetion.com.cn;p=265" n=""/><k i="725929521" u="sip:990281453@fetion.com.cn;p=10566" n=""/><k i="652025261" u="sip:905644176@fetion.com.cn;p=9410" n=""/><k i="284629783" u="sip:646553412@fetion.com.cn;p=185" n=""/><k i="472843692" u="sip:781405411@fetion.com.cn;p=9008" n=""/><k i="230112868" u="sip:838977941@fetion.com.cn;p=4214" n=""/><k i="330392439" u="sip:734776140@fetion.com.cn;p=7142" n=""/></blacklist></contact-list><score value="6577" level="10" level-score="6577"/><services><service id="2015"/><service id="99"/></services><quotas><quota-limit><limit name="max-buddies" value="500"/><limit name="max-groupadmin-count" value="4"/><limit name="max-joingroup-count" value="20"/></quota-limit><quota-frequency><frequency name="send-sms" day-limit="1000" day-count="0" month-limit="15000" month-count="0"/><frequency name="free-direct-sms" day-limit="0" day-count="0" month-limit="0" month-count="0"/></quota-frequency></quotas><capability-list basic-caps="1ffff" contact-caps="ffffff" extended-caps="7301fff" restricted-caps="0"><contact carrier="SGSH" contact-caps="857c08" /><contact carrier="HK.OTHER" contact-caps="0" /><contact carrier="CT" contact-caps="e57c1c" /><contact carrier="CMCC" contact-caps="ffffff" /><contact carrier="" contact-caps="a57008" /><contact carrier="CUCC" contact-caps="e57c1c" /><contact carrier="CMHK" contact-caps="9ffc9f" /><contact carrier="SGST" contact-caps="857c08" /><contact carrier="CMPAK" contact-caps="857c08" /></capability-list></user-info><credentials kernel="DRIOAADbuCG/ULPHp6kL35pzGsUQWyT0JDk87wqpw4x00BYbC7R9uxMI+45LSU1e3iVYTH4/gFwLvpCVB2bocGnJdmFsV08qsyRAlQO3WRy6tfGZNThj0+3idN6X9S8I6OPti6EAAA=="><credential domain="fetion.com.cn" c="ChIOAABd7u6l4aa9KRvnXB4X6J9sFnD8zlylU91ZsT1KzxuD5AhJhUApidMOzJcCv9NPTpkI57HA60ZtT1+Q2hzh24dNy+cnBihonUtzc1Z1mZbDIKRAxyiG9Sv8yncIW38vTyAAAA=="/><credential domain="m161.com.cn" c="CBAOAAA1Qi+6LDSM8bWmhCKNn5zgcMnjdKzCRunmHtz23k7Aipo/fzvfGCneFe3Pojluwgiheep9U6e0d1Cpauo6n9E7Pmq95UG3u5pckS5cV95+oQ=="/><credential domain="www.ikuwa.cn" c="ChAOAACqtt7FHQeAu9AkXY8tECKCdHepbHg/ePqStK9NdDXY7PNqBrK0yLLUatBkac2Sg2Dk4Uso7MPaZvhvhXVd5mBDD/16qzf757JImCngF1tsoA=="/><credential domain="games.fetion.com.cn" c="CLIEAAC/BRUSVTN+ncaPXAANEgPqP1Kh75/ijh/gvEiS5+f86A1hlcXZjdwFoF7B0wDG/QcqagZFdOJc9Q2DRWg7jWHsw8kxMQdouGJcTM3HLSfDW8ABBi4JKY/3MMdr1sLxxXAAAA=="/><credential domain="turn.fetion.com.cn" c="CrAEAAAdJIXNlbCNSqzSi6GE4eqcK9mgK/mrd+PeGGWGYUQvc6hdck51oZnsK6i6HNnqoGj8LpKwQyW9gtREG21TJpXLtpjn8doyhokvKc8J6fNbOQ=="/><credential domain="pos.fetion.com.cn" c="CbAEAACIlnUwMdlQxy8hvcoPnDe/rCIiQpl+SvvSWfKS5xfYdg2SKIl2T07mPK0jjsixIvGfPHy87PehJN5cIq76A8rczfTVcViJVn/5RNktMgTTRg=="/><credential domain="ent.fetion.com.cn" c="CLIEAAD9LmheX/CptstoRJ2cf78XGBflmmJJ7zj/pb7qg9dmg9rMZml4AI+tT3h2930eWT2zbi1uKsQEhlb5WcV5cCkIMc8H9TblSumVI6vM2CEp/A1zNi3uc+btys/x+1eIqhAAAA=="/><credential domain="mms.fetion.com.cn" c="CbAEAADQJwV138Rryd14f0fMl0w17NothR1GPju/DiNjGm+ZYsNg2X62sQW+Esqc4j4vSopZyldleDafduCGC5y4SJdXjH61KvrkK6iU2NmSrewv0A=="/><credential domain="cf.fetion.com.cn" c="CLIEAADmL8BVRvj4MdvXmjpLZWNgIuxNDnRGbO5bOinFcewwCZTGhpODe4YXXM6pPS1401IhIfBnw95sLSSsgc2Ze0JaG/ppkYurg+fAiY1hzmWJW0W+b6seHXmzIqwSkZkfWXMAAA=="/><credential domain="shequ.10086.cn" c="CbIEAACEu3m1hWQBDqv/Vg/bnsEjTQ+u4GpESDBM9bqFEJhdrsJlIf8aJTBnYsMg25heR4YGZ5WcEZxVMRsw5AfJi2SdBwKzg3nachD0K9gb2W/X+5fSYbNwFnu5F9k8drgsggwAAA=="/><credential domain="webim.fetion.com.cn" c="ClICAADHk4VwjK3aEPetGa3R5fcTNogbSFjwqyhSZ7CZ0RThiO79NG95vZ8Z5L7Dtjff+rtLCcTfz2n40KBNMHZMzqYIgb5O7va2FQRjOdha0nTNoJ340Pvkk/j0PbuKL63MWJkAAA=="/></credentials></results>'
#root=ElementTree.fromstring(a)
#buddiesNode=root.find('user-info/contact-list/buddies')
#if None == buddiesNode:
#    print 'None 1'
#else:
#    print 'find'
#    buddies = buddiesNode.findall('b')
#    for buddy in buddies:
#        nikename = buddy.get('n', 'another')
#        userid = buddy.get('i')
#        sip = buddy.get('u')
#        
#        print 'nikename is %s, useris is %s sip is %s' % (nikename, userid, sip) 
a='M fetion.com.cn SIP-C/4.0\
F: 585917501\
I: 64\
Q: 1 M\r\n\
T: sip:681545999@fetion.com.cn;p=4612\
K: SaveHistory\
K: NewEmotion\
N: CatMsg\
C: text/plain\
L: 4\
shit'
#print hashlib.sha1(a).hexdigest()
a='123'
print len(a)

#data1='SIP-C/4.0 200 OK..I: 32..Q: 1 S..L: 583\r\n\r\n<results><contact uri="sip:642086221@fetion.com.cn;p=4012" version="0" user-id="202578745" sid="642086221" basic-service-status="1" mobile-no="13811181235" carrier="CMCC" carrier-status="0" portrait-crc="841039497" name="" nickname="Mourinho" gender="2" birth-date="1899-12-31" birthday-valid="0" birthday-lunar="0" age="113" lunar-animal="0" horoscope="0" impresa="" carrier-region="CN.bj.10." user-region="" personal-email="" work-email="" other-email="" primary-email="0" email-binding-alias="642086221" profile="" blood-type="0" occupation="" hobby="" score-level="7"/></results>'
#data2='111SIP-C/4.0 200 OK..I: 32..Q: 1 S..L: 583\r\n\r\n<results><contact uri="sip:642086221@fetion.com.cn;p=4012" version="0" user-id="202578745" sid="642086221" basic-service-status="1" mobile-no="13811181235" carrier="CMCC" carrier-status="0" portrait-crc="841039497" name="" nickname="Mourinho" gender="2" birth-date="1899-12-31" birthday-valid="0" birthday-lunar="0" age="113" lunar-animal="0" horoscope="0" impresa="" carrier-region="CN.bj.10." user-region="" personal-email="" work-email="" other-email="" primary-email="0" email-binding-alias="642086221" profile="" blood-type="0" occupation="" hobby="" score-level="7"/></results>222'
#data3='111SIP-C/4.0 200 OK..I: 32..Q: 1 S..L: 583\r\n\r\n<results><contact uri="sip:642086221@fetion.com.cn;p=4012" version="0" user-id="202578745" sid="642086221" basic-service-status="1" mobile-no="13811181235" carrier="CMCC" carrier-status="0" portrait-crc="841039497" name="" nickname="Mourinho" gender="2" birth-date="1899-12-31" birthday-valid="0" birthday-lunar="0" age="113" lunar-animal="0" horoscope="0" impresa="" carrier-region="CN.bj.10." user-region="" personal-email="" work-email="" other-email="" primary-email="0" email-binding-alias="642086221" profile="" blood-type="0" occupation=""'
#data4='SIP-C/4.0 200 OK..I: 32..Q: 1 S..L: 583\r\n\r\n<results><contact uri="sip:642086221@fetion.com.cn;p=4012" version="0" user-id="202578745" sid="642086221" basic-service-status="1" mobile-no="13811181235" carrier="CMCC" carrier-status="0" portrait-crc="841039497" name="" nickname="Mourinho" gender="2" birth-date="1899-12-31" birthday-valid="0" birthday-lunar="0" age="113" lunar-animal="0" horoscope="0" impresa="" carrier-region="CN.bj.10." user-region="" personal-email="" work-email="" other-email="" primary-email="0" email-binding-alias="642086221" profile="" blood-type="0" occupation="" hobby="" score-level="7"/></results>SIP-C/4.0 200 OK..I: 32..Q: 1 S..L: 583\r\n\r\n<results><contact uri="sip:642086221@fetion.com.cn;p=4012" version="0" user-id="202578745" sid="642086221" basic-service-status="1" mobile-no="13811181235" carrier="CMCC" carrier-status="0" portrait-crc="841039497" name="" nickname="Mourinho" gender="2" birth-date="1899-12-31" birthday-valid="0" birthday-lunar="0" age="113" lunar-animal="0" horoscope="0" impresa="" carrier-region="CN.bj.10." user-region="" personal-email="" work-email="" other-email="" primary-email="0" email-binding-alias="642086221" profile="" blood-type="0" occupation="" hobby="" score-level="7"/></results>'
#data5='SIP-C/4.0 200 OK..I: 32..Q: 1 S..L: 583\r\n\r\n'
#data6='SIP-C/4.0 200 OK..I: 32..Q: 1 S..\r\n\r\n'
#
#    
#r1, r2 = divPacket(data6)
#for result in r1:
#    print result
#
#print '---'
#print r2

class MsgHead:
    def __init__(self):
        self.R=''
        self.S=''
        self.M=''
        self.O=''
        self.F=''
        self.I=''
        self.Q=''
        self.T=''
        self.A=''
        self.C=''
        self.N=''
        self.L=''
        self.CN=''
        self.CL=''
    def erase(self):
        self.R=''
        self.S=''
        self.M=''
        self.O=''
        self.F=''
        self.I=''
        self.Q=''
        self.T=''
        self.A=''
        self.C=''
        self.N=''
        self.L=''
        self.CN=''
        self.CL=''        
    def constructMsgHead(self):
        msgHead=''
        if '' != self.R:
            msgHead += 'R '+self.R+'\r\n'
        if '' != self.S:
            msgHead += 'S '+self.S+'\r\n'
        if '' != self.M:
            msgHead += 'M '+self.M+'\r\n'  
        if '' != self.O:
            msgHead += 'O '+self.O+'\r\n'                               
        if '' != self.F:
            msgHead += 'F: '+self.F+'\r\n'
        if '' != self.I:
            msgHead += 'I: '+self.I+' \r\n'     
        if '' != self.Q:
            msgHead += 'Q: '+self.Q+'\r\n' 
        if '' != self.T:
            msgHead += 'T: '+self.T+'\r\n'                                
        if '' != self.A:
            msgHead += 'A: '+head.A+'\r\n' 
        if '' != self.C:
            msgHead += 'C: '+self.C+'\r\n'
        if '' != self.N:
            msgHead += 'N: '+self.N+'\r\n'                
        if '' != self.L:
            msgHead += 'L: '+str(self.L)+'\r\n' 
        if '' != self.CN:
            msgHead += 'CN: '+self.CN+'\r\n'
        if '' != self.CL:
            msgHead += 'CL: '+self.CL+'\r\n'                

        msgHead += '\r\n' #head和body之间有两个\r\n
        return msgHead
    
msg1='SIP-C/4.0 200 OK\r\nI: 32\r\nQ: 1 S\r\nL: 583\r\n\r\n<results><contact uri="sip:642086221@fetion.com.cn;p=4012" version="0" user-id="202578745" sid="642086221" basic-service-status="1" mobile-no="13811181235" carrier="CMCC" carrier-status="0" portrait-crc="841039497" name="" nickname="Mourinho" gender="2" birth-date="1899-12-31" birthday-valid="0" birthday-lunar="0" age="113" lunar-animal="0" horoscope="0" impresa="" carrier-region="CN.bj.10." user-region="" personal-email="" work-email="" other-email="" primary-email="0" email-binding-alias="642086221" profile="" blood-type="0" occupation="" hobby="" score-level="7"/></results>'
msg2='SIP-C/4.0 200 OK\r\nI: 32\r\nQ: 1 S\r\n\r\n'
def preParseMsg(msg):
    msgHead = MsgHead()
    body=''
    result = msg.split('\r\n')
    if len(result) < 1:
        return (-1, -1, None, None)
    statusCode = result[0].split(' ')[1]
    statusInfo = result[0][result[0].find(statusCode)+len(statusCode)+1:]
    result.pop(0)
    msgHead.I=str(32)
    for line in result:
        if '' == line:
            continue
        if '<' == line[0]:
            body = line
            break
        exec('msgHead.%s="%s"' % (line[0], line[3:]))
    return (statusCode, statusInfo, msgHead, body)

statusCode, statusInfo, msgHead, body = preParseMsg(msg1)
print statusCode
print statusInfo
print msgHead
print body






              