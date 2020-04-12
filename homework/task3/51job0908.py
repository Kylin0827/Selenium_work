from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome()
# 别忘了设置
driver.implicitly_wait(10)

driver.get('https://www.51job.com/')

driver.find_element_by_id('kwdselectid').send_keys('python')

driver.find_element_by_id('work_position_input').click_element()

time.sleep(1)#让页面有时间发生变化，

#清除已经选择的地区
eles=driver.find_elements_by_css_selector('#work_position_click_multiple_selected span.ttag')
for ele in eles:
    ele.click_element()

#选择杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click_element()

#点击确定按钮
driver.find_element_by_id('work_position_click_bottom_save').click_element()
time.sleep(1)

driver.find_element_by_css_selector('.ush button').click_element()

#获取职位信息：
eles=driver.find_elements_by_css_selector('#resultList div.el')

for ele in eles[1:]:
    # if ele.get_attribute('class').contain('title'):
    #     continue
    # print(ele.text)
    msg=ele.text.split('\n')
    print('|'.join(msg))

driver.quit()