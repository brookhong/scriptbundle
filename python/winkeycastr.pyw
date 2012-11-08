import os
import struct
import win32api
import win32con
import win32gui
import pyHook
from ctypes import windll,cdll

class MainWindow:
    def __init__(self):
        win32gui.InitCommonControls()
        self.hinst = win32api.GetModuleHandle(None)
        self.tracelog       = open('c:/tools/vim/keycastr.log','w')
        self.key = ""
        self.gdi32 = windll.gdi32
        # create a hook manager
        self.hm = pyHook.HookManager()
        # watch for all mouse events
        self.hm.KeyDown = self.OnKeyboardEvent
        # set the hook
        self.hm.HookKeyboard()
        # wait forever
    def CreateWindow(self):
       className = self.RegisterClass()
       self.BuildWindowEx(className)

    def RegisterClass(self):
       className = "TeSt"
       message_map = { win32con.WM_DESTROY: self.OnDestroy,
               win32con.WM_KEYDOWN: self.OnKey,
               win32con.WM_PAINT: self.OnPaint,
               win32con.WM_USER+1: self.OnHook,
               }
       wc=win32gui.WNDCLASS()
       wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
       wc.lpfnWndProc = message_map
       wc.cbWndExtra = 0
       wc.hCursor = win32gui.LoadCursor( 0, win32con.IDC_ARROW )
       wc.hbrBackground = win32con.COLOR_WINDOW + 1
       wc.hIcon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
       wc.lpszClassName = className
       # C code: wc.cbWndExtra = DLGWINDOWEXTRA + sizeof(HBRUSH) + (sizeof(COLORREF))
       wc.cbWndExtra = win32con.DLGWINDOWEXTRA + struct.calcsize("Pi")
       #wc.hIconSm = 0
       classAtom = win32gui.RegisterClass(wc)
       return className

    def BuildWindowEx(self, className):
       style = win32con.WS_CLIPSIBLINGS | win32con.WS_CLIPCHILDREN | win32con.WS_POPUP
       self.hwnd = win32gui.CreateWindowEx(win32con.WS_EX_LAYERED, className,
                             "ThisIsJustATest",
                             style,
                             win32con.CW_USEDEFAULT,
                             win32con.CW_USEDEFAULT,
                             400,
                             100,
                             0,
                             0,
                             self.hinst,
                             None)
       win32gui.SetLayeredWindowAttributes(self.hwnd, 0xffffff, 200, win32con.LWA_COLORKEY)
       win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0,0,400,100, win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE| win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW)
       win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)

    def OnDestroy(self, hwnd, message, wparam, lparam):
        win32gui.PostQuitMessage(0)
        return True

    def OnKey(self, hwnd, message, wparam, lparam):
        if wparam == win32con.VK_ESCAPE:
            win32gui.PostQuitMessage(0)
        return True

    def OnPaint(self, hwnd, message, wparam, lparam):
        (hDc, ps) = win32gui.BeginPaint(hwnd)
        if len(self.key) > 0:
            hBrush = self.gdi32.CreateSolidBrush(0x00ffff)
            self.gdi32.SelectObject(hDc, hBrush)
            hFont = self.gdi32.CreateFontA(48,0,0,0,0,0,0,0,1,8, 0,5, 2, 0)
            self.gdi32.SelectObject(hDc, hFont)
            (cx, cy) = win32gui.GetTextExtentPoint32(hDc, self.key)
            self.gdi32.RoundRect(hDc,0,0,cx+20,cy+20,20,20)
            self.gdi32.SetTextColor(hDc, 0xff0000)
            self.gdi32.SetBkMode(hDc, 1)
            textRect = (10,10,400,100)
            win32gui.DrawText(hDc,self.key,-1, textRect, 0)
            self.gdi32.DeleteObject(hFont)
        win32gui.EndPaint(hwnd,ps)
        return True
    def OnHook(self, hwnd, message, wparam, lparam):
        if wparam == 1:
            self.hm.UnhookKeyboard()
            self.hm = None
            win32gui.PostQuitMessage(0)
        else:
            win32gui.InvalidateRect(hwnd, None, True)
        return True
    def OnKeyboardEvent(self, event):
        if event.Window != self.hwnd:
            k = event.Ascii
            if cdll.msvcrt.isprint(k):
                self.key = chr(event.Ascii)
            else:
                self.key = event.Key
            win32gui.PostMessage(self.hwnd,win32con.WM_USER+1,0,0)
            self.tracelog.write('MessageName:%s\n'%event.MessageName)
            self.tracelog.write('Message:%s\n'%event.Message)
            self.tracelog.write('Time:%s\n'%event.Time)
            self.tracelog.write('Window:%s\n'%event.Window)
            self.tracelog.write('Window this:%s\n'%self.hwnd)
            self.tracelog.write('WindowName:%s\n'%event.WindowName)
            self.tracelog.write('Ascii:%s, %s\n' % (event.Ascii, chr(event.Ascii)))
            self.tracelog.write('Key:%s\n'% event.Key)
            self.tracelog.write('KeyID:%s\n'% event.KeyID)
            self.tracelog.write('ScanCode:%s\n'% event.ScanCode)
            self.tracelog.write('Extended:%s\n'% event.Extended)
            self.tracelog.write('Injected:%s\n'% event.Injected)
            self.tracelog.write('Alt: %s\n'% event.Alt)
            self.tracelog.write('Transition: %s\n'% event.Transition)
            self.tracelog.write('---')
        #else:
            #win32gui.SendMessage(self.hwnd,win32con.WM_USER+1,1,0)


        # return True to pass the event to other handlers
        return True

w = MainWindow()
w.CreateWindow()
win32gui.PumpMessages()
