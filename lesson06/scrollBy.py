
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://news.baidu.com/')

#一边滑动一边查找元素---循环
#不知道滑动多少次---无限循环
while True:
    driver.execute_script('window.scrollBy(0,200)')
    #需要循环结束条件是找到目标元素
    targeteles=driver.find_elements_by_css_selector('#guonei .l-left-col>ul:nth-child(1)>li:nth-child(1) a')
    if targeteles:#如果找到了这个元素
        targeteles[0].click_element()
        break#


input('xxxxxxx')
driver.quit()