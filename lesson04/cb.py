# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# 打开网址
driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/new_selenium/lesson04/cb.html')


bike=driver.find_element_by_css_selector('[value="bike"]')
car=driver.find_element_by_css_selector('[value="car"]')
plane=driver.find_element_by_css_selector('[value="plane"]')

if not plane.is_selected():
    plane.click_element()

if not car.is_selected():
    car.click_element()

if not bike.is_selected():
    bike.click_element()

input('press any key to quit...')
driver.quit()   # 浏览器退出