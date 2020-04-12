# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# ----------------------------------
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

#刷新
driver.refresh()

#前进
driver.forward()


#后退
driver.back()








# ----------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出