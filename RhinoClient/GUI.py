# GUI.py
# -*- coding: utf-8 -*-
import sys,time,random
reload(sys)
sys.setdefaultencoding( "utf-8" )
import wx,Data,ClientNetwork
from wx.lib.pubsub import pub
from Data import *

class ChatFrame ( wx.Frame ):
    lastPos=[0,0]
    canMove=False
    canSize=False
    mousePos=[0,0]
    pos=[400,300]
    size=[0,0]
    isMaxWindow=False
    lastWindowSize=(0,0)
    lastWindowPos=(0,0)

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FengxEngine 1.0", pos = wx.DefaultPosition, size = wx.Size( 876,685 ), style =wx.DEFAULT_FRAME_STYLE  ) #wx.NO_BORDER|wx.TAB_TRAVERSAL ) #wx.RESIZE_BORDER|

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( UI_COLOR_MAIN_FG )
        self.SetBackgroundColour( UI_COLOR_MAIN_BG )

        self.tex_show = wx.TextCtrl(self, -1, "", size=(125, -1),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.tex_input = wx.TextCtrl(self, -1, "", size=(125, -1),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.but_send = wx.Button(self, 10, "send", (20, 20))
        self.but_send.Bind(wx.EVT_BUTTON, self.OnClick_send)
        self.tex_show.SetBackgroundColour( UI_COLOR_MAIN_BG )
        self.tex_input.SetBackgroundColour( UI_COLOR_MAIN_BG )


        Sizer_main = wx.BoxSizer( wx.VERTICAL )
        Sizer_send = wx.BoxSizer( wx.HORIZONTAL )
        # self.p_moveBar.Layout()
        self.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)
        # self.box_movebar.Fit( self.p_moveBar)
        Sizer_send.Add( self.tex_input, 7, wx.EXPAND |wx.ALL, 0 )
        Sizer_send.Add( self.but_send, 3, wx.EXPAND |wx.ALL, 0 )
        Sizer_main.Add( self.tex_show, 6, wx.EXPAND |wx.ALL, 0 )
        Sizer_main.Add( Sizer_send, 4, wx.EXPAND |wx.ALL, 0 )
        # bSizer_mainScene.Add( self.tree_project, 1, wx.ALL|wx.EXPAND, 0 )

        self.SetSizer( Sizer_main )
        self.Layout()
        self.Centre( wx.BOTH )
        #pub.subscribe(self.recvMsg, "recvMsg")
        pub.subscribe(self.recvMsgFromServer, "recvMsgToServer")
    def OnClick_send(self,event):
        #wx.CallAfter(pub.sendMessage , "test", msg=self.tex_input.GetValue())
        if self.tex_input.GetValue()!="":
            wx.CallAfter(pub.sendMessage , "sendMsgToServer", msg="say|"+self.tex_input.GetValue())
            self.tex_input.SetValue("")
    def recvMsgFromServer(self,m):
        self.tex_show.WriteText("\n"+m)
    def regist(self,msg):
        wx.CallAfter(pub.sendMessage , "sendMsgToServer", msg="regist|"+self.tex_input.GetValue())
    def OnKeyDown(self,event):
        keycode = event.GetKeyCode()
        ctrldown = event.ControlDown()
        shiftdown = event.ShiftDown()
        altdown = event.AltDown()
        #if 32<=keycode<=126:
        print keycode
        if keycode==wx.WXK_NUMPAD_ENTER:
            self.OnClick_send(event)

class LoginFrame ( wx.Frame ):
    host="minecraftfengx.wicp.net"
    port=9999
    names=("州","猪","小明","小亮","鱼","Rhino","Fengx","服务器_1","菠菜","土豆","外星人")
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FengxEngine 1.0", pos = wx.DefaultPosition, size = wx.Size( 270,500 ), style =wx.DEFAULT_FRAME_STYLE  ) #wx.NO_BORDER|wx.TAB_TRAVERSAL ) #wx.RESIZE_BORDER|
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( UI_COLOR_MAIN_FG )
        self.SetBackgroundColour( UI_COLOR_MAIN_BG )

        self.tex_input = wx.TextCtrl(self, -1, self.names[random.randint(0,len(self.names))],size=(200,30),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.tex_host = wx.TextCtrl(self, -1, self.host,size=(200,30),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.tex_input.SetPosition((25,25))
        self.tex_host.SetPosition((25,70))
        self.but_send = wx.Button(self, 10, "登陆")
        self.but_send.SetPosition((25,230))
        self.but_send.SetSize((200,180))
        self.but_send.Bind(wx.EVT_BUTTON, self.regist)
        Sizer_main = wx.BoxSizer( wx.VERTICAL )
    def regist(self,msg):
        global mainWindow
        self.host=self.tex_host.GetValue()
        c=ClientNetwork.createClient(self.host,self.port)
        c.start()
        wx.CallAfter(pub.sendMessage , "sendMsgToServer", msg="regist|"+self.tex_input.GetValue())
        self.Show(False)
        Data.MAIN_FRAME.Show()

class MainFrame ( wx.Frame ):
    lastPos=[0,0]
    canMove=False
    canSize=False
    mousePos=[0,0]
    pos=[400,300]
    size=[0,0]
    isMaxWindow=False
    lastWindowSize=(0,0)
    lastWindowPos=(0,0)
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"FengxEngine 1.0", pos = wx.DefaultPosition, size = wx.Size( 876,685 ), style =wx.DEFAULT_FRAME_STYLE  ) #wx.NO_BORDER|wx.TAB_TRAVERSAL ) #wx.RESIZE_BORDER|

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( UI_COLOR_MAIN_FG )
        self.SetBackgroundColour( UI_COLOR_MAIN_BG )

        self.tex_show = wx.TextCtrl(self, -1, "", size=(125, -1),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.tex_input = wx.TextCtrl(self, -1, "", size=(125, -1),style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.but_send = wx.Button(self, 10, "send", (20, 20))
        self.but_send.Bind(wx.EVT_BUTTON, self.OnClick_send)
        self.tex_show.SetBackgroundColour( UI_COLOR_MAIN_BG )
        self.tex_input.SetBackgroundColour( UI_COLOR_MAIN_BG )


        Sizer_main = wx.BoxSizer( wx.VERTICAL )
        Sizer_send = wx.BoxSizer( wx.HORIZONTAL )
        # self.p_moveBar.Layout()
        self.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)
        # self.box_movebar.Fit( self.p_moveBar)
        Sizer_send.Add( self.tex_input, 7, wx.EXPAND |wx.ALL, 0 )
        Sizer_send.Add( self.but_send, 3, wx.EXPAND |wx.ALL, 0 )
        Sizer_main.Add( self.tex_show, 6, wx.EXPAND |wx.ALL, 0 )
        Sizer_main.Add( Sizer_send, 4, wx.EXPAND |wx.ALL, 0 )
        # bSizer_mainScene.Add( self.tree_project, 1, wx.ALL|wx.EXPAND, 0 )

        self.SetSizer( Sizer_main )
        self.Layout()
        self.Centre( wx.BOTH )
        #pub.subscribe(self.recvMsg, "recvMsg")
        pub.subscribe(self.recvMsgFromServer, "recvMsgToServer")
    def OnClick_send(self,event):
        #wx.CallAfter(pub.sendMessage , "test", msg=self.tex_input.GetValue())
        if self.tex_input.GetValue()!="":
            wx.CallAfter(pub.sendMessage , "sendMsgToServer", msg="say|"+self.tex_input.GetValue())
            self.tex_input.SetValue("")
    def recvMsgFromServer(self,m):
        self.tex_show.WriteText("\n"+m)
    def regist(self,msg):
        wx.CallAfter(pub.sendMessage , "sendMsgToServer", msg="regist|"+self.tex_input.GetValue())
    def OnKeyDown(self,event):
        keycode = event.GetKeyCode()
        ctrldown = event.ControlDown()
        shiftdown = event.ShiftDown()
        altdown = event.AltDown()
        #if 32<=keycode<=126:
        print keycode
        if keycode==wx.WXK_NUMPAD_ENTER:
            self.OnClick_send(event)

def startGUI():
    mainApp = wx.App()
    mainWindow=ChatFrame(parent=None)
    loginWindow=LoginFrame(parent=None)
    Data.MAIN_FRAME=mainWindow
    Data.LOGIN_FRAME=loginWindow
    Data.MAIN_APP=mainApp
