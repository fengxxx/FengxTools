# mainApp.py
# -*- coding: utf-8 -*-
import sys,time,random
reload(sys)
import GUI,Data

if __name__=='__main__':
    GUI.startGUI()
    Data.LOGIN_FRAME.Show()
    Data.MAIN_APP.MainLoop()
