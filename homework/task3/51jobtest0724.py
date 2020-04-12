from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
# 别忘了设置
driver.implicitly_wait(10)

driver.get('http://www.51job.com')

#输入python
driver.find_element_by_id('kwdselectid').send_keys('python')


#选择城市
driver.find_element_by_id('work_position_input').click_element()
time.sleep(2)

#找到所有已选城市并取消
selected_cities=driver.find_elements_by_css_selector('#work_position_click_multiple_selected>span')

for one in selected_cities:
    one.click_element()

#找到杭州选择
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click_element()

#思路2 比较热门城市文本
# eles=driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 td')
# for ele in eles:
#     if ele.text == '杭州':
#         ele.click()

driver.find_element_by_id('work_position_click_bottom_save').click_element()
time.sleep(2)

#搜索
driver.find_element_by_css_selector('.ush button').click_element()


time.sleep(5)#为了信息加载完

#查询工作
jobs=driver.find_elements_by_css_selector('#resultList>.el')

for job in jobs[1:]:
    # t1=job.find_element_by_class_name('t1')
    # t2=job.find_element_by_class_name('t2')
    # t3=job.find_element_by_class_name('t3')
    # t4=job.find_element_by_class_name('t4')
    # t5=job.find_element_by_class_name('t5')
    msg=job.text.split('\n')
    print('|'.join(msg))


driver.quit()
