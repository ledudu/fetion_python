#encoding=utf-8
import struct
import httplib
import urllib
from hashlib import md5
from hashlib import sha1
from xml.etree import ElementTree
import exceptions
from locale import atoi
from binascii import a2b_hex,b2a_hex
import socket
from select import select
import random
import recv_send
import threading
from threading import Timer
from mailcap import findmatch

FetionOnline = "400"
FetionBusy   = "600"
FetionAway   = "100"
FetionHidden  = "0"
FetionOffline = "365"

#__debug__ = True

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    import random
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str
    
def random_hexstr(randomlength=8):
    str = ''
    chars = 'abcdef0123456789'
    length = len(chars) - 1
    import random
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str
    
class SSICertification:
    SSIServer='uid.fetion.com.cn'
    SSIUrl='/ssiportal/SSIAppSignInV4.aspx'
    domains='fetion.com.cn%3bm161.com.cn%3bwww.ikuwa.cn%3bgames.fetion.com.cn%3bturn.fetion.com.cn%3bpos.fetion.com.cn%3bent.fetion.com.cn%3bmms.fetion.com.cn%3bcf.fetion.com.cn%3bshequ.10086.cn%3bwebim.fetion.com.cn'
    def __init__(self, user):
        self.user=user
        self.v1Digest=''
        self.v2Digest=''
        self.ssic=''
        self.status_code = 0

    @staticmethod
    def GetV4Digest1_Static(password):
        return sha1("fetion.com.cn:"+password).hexdigest()

    def getV4digest1(self):
        if '' == self.v1Digest:
            self.v1Digest = SSICertification.GetV4Digest1_Static(self.user.password)
        return self.v1Digest

    @staticmethod
    def GetV4Digest2_Static(userid, password):
        if ('' == userid or '' == password):
            return ''        
        V1Digest = SSICertification.GetV4Digest1_Static(password)
        return sha1(struct.pack('i', atoi(userid)) + a2b_hex(V1Digest)).hexdigest()

    def getV4digest2(self):
        if '' == self.v2Digest:
            self.v2Digest = SSICertification.GetV4Digest2_Static(self.user.userid, self.user.password)
        return self.v2Digest
 
    def ssiParse(self, response):
        try:
            body=response.read()
            #get the result code 
            root = ElementTree.fromstring(body)
            if 'results' == root.tag:
                self.status_code = root.get('status-code')
            else:
                node = root.find('results')
                if Node != node:
                    self.status_code = node.get('status-code')

            if '200' == self.status_code:
                node = root.find("user")
                if None != node:
                    self.user.spi = node.get('uri')
                    self.user.userid = node.get('user-id')
            else:    #如果这里返回的不是200，暂时没有处理，认为有问题直接返回先
                return self.status_code
            #get the ssic
            ssic_get = response.getheader('Set-Cookie', '')
            if '' != ssic_get:
                index=ssic_get.index('; path=/')
                self.user.ssic = ssic_get[len('ssic='):index]
        except Exception,e:
            print e       
        return self.status_code
                                   
    def ssiV1Certify(self):
        if '' != self.v1Digest:
            return
        #send the V1Digest
        headers={"Accept":"*/*",
                 "User-Agent":"IIC2.0/PC 4.0.0000",
                 "Connection":"Keep-Alive",
                 "Cache-Control":"no-cache"}        

        conn=httplib.HTTPConnection(self.SSIServer)
        gURL=self.SSIUrl+'?mobileno='+self.user.mobileno+'&domains='+self.domains+'&v4digest-type='+'1'+'&v4digest='+self.getV4digest1()
        try:
            conn.request(method='GET', url=gURL, headers=headers)
            response=conn.getresponse()
            #V1 and V2 have the same return
            self.ssiParse(response)
        except Exception,e:
            print e
        finally:
            conn.close()
        return
    
    def ssiV2Certify(self):
        if '' != self.v2Digest:
            return
        #send the V2Digest
        headers={"Accept":"*/*",
                 "User-Agent":"IIC2.0/PC 4.0.0000",
                 "Connection":"Keep-Alive",
                 "Cache-Control":"no-cache"}        

        conn=httplib.HTTPConnection(self.SSIServer)
        gURL=self.SSIUrl+'?mobileno='+self.user.mobileno+'&domains='+self.domains+'&v4digest-type='+'2'+'&v4digest='+self.getV4digest2()
        try:
            conn.request(method='GET', url=gURL, headers=headers)
            response=conn.getresponse()
            print response.read()
            #V1 and V2 have the same return
            self.ssiParse(response)
        except Exception,e:
            print e
        finally:
            conn.close()
        return
                            
    def ssiCertify(self):
        if '' == self.ssic:
            #default https is used, but use http is also ok
            self.ssiV1Certify()
            self.ssiV2Certify()
        return self.ssic
    
    def getSSIC(self):
        return self.ssic

