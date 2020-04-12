# coding=utf-8
from selenium import webdriver
import  time


driver = webdriver.Chrome()
driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/new_selenium/lesson06/al.html')

#触发alert对话框
# driver.find_element_by_id('b1').click()

#切换到alert对象上面
# driver.switch_to.window()#切换窗口
# driver.switch_to.frame()# 切换frame
# al=driver.switch_to.alert
# al.accept()#调用确认方法，相当于点击确定

#触发comfirm对话框
# driver.find_element_by_id('b2').click()
# al=driver.switch_to.alert
# al.accept()
# al.dismiss()#点击取消

#触发promt对话框
driver.find_element_by_id('b3').click_element()

#切换到promt
al=driver.switch_to.alert

al.send_keys('测试输入')#向输入框输入字符
al.accept()#点击确定



# -------------------------------------
# input('press any key to quit...')
driver.quit()   # 浏览器退出