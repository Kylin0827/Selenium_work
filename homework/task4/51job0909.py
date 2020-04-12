from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome()
# 别忘了设置
driver.implicitly_wait(10)

driver.get('https://www.51job.com/')


#进入高级搜索
driver.find_element_by_css_selector('.more').click_element()

#职位搜索python
driver.find_element_by_id('kwdselectid').send_keys('python')

#选择城市
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

#点击空白取消下拉菜单
driver.find_element_by_css_selector('#saveSearchForm+div>label').click_element()

#选择职能
driver.find_element_by_id('funtype_click').click_element()
time.sleep(1)
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click_element()
time.sleep(1)
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click_element()
driver.find_element_by_id('funtype_click_bottom_save').click_element()
time.sleep(1)

#公司性质
driver.find_element_by_id('cottype_list').click_element()
driver.find_element_by_css_selector('#cottype_list .ul span[title="外资（欧美）"]').click_element()
time.sleep(1)

#选择工作年限
driver.find_element_by_id('workyear_list').click_element()
driver.find_element_by_css_selector('#workyear_list .ul span[title="1-3年"]').click_element()

#确定搜索
driver.find_element_by_css_selector('.btnbox>.p_but').click_element()

#判断页面是否加载好
driver.find_element_by_css_selector('.mainleft')

#获取职位信息：
eles=driver.find_elements_by_css_selector('#resultList div.el')

for ele in eles[1:]:
    # if ele.get_attribute('class').contain('title'):
    #     continue
    # print(ele.text)
    msg=ele.text.split('\n')
    print('|'.join(msg))

driver.quit()