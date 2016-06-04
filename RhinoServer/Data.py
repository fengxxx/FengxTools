# Data.py
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import logging,os,json

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
    verify="verify"
    say="say"
    regist="regist"
    login="login"
    msg="msg"
    fileStart="fileStart"
    fileEnd="fileEnd"
    addUser="addUser"

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
    ''' user info!!!'''
    ID=-1
    name="USER_NAME"
    __password="fengx"
    online=False
    SRH=None
    histroy="x"
    logger = logging.getLogger('RhinoServers')
    def __init__( self):
        global NEXT_USER_ID
        self.ID=NEXT_USER_ID
        NEXT_USER_ID+=1
        self.asdasdasd=1312
    def __dict__(self):
        return {"ID":self.ID,"sdasd":histroy}
    def __str__(self):
        return "sdasfmalskfmlas"
    # def __new__(self,*args, **kwargs):
    #     NEXT_USER_ID+=1
    #
    def setUserName(self,n):
        self.userName==n

    def setPassword(self,p):
        self.__password==p

    def sendMsg(self,msg):
        if self.SRH!=None:
            logger.warning("cant send msg , is not connectting")

    def isPassword(self,psw):
        res=False
        if psw==self.__password:
            res=True
        return res
    def toJson(self):
        d=[{u"name":self.name,u"ID":self.ID,u"online":self.online}]
        return json.dumps(d)
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
    print u
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

def object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    print obj.__dict__
    return d

def dict2object(d):
    #convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        print args
        inst = class_() #create new instance
    else:
        inst = d
    return inst


@classmethod
def test():
    print "@classmethod"

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

    #print dir(REGISTER_USERS[1])
    #print REGISTER_USERS[1].__dict__
    data_j= str(REGISTER_USERS[1].toJson())
    # print data_j
    j= json.dumps(data_j,sort_keys=True,indent=4)
    print j
    print data_j
    a=json.loads(data_j)
    print a
