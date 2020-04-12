# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/iframe/nested.html')

driver.switch_to.frame('layer2')#切内1层
driver.switch_to.frame('layer3')#切内2层

# driver.find_element_by_id('button-layer3').click()
driver.find_element_by_tag_name('input').send_keys('内2层')


#切回主HTML
# driver.switch_to.default_content()
# driver.switch_to.frame('layer2')#切内1层

driver.switch_to.parent_frame()#切回上一层
driver.find_element_by_tag_name('input').send_keys('内1层')

input('press any key to quit...')
driver.quit()