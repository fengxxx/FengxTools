# Data.py
# -*- coding: utf-8 -*-
import sys,time,random,logging,wx,os,socket,json
reload(sys)


LOCALHOST=socket.gethostbyname(socket.gethostname())

MAIN_APP=None
MAIN_FRAME=None
LOGIN_FRAME=None
CHAT_FRAMES=[]

#---dir
ROOT_DIR=os.getcwd() #--root dir
ICON_PATH=ROOT_DIR+"\\fengxEngine.ico"

#----color
MAIN_BG_COLOR=(37,37,37)
CONSOLE_BG_COLOR=(48,10,3)

#----data
MAIN_WINDOW_SIZE=(900,600)
# EYE_POS=[1.0,1.0,1.0]
# TARGET_POS=[0.0,0.0,0.0]
ANGLE = -90
ANGLE_UP=-90
PI=3.14159
SPEED=2
rSPEED=-0.01

GL_COLOR_viewPort_BG=(0.40,0.40,0.40,0)
GL_COLOR_gridLine=(0.35,0.35,0.35,0)

UI_COLOR_MAIN_BG=(67,67,67)
UI_COLOR_MAIN_FG=(130,130,130)
UI_COLOR_movebar_BG=(140,140,140)
UI_COLOR_movebar_FG=(45,45,45)
UI_COLOR_sizebar_BG=(130,130,130)
UI_COLOR_sizebar_FG=(67,67,67)
UI_COLOR_sceneTree_BG=(140,140,140)
UI_COLOR_sceneTree_FG=(50,50,50)
UI_COLOR_mainToolbar_BG=(130,130,130)
UI_COLOR_mainToolbar_FG=(67,67,67)

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

FRENDES=[]



LOG_FILE_PATH="RhinoClient.log"
LOG_FILE_WRITE_MODE="r"
if os.path.isfile(LOG_FILE_PATH):
    LOG_FILE_WRITE_MODE="a"
else:
    LOG_FILE_WRITE_MODE="wb"

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=LOG_FILE_PATH,
                filemode=LOG_FILE_WRITE_MODE)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

class User():
    ''' user info!!!'''
    ID=-1
    name=u"USER_NAME"
    #__password="fengx"
    online=False
    #SRH=None
    histroy="x"
    logger = logging.getLogger('RhinoClient')
    def __init__( self):
        ()
    def __dict__(self):
        return {"ID":self.ID,"sdasd":histroy}
    def __str__(self):
        return "sdasfmalskfmlas"
    def toJson(self):
        d=[{u'name':self.name,u'ID':self.ID,u'online':self.online}]
        return d
def createNewUser(name,ID,online):
    u=User()
    u.name=name
    u.online=online
    u.ID=ID
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
def createUserByJson(j):
    #dj=json.dumps(j)
    djj=json.loads(j)
    print djj[0].keys()
    return createNewUser(djj[0][u"name"],djj[0][u"ID"],djj[0][u"online"])

# obj=[1231,4124,24,{"sadasd":2112,"222":False}]
# print json.dumps(obj)
#
# s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
# print s
# print s.keys()
# createUserByJson(User().toJson())
