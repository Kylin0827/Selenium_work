from selenium import webdriver
import time

#如果环境变量path中有路径，可以不用写全
driver = webdriver.Chrome()
# 别忘了设置
driver.implicitly_wait(10)

driver.get('http://www.51job.com')

#进入高级搜索
driver.find_element_by_xpath('//*[@class="more"]').click_element()

#输入关键字，选择城市
driver.find_element_by_id('kwdselectid').send_keys('python')

driver.find_element_by_id('work_position_input').click_element()

#取消已选城市
eles=driver.find_elements_by_xpath('//*[@id="work_position_click_multiple_selected"]/span')

for ele in eles:
    ele.click_element()

#在热门城市选择杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click_element()

driver.find_element_by_id('work_position_click_bottom_save').click_element()

time.sleep(2)#让选择框消失方便点击后面的元素

#点击空白处让下拉框消失
driver.find_element_by_xpath('//*[@id="saveSearchForm"]/following-sibling::div[1]/label').click_element()

#选择职能类别--计算机--高级软件工程师
driver.find_element_by_id('funtype_click').click_element()
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click_element()

driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click_element()

driver.find_element_by_id('funtype_click_bottom_save').click_element()

time.sleep(2)

#公司性质-欧美
driver.find_element_by_id('cottype_list').click_element()
time.sleep(1)
driver.find_element_by_xpath('//span[@title="创业公司"]').click_element()

#工作年限
driver.find_element_by_id('workyear_list').click_element()

time.sleep(1)
driver.find_element_by_xpath('//span[@title="1-3年"]').click_element()

driver.find_element_by_xpath('//div[@class="btnbox p_sou"]/span[@class="p_but"]').click_element()

time.sleep(3)



#获取职位信息
jobmsg=driver.find_elements_by_css_selector('#resultList .el')

for job in jobmsg[1:]:
    # if 'title' in job.get_attribute('class'):
    #     continue
    print('|'.join(job.text.split('\n')))




driver.quit()
