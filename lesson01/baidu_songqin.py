import time

from selenium  import webdriver

def search_sq():
    #初始化Chomedriver---打开浏览器
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)#隐式等待，针对webdriver,webelement,共享等待时间

    #输入网页-到指定页面
    driver.get('https://www.baidu.com/')

    #找元素，操作元素
    ele=driver.find_element_by_id('kw')

    ele.send_keys('松勤\n')


    #判断当前搜索页面有没有 松勤网 - 松勤软件测试搜索结果
    a=driver.find_element_by_id('1').find_element_by_tag_name('a')

    # 保存开始页面的handles
    baidu_handle = driver.current_window_handle

    if '松勤网 - 松勤软件测试' in a.text:
        print('pass')
        a.click_element()#如果判断正确就点进去第一链接
        #切换webdriver到新的窗口
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            #判断页面的标题
            if '松勤网 - 松勤软件测试' in driver.title:
                break

        driver.find_element_by_link_text('全部课程分类').click_element()
    else:
        print('fail')
        print(a.text)
    #切回百度页面
    driver.switch_to.window(baidu_handle)
    time.sleep(3)
    driver.refresh()

    time.sleep(10)
    driver.quit()#关闭浏览器并退出chromedriver



if __name__ == '__main__':
    search_sq()
