# coding=utf-8
import time

from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('https://www.baidu.com/')

print(driver.title)
driver.find_element_by_id('kw').send_keys('松勤\n')

#点击第一个链接进入松勤官网
driver.find_element_by_css_selector('[id="1"]>h3>a').click_element()

#点击全部课程
# driver.find_element_by_css_selector('span>[href="/course/explore"]').click()

print(driver.window_handles)
for handle in driver.window_handles:
    #切换新窗口
    driver.switch_to.window(handle)
    #判断当前窗口的特征是否为目标窗口
    eles=driver.find_elements_by_css_selector('span>[href="/course/explore"]')
    if eles:
        eles[0].click_element()#点击全部课程
        break

# driver.switch_to.window()




driver.quit()