#define the SPIC message header
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
            
class Friend:
    localName=''
    nickName=''
    userid=''
    sip=''

#起一个进程，定时发送保活报文            
class SIPCKAThread(threading.Thread):
    #默认30s发一个KA报文
    def __init(self, socket, sipc, time=30):
        self.__socket = socket
        self.__time = time
        self.__sipc = sipc
        self.__stop = False
        threading.Thread.__init__(self)
        
    def run(self):
        while False == self.__stop:
            nextI = sipc.getNextI()
            head=MsgHead()
            head.O = 'fetion.com.cn SIP-C/4.0'
            head.F = ''
            head.I = str(self.__sipc.getNextI())
            head.Q = '1 O'
            head.N = 'KeepConnectionBusy'
            msg = head.constructMsgHead()
            sipc.sendMsg(socket, msg, head.I, head.N)
            time.sleep(time)
        
    def stop(self):
        self.__stop = True
        
class SIPC:            
    __timeout=5
    __ERR_PACKET = -1
    
    __ERR_PASSWORD = 401
    __SUCCESS = 200
    __ERR_NEED_PICVERIFY = 521
    
    __INITIAL = 0
    __NORMAL = 1
    __WAIT_SIPC_VERIFY1 = 2
    __WAIT_SIPC_VERIFY2 = 3
    __WAIT_SIPC_CONTACTDETAIL = 4
    
    ILock = threading.Lock()
    def __init__(self, user):
        self.spicProxy='115.181.16.78:8080'
        self.defaultR = 'fetion.com.cn SIP-C/4.0'
        self.defaultCL = 'type="pc",version="4.7.0800"'
        #mobileno, userid and presece need to be filled
        self.defaultLoginXML = '<args><device accept-language="default" machine-code="2DE4EC48822405CF4A1CB7C4834432F3" opmsg-version="0" /><caps value="BF9FFF" /><events value="7F" /><user-info mobile-no="%s" user-id="%s"><personal version="0" attributes="v4default;alv2-version;alv2-warn;dynamic-version;restricted;birthday-lunar;lunar-animal;horoscope;age" /><custom-config version="0" /><contact-list version="0" buddy-attributes="v4default" /></user-info><credentials domains="fetion.com.cn;m161.com.cn;www.ikuwa.cn;games.fetion.com.cn;turn.fetion.com.cn;pos.fetion.com.cn;ent.fetion.com.cn;mms.fetion.com.cn;cf.fetion.com.cn;shequ.10086.cn;webim.fetion.com.cn" /><presence><basic value="%s" desc="" /><extendeds /></presence><login type="0" retry="0" /></args>'    
        #userid and sip url need to be filled
        self.defGetFrdDetail = '<args><contact user-id="%s" uri="%s" version="0" /></args>'
        self.__sock=None
        self.__user=user
        #self.   #default recv timeout is set to 5
        self.__dataRecv=list()
        self.__DigAlg = ''
        self.__nonce = ''
        self.__key = ''
        self.__signature = ''
        self.__curStausCode=0
        self.__state=self.__INITIAL
        self.__curI = 1
        self.__sendedMsg = dict()
        
    def __del__(self):
        if None != self.__sock:
            self.__sock.close()
                
    def initSock(self):
        if None != self.__sock:
            return self.__sock
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        (host, port)=tuple(self.spicProxy.split(':'))
        try:
            self.__sock.connect((host,int(port)))
        except socket.error, e:
            self.__sock.close()
            self.__sock = None
            print "socket connect error in spic"
        return self.__sock
    
    #这里只处理发一个报文然后等着回一个报文的情况。这里一般使用阻塞，如果会回多个报文之类的，这里判断response可能就不准了
    #但是收全第一个报文应该是没有问题的，这个只是在登录的时候使用，在登录以后，后面报文的首发都使用任务来进行处理
    def sendMsgWaitResponse(self, head, body, timeout=__timeout):
        datalen=0
        recvOnce=1024
        data=''
        readOver = False
        
        if None == self.__sock:
            initSock()
        msgHead=head.constructMsgHead()
        msg=msgHead+body
        print 'msgsend'+msg
        
        self.__sock.send(msg)
        if timeout:
            while False == readOver:
                infd,outfd,errfd=select([self.__sock], [], [], timeout)
                if 0 != len(infd):
                    data+=self.__sock.recv(recvOnce)
                    infd,outfd,errfd=select([self.__sock], [], [], 0)
                    while 0 != len(infd): #这里先把报文收全了
                        data+=self.__sock.recv(recvOnce)
                        infd,outfd,errfd=select([self.__sock], [], [], 0)                    
                    #SPIC回应的部份报文以'\r\n\r\n'作为结束，其他只能靠select的超时了。
                    timeout=1 #如果已经开始收到回应的报文，那么可以认为后面报文的收到时间也不会差太多，这里把等待时间调小一些，减小阻塞
                    if '\r\n\r\n' == data[-4:]:
                        print "readOver"
                        readOver = True
                    elif '</results>' == data[-10:]:    #一些类是获取通讯录信息的回应报文是以</result>结尾的
                        readOver = True
                else:
                    break
        print 'len=%d' % len(data)
        return data    

    
    #解析SPIC的回复报文，如果返回负值表示回复的报文有误，为正数表示的是状态值,-1~-10表示报文错误
    #这里只实时处理注册时的报文
    def parseResponse(self, response):
        result=response.split('\r\n')
        if len(result) < 0:
            return -1
        
        statusCode = result[0].split(' ')[1]    #收到回复报文的第一行形如SIP-C/4.0 200 OK
        if '200' == statusCode:   #认证成功，下面对内容进行解析
            #print 'come here'
            if self.__WAIT_SIPC_VERIFY2 == self.__state: #认证时报文
                #这里只解析第一个报文，
                if len(result) <= 5:
                    print 'the result len is err:'+str(len(result))+'and the result is:'+result
                    return -2
                #第六个就是第一个报文返回的XML格式的内容
                root = ElementTree.fromstring(result[6][-1*len('BN 585917501 SIP-C/4.0'):])
                buddiesNode=root.find('user-info/contact-list/buddies')
                if None == buddiesNode:
                    print 'None 1'
                else:
                    #将联系人列表中的结果存入到user的friends中
                    #如果之前已经有了该联系人，那么只有数据有更新的时候才更新上去
                    buddies = buddiesNode.findall('b')
                    for buddy in buddies:
                        newFriend = Friend()
                        newFriend.localName = buddy.get('n', 'another')
                        newFriend.userid = buddy.get('i')
                        newFriend.sip = buddy.get('u')
                        #todo 这里还需要将用户的状态添加上去，如果用户已经退出飞信了，至少应该把这个状态给标记下来
                        oldFriend = self.__user.friends.get(newFriend.userid)
                        #print 'nikename is %s, useris is %s sip is %s' % (nikename, userid, sip)
                        if None == oldFriend:                           
                            self.__user.friends[newFriend.userid] = newFriend
                        if newFriend.localName != oldFriend.localName:
                            oldFriend.localName = newFriend.localName
                            self.__user.friends.update({newFriend.userid, oldFriend})
        
        if '401' == statusCode:    #第一次认真的时候必然会返回这个，因为此次主要是为了获取nonce等值，服务端可能就认为是没有输入正确的密码
            if self.__WAIT_SIPC_VERIFY1 == self.__state:
                if (len(result) < 4):
                    print 'the result len is err:'+str(len(result))+'and the result is:'+result
                    return -2
                rW = result[4]
                rwParse = rW[3:].split(',') #得到Digest algorithm, nonce,key和signature
                if 4 != len(rwParse):
                    print 'the nonce return is err, and the return result is '+rwParse
                    return -3
                self.__DigAlg = rwParse[0][rwParse[0].find('"')+1:-1]
                self.__nonce = rwParse[1][rwParse[1].find('"')+1:-1]
                self.__key = rwParse[2][rwParse[2].find('"')+1:-1]
                self.__signature = rwParse[3][rwParse[3].find('"')+1:-1]           
        return atoi(statusCode)    
        
    def __RSA_Encrypt(self,plain,length,rsa_n,rsa_e):
        import rsa
        ret = rsa.rsa(plain, rsa_e, rsa_n[:256], False)
        return b2a_hex(ret)
        
    def constructEncodedResponse(self):
        if self.__ERR_PASSWORD != self.__curStausCode:
            return ''
        V2Digest = SSICertification.GetV4Digest2_Static(self.__user.userid, self.__user.password)
        AESKey = random_hexstr(32)
        plain = self.__nonce+a2b_hex(V2Digest)+a2b_hex(AESKey)
        key = self.__key
        result = self.__RSA_Encrypt(plain,len(plain),key[:-6],key[-6:])        
        return result
       
    #regiseter the client to the server            
    def SPICRegister(self):
        self.initSock()
        #这里只是测试用
        self.__user.spi='585917501@fetion.com'
        self.__user.userid='202251968'
        
        msgHead=MsgHead()
        msgHead.R='fetion.com.cn SIP-C/4.0'
        msgHead.F=self.__user.spi[:self.__user.spi.find('@')]
        msgHead.I='1'
        msgHead.Q='1 R'
        msgHead.CN=random_str(32)
        msgHead.CL='type="pc",version="4.7.0800"'
        self.__state = self.__WAIT_SIPC_VERIFY1
        response=self.sendMsgWaitResponse(msgHead, '', self.__timeout)
        if '' == response:
            return -1
        self.__curStausCode = self.parseResponse(response)
        msgHead.erase()
        if __debug__:
            print self.__curStausCode
        
        if self.__ERR_PASSWORD == self.__curStausCode:   #如果是密码错误
            res = self.constructEncodedResponse()
            msgHead.R='fetion.com.cn SIP-C/4.0'
            msgHead.F=self.__user.spi[:self.__user.spi.find('@')]
            msgHead.I='1'
            msgHead.Q='2 R'
            msgHead.CN=''
            msgHead.CL=''
            msgHead.A='Digest algorithm="'+self.__DigAlg+'",response="'+res+'"'
 
            body = self.defaultLoginXML % (self.__user.mobileno, self.__user.userid, self.__user.presece)
            msgHead.L = len(body)
            self.__state = self.__WAIT_SIPC_VERIFY2
            response = self.sendMsgWaitResponse(msgHead, body, self.__timeout)
            self.__curStausCode = self.parseResponse(response)
            if __debug__:
                print self.__curStausCode
                print 'response:'
                print response
            
            #如果认证成功，启动收包任务和keep alive任务    
            if self.__SUCCESS == self.__curStausCode:
                   pass             
        return

    #以下为正常情况下的处理
    def getNextI(self):
        SIPC.ILock.acquire()
        self.__curI = self.__curI + 1
        SIPC.ILock.release()
        return self.__curI 
    
    def sengMsg(self, socket, msg, key, value):
        socket.send(msg)
        if self.__sendedMsg.has_key(key):
            return -1
        self.__sendedMsg[key] = value
        
    #报文拆分函数
    @staticmethod
    def divPacket(self, data):
        packetList = list()
        left = data
        while True:
            index = left.find('SIP-C/4.0 ')
            if (-1 != index):
                left = left[index:]
            valid=re.compile('SIP-C/4.0 .*\r\n\r\n.*')
            r1=valid.match(left)
            if None == r1:
                return (packetList, left)
            packets = str(r1.group(0))
            dataLen = len(packets)
            bodyIndex = packets.find('\r\n\r\n')+4
            #如果pakcets以'\r\n\r\n'结尾，并且报文头中也没有L，那么说明没有报文体，可以认为报文头就是一个报文
            Lindex = packets[:bodyIndex-4].find('L: ')
            if -1 == Lindex:
                packetList.append(packets[:bodyIndex-1])
                if dataLen == bodyIndex:
                    left = ''
                    return (packetList, left)
                left = packets[bodyIndex:]
                    
            Lindex = Lindex+3
            packlen = atoi(packets[Lindex:bodyIndex])
            #说明剩下的不够一个报文
            if packlen > len(packets[bodyIndex:]):
                print 'A'
                return (packetList, left)
            elif packlen == len(packets[bodyIndex:]):
                print 'B'
                packetList.append(packets)
                left=''
                return  (packetList, left)
            else:
                print 'C'
                packetList.append(packets[:bodyIndex+packlen])
                left = packets[bodyIndex+packlen:]
                
    def startRun(self):
        self.KAThread = SIPCKAThread(self.__sock, self)
        self.KAThread.start()
        
        recvTask(self.__sock, func_divPacket, func_ParsePacket)
        return
    
    def stopRun(self):
        if None != self.KAThread:
            self.KAThread.stop()

    @staticmethod
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
    
    
    def findMatchSend(self, key):
        if self.__sendedMsg.has_key(key):
            return self.__sendedMsg.pop(key) 
        return ''
             
    def parseMsg(self, msg):
        statusCode, statusInfo, msgHead, body = preParseMsg(msg)
        if self.__NORMAL == self.__state:
            type = self.findMatchSend(msgHead.I)
            if '' == type:    #如果服务器返回的I值不是之前发过的I值，那么这个消息直接丢弃
                print 'the message Id is not correct'
                return -1
            

    def getFriendDetail(self, userid, sip):
        msgHead=MsgHead()
        msgHead.S = 'fetion.com.cn SIP-C/4.0'
        msgHead.F = self.__user.spi[:self.__user.spi.find('@')]
        msgHead.I = str(getNextI())+' '
        msgHead.Q = '1 S'
        msgHead.N = 'GetContactInfoV4'
        body = self.defGetFrdDetail % (userid, sip)
        msgHead.L = len(body)
        response = self.sendMsgWaitResponse(msgHead, body, self.__timeout)
        return
    
    def updateFriendInfo(self, friend):
        self.__user.friends.
                        
    def sendMsg2(self, to, msg):
        msgHead=MsgHead()
        msgHead.M = 'fetion.com.cn SIP-C/4.0'
        msgHead.F = self.__user.spi[:self.__user.spi.find('@')]
        msgHead.I = str(getNextI())+' '
        msgHead.Q = '1 M'
        msgHead.T = to
        msgHead.C = 'text/plain'
        msgHead.N = 'CatMsg'
        msgHead.L = len(msg)
        response = self.sendMsgWaitResponse(msgHead, msg, self.__timeout)
        print response        
              
