#encoding=utf-8
import httplib,urllib
#第一步获取nav.fetion.com.cn的信息
#url = 'http://nav.fetion.com.cn/nav/getsystemconfig.aspx?NewType=0'
#
#headers={"Accept":"*/*","User-Agent":"IIC2.0/PC 4.7.0800",
#         "Content-Type":"application/oct-stream",
#         "Connection":"Keep-Alive",
#         "Cache-Control":"no-cache"}
#
#params='<config><user mobile-no="13910000000" /><client type="PC" version="4.7.0800" platform="W6.1" />\
#<servers version="0" /><service-no version="0" /><parameters version="0" /><hints version="0" />\
#<http-applications version="0" /><client-config version="0" /><banners version="0" /><config-url version="0" /><services version="0" /></config>'
#conn=httplib.HTTPConnection("nav.fetion.com.cn")
#conn.request(method="POST", url='/nav/getsystemconfig.aspx?NewType=0', body=params, headers=headers)
#response=conn.getresponse()
#
#if 200 == response.status:
#    result=response.read()
#    print result
#response.close()

#/ssiportal/SSIAppSignInV4.aspx?mobileno=138********
#&domains=
#&v4digest-type=2
#&v4digest=941a575e33318ddc1dc1da4d882ca3a2025744f7
#&userid=**** 
#
#url = 'http://nav.fetion.com.cn/nav/getsystemconfig.aspx?NewType=0'
#
#headers={"Accept":"*/*",
#         "User-Agent":"IIC2.0/PC 4.7.0800",
#         "Connection":"Keep-Alive",
#         "Cache-Control":"no-cache"}
#domains='fetion.com.cn%3bm161.com.cn%3bwww.ikuwa.cn%3bgames.fetion.com.cn%3bturn.fetion.com.cn%3bpos.fetion.com.cn%3bent.fetion.com.cn%3bmms.fetion.com.cn%3bcf.fetion.com.cn%3bshequ.10086.cn%3bwebim.fetion.com.cn'
#
#params=urllib.urlencode({"mobileno":"13810686793",
#                         "domains":domains,
#                         "v4digest-type":'1'
#                         "v4digest":})
#conn=httplib.HTTPConnection("nav.fetion.com.cn")
#conn.request(method="POST", url='/nav/getsystemconfig.aspx?NewType=0', body=params, headers=headers)
#response=conn.getresponse()
#
#if 200 == response.status:
#    result=response.read()
#    print result
#response.close()

import binascii  
  
bin = lambda n:(n > 0) and (bin(n/2) + str(n%2)) or ''  
  
s = 'hello world,this is python'  
s_16 = binascii.b2a_hex(s) 
s_10 = int(s_16,16)  
s_2 = bin(s_10)  
print s_16  
  
s_10 = int(s_2,2)  
s_16 = '%x'%(s_10)  
s = binascii.a2b_hex(s_16)  
print s  


