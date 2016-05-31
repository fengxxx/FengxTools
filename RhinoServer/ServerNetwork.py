# ServerNetwork.py
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import time,os,socket,Data,SocketServer,logging


class RhinoServers(SocketServer.StreamRequestHandler):
    logger = logging.getLogger('RhinoServers')
    recvByteSize=1025
    connecter=None
    user=None
    isRegist=False
    isWaite=False
    CMD_Split=Data.CMD_SPLIT
    CMDN=Data.CMD_NETWORK_HAND()
    def handle(self):
        self.onConnectStart()
        while True:
            data=""
            try:
                data = self.request.recv(recvByteSize)
            except:
                logger.warning('dont know what')
            if not data:
                self.onNetworkBreak()
            else:
                self.onNetworkRecv(data)

    # on recv message
    def onNetworkRecv(self,data):
        #on first hand
        CMDN=Data.CMD_NETWORK_HAND()
        print "recv:",data
        if data!="" and data!=None:
            ds=data.split(commandSplit)
            if ds.count>1:
                if not self.isRegist:
                    if ds[0]==CMDN.login:
                        loginMsg=""
                        if ds.count==3:
                            suc,u,loginMsg=Data.login(ds[1],ds[2])
                            if suc:
                                self.user=u
                        else:
                            self.sendMsg(CMDN.msg,loginMsg)
                    elif ds[0]==CMDN.regist:
                        regMsg=""
                        if ds.count==3:
                            suc,u,regMsg=Data.regist(ds[1],ds[2])
                            if suc:
                                self.user=u
                        else:
                            self.sendMsg(CMDN.msg,"")
                else:
                    if ds[0]==CMDN.say:
                        if ds.count==2:
                            self.broadcastMsg(self.user,ds[1])
                        else:
                            print "say what?"
                    else:
                        ()#...
    # on connection break
    def onConnectionBreak(self):
        print self.name," is leav!"
        loginMsg=('<%s> %s:%s at %s was leaved the chat room!' % (self.name,self.client_address[0],self.client_address[1],time.ctime()))
        self.broadcastCMD(loginMsg)
        Data.CONNECTIONS.remove (self);

    # on connection start
    def onConnecttionStart(self):
        Data.CONNECTIONS.append(self);
        #print 'got connection from ',self.client_address
        logger.DEBUG('got connection from ',self.client_address)
        self.onVerify()
    def onVerify(self):
        self.request.send(CMDN.verify+commandSplit+"who are you!")
        self.isWaite=True

    def broadcastCMD(self,user,msg):
        for s in Data.CONNECTIONS:
            try:
                self.sendMsg(CMDN.msg,msg)
            except Exception as e:
                print "lost men:",e
    def broadcastMsg(self,user,msg):
        for s in Data.CONNECTIONS:
            try:
                self.sendMsg(CMDN.msg,msg)
            except Exception as e:
                print "lost men:",e

    def sendMsg(self,msgType,msg):
        CMD_Split=Data.CMD_SPLIT
        self.request.sendMsg(msgType+CMD_Split+msg)

    def sendMsgToUser(self,user,msg):
        ()#self.request.sendMsg(msgType+CMD_Split+msg)
def createServer(host,port):
    addr=(host,port)
    server = SocketServer.ThreadingTCPServer(addr,RhinoServers)
    return server
