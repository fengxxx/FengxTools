# Data.py
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import logging,os

LOG_FILE_PATH=SERVER_NAME+".log"
LOG_FILE_WRITE_MODE="r"
if os.path.isfile(LOG_FILE_PATH):
    LOG_FILE_WRITE_MODE="a"
else:
    LOG_FILE_WRITE_MODE="wb"

# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# logging.basicConfig函数各参数:
# filename: 指定日志文件名
# filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
# format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
#  %(levelno)s: 打印日志级别的数值
#  %(levelname)s: 打印日志级别名称
#  %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
#  %(filename)s: 打印当前执行程序名
#  %(funcName)s: 打印日志的当前函数
#  %(lineno)d: 打印日志的当前行号
#  %(asctime)s: 打印日志的时间
#  %(thread)d: 打印线程ID
#  %(threadName)s: 打印线程名称
#  %(process)d: 打印进程ID
#  %(message)s: 打印日志信息
# datefmt: 指定时间格式，同time.strftime()
# level: 设置日志级别，默认为logging.WARNING
# stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=LOG_FILE_PATH,
                filemode=LOG_FILE_WRITE_MODE)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

SERVER=None
SERVER_NAME="RhinoServer"
VERSION=1.0
Version=VERSION

CONNECTIONS=[]
USERS=[]
REGISTER_USERS=[]
ONLINE_USER=[]

class User():
    ID=-1
    name="USER_NAME"
    __password="fengx"

    online=False

    SRH=None

    histroy="x"

    logger = logging.getLogger('RhinoServers')
    def setUserName(self,n):
        self.userName==n
    def setPassword(self,p):
        self.__password==n
    def sendMsg(self,msg):
        if SRH!=None:
            logger.warning("cant send msg , is not connectting")
def createNewUser(name):
    u=User()
    u.name=name
    return u

# def getUserByName(name):
#     for u in REGISTER_USERS:
#         if u.name==name:
#


#---
