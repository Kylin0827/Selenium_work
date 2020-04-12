import time

from selenium import webdriver

def setup():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.51job.com/')
    return driver

def input_keyword(driver):
    #关键字输入Python
    driver.find_element_by_id('kwdselectid').send_keys('python')


def adv_search(driver):
    #进入高级搜索
    driver.find_element_by_css_selector('.more').click_element()
    driver.find_element_by_id('kwdselectid').send_keys('python')
    driver.find_element_by_css_selector('[class="c c_h"]>label').click_element()
    # time.sleep(2)#让页面有反应时间
    #选择职能类别
    driver.find_element_by_id('funtype_click').click_element()
    driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click_element()
    driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click_element()
    driver.find_element_by_id('funtype_click_bottom_save').click_element()

    #选择公司性质-欧美
    driver.find_element_by_id('cottype_list').click_element()
    driver.find_element_by_css_selector('[title="外资（欧美）"]').click_element()

    #工作年限-1-3年
    driver.find_element_by_id('workyear_list').click_element()
    driver.find_element_by_css_selector('[title="1-3年"]').click_element()
    set_city(driver,'杭州')
    #点击搜索
    driver.find_element_by_css_selector('[class="btnbox p_sou"] span').click_element()



def set_city(driver,target_city):
    #选择目标城市-杭州
    driver.find_element_by_id('work_position_input').click_element()
    time.sleep(1)
    #删除已选择城市
    selected_cities=driver.find_elements_by_css_selector('#work_position_click_multiple_selected>span em')
    for city in selected_cities:
        city.click_element()
    time.sleep(1)
    #直接在热门城市选择杭州
    # driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
    #获取所有热门城市和指定城市名称判断
    cities=driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 td em')

    for city in cities:
        if target_city==city.text:
            print(city.text)
            city.click_element()
    time.sleep(1)


    driver.find_element_by_id('work_position_click_bottom_save').click_element()

    time.sleep(1)#为了弹出框消失



def get_jobs(driver):
    #输出搜索结果
    jobs=driver.find_elements_by_css_selector('#resultList .el')

    for job in jobs[1:]:
        # if 'title' in job.get_attribute('class'):
        #     continue
        msg=job.text.split('\n')
        print('|'.join(msg))


def teardown(driver):
    driver.quit()


if __name__ == '__main__':
    driver=setup()
    adv_search(driver)
    get_jobs(driver)
    teardown(driver)