import time

from selenium import webdriver

driver=webdriver.Chrome(r'D:\tools\webdrivers\chromedriver.exe')

driver.implicitly_wait(3)

driver.get('https://mail.qq.com')

frame=driver.find_element_by_id('login_frame')
driver.switch_to.frame(frame)

driver.find_element_by_id('q_low_login_enable').click_element()

driver.switch_to.default_content()#回到主HTML
driver.find_element_by_class_name('header_logo').click_element()

driver.quit()