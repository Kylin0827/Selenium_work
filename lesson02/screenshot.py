import time

from selenium  import webdriver
from selenium.common.exceptions import NoSuchElementException


def search_sq(driver):

    #输入网页-到指定页面
    driver.get('https://www.baidu.com/')

    #截取百度一下按钮
    btn=driver.find_element_by_id('su')
    btn.screenshot('baidu_btn.png')

    #找元素，操作元素
    ele=driver.find_element_by_id('kw')

    ele.send_keys('松勤\n')

    time.sleep(10)
    driver.quit()#关闭浏览器并退出chromedriver



if __name__ == '__main__':
    try:
        # 初始化Chomedriver---打开浏览器
        driver = webdriver.Chrome()
        search_sq(driver)
    except NoSuchElementException:
        #截屏
        driver.get_screenshot_as_file(r'd:\baidu.png')
        driver.quit()

