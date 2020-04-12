import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost/mgr/ps/mgr/index.html#/')

def add_course():
    #点击添加课程
    driver.find_element_by_css_selector('[ng-click="showAddOne=true"]').click_element()
    #输入课程名称
    driver.find_element_by_css_selector('[ng-model="addData.name"]').send_keys('selenium课程')

    #输入课程描述
    driver.find_element_by_css_selector('[ng-model="addData.desc"]').send_keys('课程描述')

    #输入展示次序
    driver.find_element_by_css_selector('[ng-model="addData.display_idx"]').send_keys('1')

    #点击创建
    driver.find_element_by_css_selector('[ng-click="addOne()"]').click_element()

    time.sleep(3)

def delete_allCourse():


    #不停获取
    while True:
        delBtns = driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        if delBtns==[]:#课程全部删除，删除按钮没有了
            break
        #删除课程的具体过程
        delBtns[0].click_element()#每次删除第一个课程
        driver.find_element_by_css_selector('.btn-primary').click_element()
        time.sleep(1)#给弹出框消失的时间，防止点击下面的删除按钮点不到





if __name__ == '__main__':
    delete_allCourse()#初始化-清除课程
    add_course()
    delete_allCourse()#清除动作-清除测试产生的数据