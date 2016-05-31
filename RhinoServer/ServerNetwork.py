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
        self.onConnecttionStart()
        while True:
            data=""
            try:
                data = self.request.recv(self.recvByteSize)
            except:
                ()
                #self.logger.warning('dont know what')
            if not data:
                ()#self.onConnectionBreak()
            else:
                self.onNetworkRecv(data)

    # on recv message
    def onNetworkRecv(self,data):
        #on first hand
        CMDN=Data.CMD_NETWORK_HAND()
        print "recv:",data
        if data!="" and data!=None:
            ds=data.split(Data.CMD_SPLIT)
            if len(ds)>1:
                if not self.isRegist:
                    if ds[0]==CMDN.login:
                        loginMsg=""
                        suc=False
                        u=None
                        print ds[1],ds[2]
                        print Data.login(ds[1],ds[2])
                        try:
                            suc,u,loginMsg=Data.login(ds[1],ds[2])
                            print "suc,u,loginMsg",suc,u,loginMsg
                        except Exception as e:
                            print e
                            loginMsg="get bad login value"
                        print suc
                        if suc:
                            self.user=u
                            self.isRegist=True
                            self.sendMsg(CMDN.verify,loginMsg)
                            self.sendMsg(CMDN.msg,loginMsg)
                        else:
                            self.sendMsg(CMDN.msg,loginMsg)
                    elif ds[0]==CMDN.regist:
                        regMsg=""
                        suc=False
                        u=None
                        try:
                            suc,u,regMsg=Data.regist(ds[1],ds[2])
                            print "suc,u,regMsg",suc,u,regMsg
                        except Exception as e:
                            print e
                        if suc:
                            self.user=u
                            self.isRegist=True
                            self.sendMsg(CMDN.verify,regMsg)
                            self.sendMsg(CMDN.msg,regMsg)
                        else:
                            self.sendMsg(CMDN.msg,regMsg)
                else:
                    if ds[0]==CMDN.say:
                        if len(ds)==2:
                            print "broadcastMsg",ds[1]
                            self.broadcastMsg(self.user,ds[1])
                        else:
                            print "say what?"
                    else:
                        ()#...
    # on connection break
    def onConnectionBreak(self):
        if not self.isRegist or self.user==None:
            print self.request," is leav!"
        else:
            print self.user.name," is leav!"
        #loginMsg=('<%s> %s:%s at %s was leaved the chat room!' % (self.name,self.client_address[0],self.client_address[1],time.ctime()))
        self.broadcastCMD(None,"someone is leav")
        try:
            Data.CONNECTIONS.remove (self);
        except Exception as e:
            print e

    # on connection start
    def onConnecttionStart(self):
        Data.CONNECTIONS.append(self);
        #print 'got connection from ',self.client_address
        self.logger.debug('got connection from ',self.client_address)
        self.onVerify()
    def onVerify(self):
        cmd=self.CMDN.verify+self.CMD_Split+"who are you!"
        self.request.send(cmd)
        self.isWaite=True

    def broadcastCMD(self,user,msg):
        for s in Data.CONNECTIONS:
            try:
                s.request.send(self.CMDN.say+Data.CMD_SPLIT+msg)
                print (self.CMDN.say+Data.CMD_SPLIT+msg)
            except Exception as e:
                print "lost men:",e
    def broadcastMsg(self,user,msg):
        for s in Data.CONNECTIONS:
            try:
                s.request.send(self.CMDN.say+Data.CMD_SPLIT+s.user.name+":"+msg)
                print (self.CMDN.say+Data.CMD_SPLIT+msg)
            except Exception as e:
                print "lost men:",e

    def sendMsg(self,msgType,msg):
        CMD_Split=Data.CMD_SPLIT
        print msgType,msg
        self.request.send(msgType+CMD_Split+msg)

    def sendMsgToUser(self,user,msg):
        ()#self.request.sendMsg(msgType+CMD_Split+msg)
def createServer(host,port):
    addr=(host,port)
    server = SocketServer.ThreadingTCPServer(addr,RhinoServers)
    return server
