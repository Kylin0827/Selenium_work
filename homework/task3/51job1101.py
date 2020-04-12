from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome()
# 别忘了设置
driver.implicitly_wait(10)

driver.get('http://www.51job.com')

#输入关键字Python
driver.find_element_by_id('kwdselectid').send_keys('python')



#选择地区
driver.find_element_by_id('work_position_input').click_element()

time.sleep(3)
#选择杭州，并且取消不是杭州的城市

selected=driver.find_elements_by_css_selector('#work_position_click_multiple_selected span.ttag')
#取消所有已经选择的城市
for se in selected:
    se.click_element()

#直接选择杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click_element()

#点击确定
driver.find_element_by_id('work_position_click_bottom_save').click_element()

#保证弹出框消失再操作
time.sleep(2)

#点击搜索
driver.find_element_by_css_selector('.ush button').click_element()


#获取职位信息
jobmsg=driver.find_elements_by_css_selector('#resultList .el')

for job in jobmsg[1:]:
    # if 'title' in job.get_attribute('class'):
    #     continue
    print('|'.join(job.text.split('\n')))




driver.quit()
