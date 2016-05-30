# ServerNetwork.py
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import time,os,socket,Data,SocketServer,logging



class RhinoServers(SocketServer.StreamRequestHandler):
    logger = logging.getLogger('RhinoServers')
    def handle(self):
        Data.CONNECTIONS.append(self);
        print 'got connection from ',self.client_address
        #logger.DEBUG('got connection from ',self.client_address)
        while True:
            data=""
            try:
                data = self.request.recv(1024)
            except:
                print self.name," is leav!"
                #not work
            if not data:
                print self.name," is leav!"
                loginMsg=('<%s> %s:%s at %s was leaved the chat room!' % (self.name,self.client_address[0],self.client_address[1],time.ctime()))
                self.broadcastMesg(loginMsg)
                Data.CONNECTIONS.remove (self);
                break
            if self.name!="noname":
                print "-->>from: ", self.name
            else:
                print "-->>from: ", self.client_address
            print data
            if data!="" and data!=None:
                ds=data.split("|")
                if ds.count>1:
                    if ds[0]=="say":
                        self.broadcastMesg(self.name+":"+ds[1])
                    elif ds[0]=="regist":
                        self.name=ds[1]
                        loginMsg=('wellcome  <%s> %s:%s at %s add chat room!' % (self.name,self.client_address[0],self.client_address[1],time.ctime()))
                        self.broadcastMesg(loginMsg)

    def broadcastMesg(self,msg):
        print ("broadcastMesg: ",msg)
        for s in Data.CONNECTIONS:
            try:
                s.request.send(msg)
            except Exception as e:
                print "lost men:",e

def createServer(host,port):
    addr=(host,port)
    server = SocketServer.ThreadingTCPServer(addr,RhinoServers)
    return server
