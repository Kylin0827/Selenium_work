import time

from selenium import webdriver
import win32api
import win32con

driver=webdriver.Chrome()
driver.get('https://music.163.com/')
driver.switch_to.frame('g_iframe')
driver.find_element_by_css_selector('#discover-module .g-wrap3 .n-rcmd .v-hd2').click_element()
time.sleep(1)
#模拟向下滚动页面20次
for i in range(20):
    win32api.keybd_event(win32con.VK_DOWN, 0)
    time.sleep(0.5)

input('xxxxxxx')
driver.quit()