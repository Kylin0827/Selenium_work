#模拟Windows点击键盘
# import win32com.client
#需要先安装pypiwin32库，安装好了之后重启下pycharm，windows版本的默认安装好了
#官方文档：http://timgolden.me.uk/pywin32-docs/win32api__keybd_event_meth.html
#键盘对应参数：https://docs.microsoft.com/zh-cn/windows/desktop/inputdev/virtual-key-codes
import time
import win32api
import win32con

# shell = win32com.client.Dispatch("WScript.Shell")
#模拟5次下方向键
# for i in range(5):
#     win32api.keybd_event(win32con.VK_DOWN, 0)
#     time.sleep(0.5)

#模拟向下的按键
win32api.keybd_event(win32con.VK_DOWN,0)

win32api.keybd_event(win32con.VK_NUMPAD0,0)
#模拟回车符号
win32api.keybd_event(win32con.VK_RETURN, 0)

win32api.keybd_event(win32con.VK_SPACE, 0)

win32api.keybd_event(win32con.VK_ADD, 0)



