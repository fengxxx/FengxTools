# Data.py
# -*- coding: utf-8 -*-
import sys,time,random,logging,wx,os
reload(sys)

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
