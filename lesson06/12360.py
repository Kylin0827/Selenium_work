from selenium  import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

#出发地目的地
ele=driver.find_element_by_id('fromStationText')
ele.click_element()
ele.send_keys('南京南\n')

ele=driver.find_element_by_id('toStationText')
ele.click_element()
ele.send_keys('杭州东\n')

#操作发车时间
select=Select(driver.find_element_by_id('cc_start_time'))
select.select_by_visible_text('06:00--12:00')

#选择发车日期-当前时间第二天
driver.find_element_by_xpath('//*[@id="date_range"]//li[2]').click_element()

#筛选出二等座有做的车次
#//*[@id="queryLeftTable"]/tr/td[4][@class]/preceding-sibling::td[last()]//a

#//*[@id="queryLeftTable"]/tr/td[4][@class]/../td[1]//a

eles=driver.find_elements_by_xpath('//*[@id="queryLeftTable"]/tr/td[4][@class]/../td[1]//a')

print('符合条件的车次信息有：')

for ele in eles:
    print(ele.text)


driver.quit()
