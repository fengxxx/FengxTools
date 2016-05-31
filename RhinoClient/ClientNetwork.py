# ClientNetwork.py
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import socket,os,time,sys,Data,wx
from threading import Thread
from wx.lib.pubsub import pub

class Client():
    HOST='localhost'
    if HOST=="":
        HOST='localhost'
    PORT=9999
    CMD_Split=Data.CMD_SPLIT
    CMDN=Data.CMD_NETWORK_HAND()
    isRegist=False
    isLogin=False
    canVerify=False
    def __init__(self,host,port):
        self.HOST=host
        self.PORT=port
        ADDR=(self.HOST,self.PORT)
        self.TCP_Sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.TCP_Sock.connect(ADDR)
        name=""
        print ">>conect to : ",self.HOST,":",self.PORT
        pub.subscribe(self.sendMsgToServer, "sendMsgToServer")
        pub.subscribe(self.login, "login")
        pub.subscribe(self.regist, "regist")
        pub.subscribe(self.sayWord, "sayWord")
    def run(self):
        while True:
            data=self.TCP_Sock.recv(1024)
            if data!="" and data!=None:
                self.onNetworkRecv(data)
    def sendMsgToServer(self,msg):
        t=msg
        self.TCP_Sock.send(t)
        print "send:",t
    def sayWord(self,msg):
        msg=CMDN.say+CMD_SPLIT+msg
        self.TCP_Sock.send(msg)
        print msg
    def onNetworkRecv(self,data):
        #on first hand
        CMDN=Data.CMD_NETWORK_HAND()
        print "recv:",data
        if data!="" and data!=None:
            ds=data.split(Data.CMD_SPLIT)
            if len(ds)>1:
                if not self.isLogin:
                    if ds[0]==CMDN.verify:
                        print "ds",ds
                        if len(ds)>1:
                            self.isLogin=True
                            print "server:",ds[1]
                else:
                    if ds[0]==CMDN.say:
                        if len(ds)==2:
                            wx.CallAfter(pub.sendMessage , "getMsg",m=ds[1])
                        else:
                            print "say what?"
                    else:
                        ()#...
    def login(self,name,password):
        cmd=self.CMDN.login+Data.CMD_SPLIT+name+Data.CMD_SPLIT+password
        self.TCP_Sock.send(cmd)
    def regist(self,name,password):
        cmd=self.CMDN.regist+Data.CMD_SPLIT+name+Data.CMD_SPLIT+password
        self.TCP_Sock.send(cmd)
    # def sendCMD(self,cmdType,):
    #     cmd=
    #     self.request.send()
class ClientThread(Thread):
    host= socket.gethostbyname(socket.gethostname())
    port=9999
    def __init__(self,host,port):
        Thread.__init__(self)
        self.host=host
        self.port=port
        self.client=Client(self.host,self.port)
        #self.start()
    def run(self):
        self.client.run()

def createClient(host,port):
    return ClientThread(host,port)
