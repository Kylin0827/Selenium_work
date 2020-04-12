# -*- coding: utf-8 -*-
import time

from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson04/input1.html') # 打开网址



input1=driver.find_element_by_id('input1')
ta=driver.find_element_by_id('ta1')

# print(ta.get_attribute('placeholder'))

ta.send_keys('呵呵')
ta.clear()
ta.send_keys('123123123123')
print(ta.get_attribute('value'))
































# input('press any key to quit...')
driver.quit()