from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('file:///C:/Users/Administrator/Dropbox/python_autotest/new_selenium/lesson01/s1.html')
#进入链接页面
driver.find_element_by_link_text('转到百度').click_element()

#最大化
# driver.maximize_window()

# time.sleep(3)
#最小化
# driver.minimize_window()


#设置指定的大小--固定的尺寸
driver.set_window_size(800,600)

#获取窗口尺寸
size=driver.get_window_size()
print(f'高度是{size["height"]}')
print(f'宽度是{size["width"]}')

#获取元素的尺寸
btn=driver.find_element_by_id('su')
e_size=btn.size
print(f'按钮高度是{e_size["height"]}')
print(f'按钮宽度是{e_size["width"]}')
#元素坐标--原点是
e_loc=btn.location
print(f'元素坐标是X:{e_loc["x"]}Y:{e_loc["y"]}')


#获取窗口的位置--远点是屏幕左上角
loc=driver.get_window_position()
print(f'坐标是X:{loc["x"]}Y:{loc["y"]}')





input('.......')
driver.quit()