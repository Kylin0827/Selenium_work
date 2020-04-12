from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://mail.qq.com/')

#切进Frame
# driver.switch_to.frame('login_frame')
driver.switch_to.frame(1)

driver.find_element_by_id('switcher_plogin').click_element()

#如果要操作frame外面的元素，就要切回主HTML
driver.switch_to.default_content()


input('.......')
driver.quit()

