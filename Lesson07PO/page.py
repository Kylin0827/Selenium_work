#先写出具体的业务逻辑--比如登录

#再将写好的逻辑封装到类里面

#继续构造其他的页面类

#将这些类共同的功能抽象化父类，被其他业务类继承

#可以将代码内部的具体元素抽离出来用外部的配置文件进行管理
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#实现BasePage类用于封装公共方法
import conf_util
class BasePage():
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)

    #点击操作--知道元素的定位方法
    def click_element(self, locator):
        self.driver.find_element(locator[0],locator[1]).click()

    #输入操作--知道元素的定位方法还有文本
    def input_text(self,locator,text):
        self.driver.find_element(locator[0], locator[1]).send_keys(text)

    #获取元素-复数形式
    def get_webelements(self,locator):
        return self.driver.find_elements(locator[0],locator[1])


class LoginPage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        LoginPage=conf_util.get_locators('locators.yml')['LoginPage']
        # 进入登录页面
        self.driver.get('http://localhost/mgr/login/login.html')
        #用户名输入框
        self.username_input=LoginPage['username']
        #密码输入框
        self.password_input=LoginPage['password']
        #登录按钮
        self.login_btn= LoginPage['login_btn']

    def login(self,username,password):
        #输入用户名和密码
        self.input_text(self.username_input,username)
        self.input_text(self.password_input,password)
        #点击登录
        self.click_element(self.login_btn)

        #关闭浏览器
        # driver.quit()

        #返回下一个流程的页面--课程页面
        return CoursePage(self.driver)


#课程页面类
class CoursePage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        #初始化方法里面打开浏览器并且访问该页面的URL
        # self.driver.get('http://localhost/mgr/ps/mgr/index.html#/')
        #不用获取webelement,把元素定位的方法-表达式给页面的属性

        #添加课程按钮
        self.addCourseBtn='css selector','[ng-click="showAddOne=true"]'
        # 课程名称
        self.courseName = 'css selector','[ng-model="addData.name"]'
        # 课程描述
        self.courseDesc='css selector','[ng-model="addData.desc"]'
        # 展示次序
        self.courseIdx='css selector','[ng-model="addData.display_idx"]'
        # 创建按钮
        self.createBtn='css selector','[ng-click="addOne()"]'

        #确认按钮
        self.confirmBtn='css selector','.btn-primary'

        #所有删除按钮
        self.delBtns='css selector','[ng-click="delOne(one)"]'

    #返回课程页面
    def get_coursePage(self):
        #确保浏览器访问课程页面
        self.driver.get('http://localhost/mgr/ps/mgr/index.html#/')
        #返回这个页面对象-coursePage
        return self

    def add_Course(self,name,desc,idx):
        # 点击添加课程
        self.click_element(self.addCourseBtn)

        # 输入课程名称
        self.input_text(self.courseName,name)

        # 输入课程描述
        self.input_text(self.courseDesc,desc)
        # 输入展示次序
        self.input_text(self.courseIdx,idx)
        # 点击创建
        self.click_element(self.createBtn)

    def delete_allCourse(self):
        self.driver.implicitly_wait(1)
        # 不停获取
        while True:
            delBtns = self.get_webelements(self.delBtns)
            if delBtns == []:  # 课程全部删除，删除按钮没有了
                break
            # 删除课程的具体过程
            delBtns[0].click()  # 每次删除第一个课程
            self.click_element(self.confirmBtn)
            time.sleep(1)  # 给弹出框消失的时间，防止点击下面的删除按钮点不到
        self.driver.implicitly_wait(10)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    lp=LoginPage(driver)
    cp=lp.login('auto','sdfsdfsdf')
    cp.delete_allCourse()
    cp.add_Course('初中化学','课程描述',2)
    cp.delete_allCourse()


