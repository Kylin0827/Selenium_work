# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson05/xpath.html')


ele=driver.find_element_by_xpath('//*[@id="pork"]/..')
print(ele.get_attribute('outerHTML'))
print(ele.text.split()[0])


driver.quit()

