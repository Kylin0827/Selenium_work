import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.51job.com/')

#关键字输入Python
driver.find_element_by_id('kwdselectid').send_keys('python')

#选择目标城市-杭州
driver.find_element_by_id('work_position_input').click_element()

#删除以选择城市
selected_cities=driver.find_elements_by_css_selector('#work_position_click_multiple_selected>span')
for city in selected_cities:
    city.click_element()

#直接在热门城市选择杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click_element()

driver.find_element_by_id('work_position_click_bottom_save').click_element()


time.sleep(1)#为了弹出框消失

#点击搜索
driver.find_element_by_css_selector('.ush.top_wrap button').click_element()




#输出搜索结果
jobs=driver.find_elements_by_css_selector('#resultList .el')

for job in jobs[1:]:
    # if 'title' in job.get_attribute('class'):
    #     continue
    msg=job.text.split('\n')
    print('|'.join(msg))

driver.quit()