# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/new_selenium/lesson05/s1.html')

ele=driver.find_element_by_id('many')

eles=ele.find_elements_by_xpath('.//span')
eles2=ele.find_elements_by_xpath('//span')#不加点表示在整个HTML范围
print(len(eles))
print(len(eles2))

driver.quit()

