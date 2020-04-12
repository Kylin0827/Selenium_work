import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://demo.crccmall.com/static/crccmall/#/register?tdsourcetag=s_pcqq_aiomsg')

source=driver.find_element_by_css_selector('.ant-row:nth-child(4) .ant-form-item-control>div div:nth-child(3)')
ele=driver.find_element_by_css_selector('.ant-row:nth-child(4) .ant-form-item-control>div')
pos=ele.location
size=ele.size

x=pos['x']+size['width']
y=pos['y']+size['height']

ac=ActionChains(driver)
ac.drag_and_drop_by_offset(source,x,y).perform()


time.sleep(10)
driver.quit()