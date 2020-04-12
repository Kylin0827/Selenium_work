from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://vip.ytesting.com/loginController.do?login')

import winsound
winsound.Beep(1500,3000)


randcode=input('请输入验证码....')
driver.find_element_by_id('randCode').send_keys(randcode)




input('....')
driver.quit()