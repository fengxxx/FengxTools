# mainApp.py
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import Data,ServerNetwork,socket,logging


if __name__ == '__main__':
    logger = Data.logging.getLogger('MAIN_APP')
    #print Data.SERVER_NAME," ",Data.VERSION," initialization is starting....."
    logger.debug("\n========================================\n"*3+Data.SERVER_NAME+" "+str(Data.VERSION)+" initialization is starting.....")
    host=""
    port = 9999
    addr = (host,port)
    if len(sys.argv)>1:
        if sys.argv[1]!="":
            sp=sys.argv[1]
            if len(sp)>1:
                host= sys.argv[1]
            else:
                host=sp[0]
                port=sp[1]
            print sys.argv[1]
    if host=="":
        host= socket.gethostbyname(socket.gethostname())
    Data.SERVER=ServerNetwork.createServer(host,port)
    #print Data.SERVER_NAME,' is servering on addr:',host,'port:',port
    logger.debug(Data.SERVER_NAME+' is servering on addr: '+host+' port: '+str(port))
    Data.SERVER.serve_forever()
