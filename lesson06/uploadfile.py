
from selenium import webdriver

import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)




#先到目标页面
driver.get('https://tinypng.com/')

#触发文件选择框
driver.find_element_by_css_selector('.icon').click_element()
time.sleep(3)#等待文件选择框弹出

#导入win32com  通常windows版本的Python都自带
import win32com.client
#构造shell对象，固定用法，建议直接复制
shell=win32com.client.Dispatch("WScript.Shell")
#调用Sendkeys方法，方法原理相当于闭眼睛敲键盘
#需要默认输入法设置成英文
shell.Sendkeys(r"d:\baidu.png"+'\n')#需注意回车符需要有转义效果










# driver.find_element_by_css_selector('.icon').click()
# time.sleep(2)
# # 直接发送键盘消息给 当前应用程序，
# # 前提是浏览器必须是当前应用
# #   pip install pypiwin32
#
# import win32com.client
#
# shell=win32com.client.Dispatch("WScript.Shell")
#
# shell.Sendkeys(r'd:\baidu.png'+'\n')





input('...')

driver.quit()