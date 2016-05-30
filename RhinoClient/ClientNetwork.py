# ClientNetwork.py
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import socket,os,time,sys,wx
from threading import Thread
from wx.lib.pubsub import pub

class Client():
    HOST='localhost'
    if HOST=="":
        HOST='localhost'
    PORT=9999
    def __init__(self,host,port):
        self.HOST=host
        self.PORT=port
        ADDR=(self.HOST,self.PORT)
        self.TCP_Sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.TCP_Sock.connect(ADDR)
        name=""
        print ">>conect to : ",self.HOST,":",self.PORT
        pub.subscribe(self.sendMsgToServer, "sendMsgToServer")
    def run(self):
        while True:
            data=self.TCP_Sock.recv(1024)
            if data!="" and data!=None:
                wx.CallAfter(pub.sendMessage , "recvMsgToServer", m=data)
                # if data!="" and data!=None:
                #     ds=data.split("|")
                #     if ds.count>1:
                #         if ds[0]=="say":
                #             self.broadcastMesg(self.name+":"+ds[1])
                #         elif ds[0]=="regist":
                #             self.name=ds[1]
                #             loginMsg=('wellcome  <%s> %s:%s at %s add chat room!' % (self.name,self.client_address[0],self.client_address[1],time.ctime()))
                #             self.broadcastMesg(loginMsg)
    def sendMsgToServer(self,msg):
        t=msg
        self.TCP_Sock.send(t)
        print "send:",t

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
