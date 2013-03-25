#encoding=utf-8
import thread
import select

class recvTask(threading.Thread):
    #传入需要收包的socket以及收到报文以后放入的队列，这里队列使用list就可以了, 
    #func_divPacket(data)传入的报文分段，该函数返回一个报文的（list, left)前面是完整的报文的list，后面是剩下的不完整的报文部份
    def __init__(self, socket, func_divPacket, func_ParsePacket, timeout=10):
        self.__socket = socket
        self.__queue = queue
        self.stop = False
        self.__timeout = timeout
        self.recvOnce = 1024
        
    def stop(self):
        self.__stop = True
            
    def run(self):
        data = ''
        while False == self.__stop:
            infd,outfd,errfd=select([self.__sock], [], [], self.__timeout)
            if 0 != len(infd):
                data+=self.__sock.recv(self.recvOnce)
                infd,outfd,errfd=select([self.__sock], [], [], 0)
                while 0 != len(infd): #这里先把报文收全了
                    data+=self.__sock.recv(self.recvOnce)
                    infd,outfd,errfd=select([self.__sock], [], [], 0)
            
            list, left = func_divPacket(data)
            data = left
            for packet in list:
                func_ParsePacket(packet)
        return
                