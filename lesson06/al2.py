# coding=utf-8
from selenium import webdriver
import  time


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('http://ci.ytesting.com/student/login/login.html')

# ----------------------------------


# ----------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出