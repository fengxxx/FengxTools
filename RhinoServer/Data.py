# Data.py
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import logging,os

# main value
SERVER=None
SERVER_NAME="RhinoServer" #_save
VERSION=1.0 #_save
Version=VERSION
CONNECTIONS=[]
#USERS=[]
REGISTER_USERS=[] #_save
ONLINE_USER=[]
NEXT_USER_ID=0 #_save

# network defien
CMD_SPLIT="|"
class CMD_NETWORK_HAND():
    verify="verify",
    say="say",
    regist="regist",
    login="regist"
    msg="msg"


#--filePath
PATH_SETTINGS="config.xml"
PATH_REGISTER_USERS="register_users.xml"
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
logger = logging.getLogger(SERVER_NAME)

class User():
    def __init__( self):
        global NEXT_USER_ID
        NEXT_USER_ID+=1
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
    def isPassword(psw):
        res=False
        if psw==__password:
            res=True
        return res
def createNewUser(name):
    u=User()
    u.name=name
    return u

def getUserByName(name):
    user=None
    for u in REGISTER_USERS:
        if u.name==name:
            user=u
    if user==None:
        logger.debug("cant find the user!")
    return user

def getUserByID(userID):
    user=None
    for u in REGISTER_USERS:
        if u.ID==userID:
            user=u
    if user==None:
        logger.debug("cant find the user! with ID:"+str(userID))
    return user

def getUsersByName(name):
    users=[]
    for u in REGISTER_USERS:
        if u.name==name:
            users.append(u)
    if len(user)==0:
        logger.debug("cant find the user!")
    return users



def login(name,password):
    suc=False
    msg="bad userName or password"
    u=getUserByName(name)
    if u!=None:
        if u.isPassword(password):
            msg="login succed!"
            suc=True
    return suc,u,msg
def regist(name,password):
    regMsg=""
    suc=False
    u=getUserByName(name)
    if u==None:
        u=createNewUser(name)
        u.setPassword=password
        REGISTER_USERS.append(u)
        regMsg="regist succed!"
        suc=True
    else:
        regMsg="the userName is exist!"
    return suc,u,regMsg


def getUsersDataFromFile(filePath):
    ()

def savaUsersDataFromFile(filePath):
    ()

def getSettingsFromFile(filePath):
    ()

def savaSettingsToFile(filePath):
    ()

if __name__ == '__main__':
    for i in xrange(0,20):
        REGISTER_USERS.append(createNewUser(str(i)))
    for u in REGISTER_USERS:
        print u.name,u.ID