class SysConfig:
    def __init__(self):
        self.spicServer=''
        self.ssiServer=''
        
    def getSysConfig(self, mobileNum, fetionNum):
        return
        
class user:
    def __init__(self, username, password):
        MOBILENUM_LEN = 11
        self.mobileno = ''
        self.fetionno = ''        
        if MOBILENUM_LEN == len(username):
            self.mobileno = username
        else:
            self.fetionno = username    
        self.password = password
        self.spi=''
        self.ssic=''
        self.userid = ''
        self.ssiCty=SSICertification(self)
        self.presece = FetionHidden   #默认隐身
        self.friends=dict()
                
    def login(self):
        self.ssiCty.ssiCertify()
        #self.ssic=self.ssiCty.getSSIC()
    def printUserInfo(self):
        print 'mobile='+self.mobileno
        print 'fetion='+self.fetionno
        print 'spi='+self.spi
        print 'ssic='+self.ssic
        print 'userid='+self.userid     
        
ut1=user('13810686793', 'Lyz8401')
#ut1.login()
#spic1=SIPC(ut1)
#spic1.SPICRegister()

#spic1.sendMsg('sip:681545999@fetion.com.cn;p=4612', 'this is first msg')
#test1

spic1=SIPC(ut1)
print spic1.getNextI()
print 'result should be ** and result is '+ut1.ssic     