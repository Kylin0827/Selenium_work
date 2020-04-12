# coding:utf8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/new_selenium/lesson01/s1.html')

#获取窗口标题
print(driver.title)

#窗口URL
print(driver.current_url)



driver.quit()


