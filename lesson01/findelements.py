import time

from selenium import webdriver
#文件名，模块名不要和现有的库名称相同
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r'D:\tools\webdrivers\chromedriver.exe')#

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/new_selenium/lesson01/s1.html')


# eles=driver.find_elements_by_tag_name('button1')
# print(eles)
# for ele in eles:
#     print(ele.text)

#通过webelement选择元素
ele=driver.find_element_by_id('food')
# ele1=ele.find_element_by_class_name('vegetable')
# ele1=ele.find_element_by_tag_name('span')
# print(ele1.text)
# print(ele1.get_attribute('outerHTML'))
#范围是当前元素的所有后代元素
spans=ele.find_elements_by_tag_name('span1')
print(spans)
for span in spans:
    print(span.get_attribute('outerHTML'))

print('-------------')

#范围是当前整个HTML
# spans2=driver.find_elements_by_tag_name('span')
# for span in spans2:
#     print(span.get_attribute('outerHTML'))
driver.quit()


