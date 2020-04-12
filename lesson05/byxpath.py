# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/new_selenium/lesson04/s1.html')



food=driver.find_element_by_id('food')

eles=food.find_elements_by_xpath('.//span')
eles2=driver.find_elements_by_xpath('//span')
print(len(eles))
print(len(eles2))


# raw_input('press any key to quit...')
driver.quit()

