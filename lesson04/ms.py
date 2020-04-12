# coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/lesson04/ms.html') # 打开网址



#多选框
multi=Select(driver.find_element_by_id('multi'))

multi.select_by_visible_text('奔驰S300')
multi.select_by_visible_text('雅阁')
multi.select_by_visible_text('奥迪A6')

time.sleep(5)

multi.deselect_by_visible_text('雅阁')

#取消所有选择的

multi.deselect_all()


#操作下拉框
select=Select(driver.find_element_by_id('single'))

select.select_by_visible_text('男')
time.sleep(2)
select.select_by_visible_text('请选择性别')
time.sleep(2)

input('press any key to quit...')
driver.quit()   # 浏览器退出