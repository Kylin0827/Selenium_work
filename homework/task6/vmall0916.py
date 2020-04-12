import random
import time

from selenium import  webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

#华为商城
driver.get('https://www.vmall.com/')

#打开华为消费者官网
driver.find_element_by_css_selector('[href="http://consumer.huawei.com/cn/"]').click_element()


def check_consumer():
    eles=driver.find_elements_by_css_selector('ul[class="clearfix nav-cnt"]>li>a')
    msg='|'.join([ele.text for ele in eles])
    expect='''  智能手机
  笔记本
  平板
  穿戴设备
  智能家居
  更多产品
  软件应用
  服务与支持'''
    expect='|'.join([txt.strip() for txt in expect.split('\n')])
    print(expect)
    if msg=='':
        print('pass')
    else:
        print('fail')
        print(msg)


def check_vmall():
    ac=ActionChains(driver)
    target_ele=driver.find_element_by_id('zxnav_1')
    ac.move_to_element(target_ele).perform()#必须调用perform
    time.sleep(1)
    eles=driver.find_elements_by_css_selector('#zxnav_1>div.category-panels>ul span')
    msg='|'.join([ele.text for ele in eles])
    if msg=='平板电脑|笔记本电脑|笔记本配件':
        print('pass')
    else:
        print('fail')
        print(msg)


#窗口切换
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '华为商城' in driver.title:
        check_vmall()
    elif '华为消费者业务官网' in driver.title:
        check_consumer()




driver.quit()