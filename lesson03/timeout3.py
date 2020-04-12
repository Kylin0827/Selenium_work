# coding:utf8
import time

from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(3)

driver.get('http://www.baidu.com')


element_keyword = driver.find_element_by_id("kw")
element_keyword.send_keys('松勤\n')

#对常规操作的最大等待时间不能超过3秒
driver.find_element_by_id('xxxx')#花费的时间》3


#代码执行速度要快于网页加载速度
driver.find_element_by_id('1')

driver.implicitly_wait(60)
#有特殊的业务，60s
driver.find_element_by_id('1')
driver.find_element_by_id('2')
driver.find_element_by_id('3')
driver.implicitly_wait(3)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ele = WebDriverWait(driver,60). until(EC.presence_of_element_located((By.CLASS_NAME,'username')))

#当元素可以被点击时，进入下一步，最大等待时间60，秒
ele1 = WebDriverWait(driver,60). until(EC.element_to_be_clickable((By.CLASS_NAME,'username')))






# ================================
driver.quit()

