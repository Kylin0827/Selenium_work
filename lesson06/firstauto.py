import time

from selenium import webdriver
#文件名，模块名不要和现有的库名称相同
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r'D:\tools\webdrivers\chromedriver.exe')#谷歌浏览器
#webdriver.Firefox()#火狐浏览器
driver.implicitly_wait(10)#时间单位是秒<=设置的最大等待时间
#只作用于寻找元素

driver.get('https://www.baidu.com/')

ele=driver.find_element_by_id('kw')#获取元素对象

ele.send_keys('松勤')#输入框输入松勤

driver.find_element_by_id('su').click_element()#点击百度一下

#获取搜素结果并判断

# time.sleep(10)

#res=driver.find_element_by_id('1')
res=driver.find_element(By.ID,'1')

driver.implicitly_wait(1)
#下面还有寻找元素


if '松勤网 - 松勤软件测试' in res.text:
    print('pass')
else:
    print('fail')
    print(res.text)

#点击第一个搜索结果
driver.find_element_by_css_selector('[id="1"]>h3>a').click_element()

main_handle=driver.current_window_handle
#获取浏览器所有窗口的handle
handles=driver.window_handles
print(handles)

#要切换新的窗口
for handle in handles:
    driver.switch_to.window(handle)
    # if '松勤网 - 松勤软件测试' in driver.title:
    #     break

    if driver.find_elements_by_css_selector('span>a[href="/course/explore"]'):
        break


#进入松勤官网后，点击全部课程分类
driver.find_element_by_css_selector('span>a[href="/course/explore"]').click_element()

driver.switch_to.window(main_handle)#切回前一个窗口
time.sleep(3)


#模拟滚动页面
for  i in range(5):
    driver.execute_script('window.scrollBy(0,200)')
    time.sleep(1)
    if driver.find_element_by_css_selector('xxxx'):
        #do something找到这个目标元素之后做对应操作
        print()

#
# for  i in range(5):
#     driver.execute_script('window.scrollBy(0,-200)')
#     time.sleep(1)

driver.quit()


