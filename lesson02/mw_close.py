import time

from selenium  import webdriver

driver=webdriver.Chrome()

driver.get('https://music.163.com/')
#改变窗口的大小

driver.maximize_window()#将窗口最大化


#指定窗口大小
driver.set_window_size(800,600)
# driver.set_window_size(3000,2000)


#如果只想改变高度或者宽度呢？

size=driver.get_window_size()
width=size['width']
height=size['height']

#设置窗口高度为原来的1/2
driver.set_window_size(width,height/2)






driver.quit()



