# coding:utf8
import time

from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
# 别忘了设置
driver.implicitly_wait(10)

# 打开网址
driver.get('http://www.51job.com')

#点击高级搜索
driver.find_element_by_css_selector('a[href*="advance_search"]').click_element()

time.sleep(1)

#输入选择关键字python
driver.find_element_by_id('kwdselectid').send_keys('python')

#选择地区
driver.find_element_by_id('work_position_input').click_element()
time.sleep(1)

#获取所有城市
cityeles=driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')

for one in cityeles:
    cityName=one.text
    selected=one.get_attribute('class')
    if selected =='on':
        if cityName !='杭州':
            one.click_element()
    else:
        if cityName =='杭州':
            one.click_element()

#保存选择
driver.find_element_by_id('work_position_click_bottom_save').click_element()
#点击空白
driver.find_element_by_xpath('//div[@class="c c_h"]/label').click_element()
#选择职能类型
driver.find_element_by_id('funtype_click').click_element()
time.sleep(1)
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click_element()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click_element()

driver.find_element_by_id('funtype_click_bottom_save').click_element()

#选择公司性质
driver.find_element_by_id('cottype_list').click_element()
driver.find_element_by_css_selector('#cottype_list>.ul>span[title="外资（欧美）"]').click_element()

#选择工作年限
driver.find_element_by_id('workyear_list').click_element()
driver.find_element_by_css_selector('#workyear_list>.ul>span[title="1-3年"]').click_element()

#点击搜索
driver.find_element_by_xpath('//*[@class="btnbox p_sou"]/span').click_element()

#搜索结果分析
jobs=driver.find_elements_by_css_selector('#resultList div[class=el]')

for job in jobs:
    # if 'title' in job.get_attribute('class'):
    #     continue
    fields=job.find_elements_by_tag_name('span')
    strField= [field.text for field in fields]
    print('|'.join(strField))

driver.quit()















