# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson04/rb.html')

male=driver.find_element_by_css_selector('[value="male"]')

female=driver.find_element_by_css_selector('[value="female"]')

other=driver.find_element_by_css_selector('[value="other"]')

#选择单选框
female.click_element()

male.click_element()

other.click_element()

#判断是否被选择
print(male.is_selected())
print(female.is_selected())
print(other.is_selected())













# input('press any key to quit...')
driver.quit()   # 浏览器退出