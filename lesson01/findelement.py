import time

from selenium import webdriver
#文件名，模块名不要和现有的库名称相同
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r'D:\tools\webdrivers\chromedriver.exe')#

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/new_selenium/lesson01/s1.html')

#根据Name查找元素

# btn=driver.find_elements_by_name('buttonfsdfsd')
#
#
# print(btn)
#
# if btn:
#     print('找到元素了')
# else:
#     print('没有这个元素')

# btns=driver.find_elements_by_name('button')

# print(btn[0].text)
# print(btn[1].text)
# for btn in btns:
#     print(btn.text)

#通过class找元素
# ele=driver.find_element_by_class_name('cheese')
# print(ele.text)

# eles=driver.find_elements_by_class_name('cheese1')
# print(eles)
# for ele in eles:
#     print(ele.text)

#根据tag找元素
# ele=driver.find_element_by_tag_name('button')
# print(ele.text)
# eles=driver.find_elements_by_tag_name('button')
# print(eles)
# for ele in eles:
#     print(ele.text)

#根据超链接定位元素
# driver.find_element_by_link_text('转到百度').click()

# ele=driver.find_element_by_partial_link_text('百度2')#根据部分超链接文本定位元素
#
# print(ele.get_attribute('href'))

#获取元素html源码
ele=driver.find_element_by_id('many')
# print(ele.get_attribute('innerHTML'))
# print(ele.get_attribute('outerHTML'))



#通过上层元素找子元素
ps=ele.find_elements_by_tag_name('p')
for p in ps:
    print(p.get_attribute('outerHTML'))



input('输入任意键退出。。。。。')



driver.quit()