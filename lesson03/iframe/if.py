# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/autoUI_selenium/iframe/if.html')

driver.switch_to.frame('baidu')
driver.find_element_by_id('kw').send_keys('松勤\n')

#切回主HTML
driver.switch_to.default_content()
driver.find_element_by_tag_name('input')





input('press any key to quit...')
driver.quit()