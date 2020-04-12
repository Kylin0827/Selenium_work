from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# 别忘了设置
driver.implicitly_wait(10)

driver.get('http://www.51job.com')

#进入高级搜索
driver.find_element_by_css_selector('[class="more"]').click_element()

#输入关键字python
driver.find_element_by_id('kwdselectid').send_keys('python')

#点击空白区域，取消提示框
driver.find_element_by_css_selector('.tit>span').click_element()

#选择城市
driver.find_element_by_id('work_position_input').click_element()
time.sleep(2)

#找到所有已选城市并取消
selected_cities=driver.find_elements_by_css_selector('#work_position_click_multiple_selected>span')

for one in selected_cities:
    one.click_element()

#找到杭州选择
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click_element()


#点击确定按钮
driver.find_element_by_id('work_position_click_bottom_save').click_element()


#选择职能类别
driver.find_element_by_id('funtype_click').click_element()
time.sleep(1)
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click_element()
time.sleep(1)
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click_element()

driver.find_element_by_id('funtype_click_bottom_save').click_element()

#选择公司类型
driver.find_element_by_id('cottype_list').click_element()
time.sleep(1)
driver.find_element_by_css_selector('span[title="外资（欧美）"]').click_element()

#选择公司年限
driver.find_element_by_id('workyear_list').click_element()
time.sleep(1)
driver.find_element_by_css_selector('span[title="1-3年"]').click_element()

#开始搜搜
driver.find_element_by_css_selector('.p_sou span[onclick*="kwdGoSearch"]').click_element()



time.sleep(5)#为了信息加载完

#查询工作
jobs=driver.find_elements_by_css_selector('#resultList>.el')

for job in jobs[1:]:

    msg=job.text.split('\n')
    print(msg)
    print('|'.join(msg))


driver.quit()


