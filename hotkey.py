import pythoncom
import pyHook
import time
#import pyhk
import os
import sys
import ctypes
from ctypes import wintypes
import win32con,win32api
import threading


print('  sdf')

def onKeyboardEvent(event):
    print('MessageName: %s' % event.MessageName)
    print('Message: %s' % event.Message)
    print('Time: %s' % event.Time)
    print('Window: %s' % event.Window)
    print('WindowName: %s' % event.WindowName)
    print('Ascii: %s' % event.Ascii)
    print('Key: %s' % event.Key)
    print('KeyID: %s' % event.KeyID)
    print('ScanCode: %s' % event.ScanCode)
    print('Extended: %s' % event.Extended)
    print('Injected: %s' % event.Injected)
    print('Alt: %s' % event.Alt)
    print('Transition: %s' % event.Transition)
    print('--------------------------------')
    if str(event.Key) == 'F12':
        win32api.PostQuitMessage()
    if str(event.Key) == 'Alt':
        print('yes')
    if str(event.Key) == 'F8':
        print('**********************')
    return True

def onMouseEvent(event):
    print('MessageName%s' % event.MessageName)
    return True
    
# 创建一个“钩子”管理对象    
hm = pyHook.HookManager()

# 监听所有键盘事件     
hm.KeyDown = onKeyboardEvent

# 设置键盘“钩子”
hm.HookKeyboard()



# 监听所有鼠标事件     
#hm.MouseAll = onMouseEvent     
# 设置鼠标“钩子”
#hm.HookMouse()

def task():
    for each in range(1,10000,1):
        print('I am task')
        time.sleep(1)

mythread = threading.Thread(target=task)
mythread.start()


# 进入循环，如不手动关闭，程序将一直处于监听状态
pythoncom.PumpMessages(100) 




