import time
from basepage import BasePage
from commonlib import load_eles
class CoursePage(BasePage):
    def __init__(self,driver):
        self.driver=driver
        self.go_to('http://localhost/mgr/ps/mgr/index.html#/')
        self.locators=load_eles('CoursePage')

        self.course_btn=self.locators['course_btn']
        self.show_add_btn=self.locators['show_add_btn']
        self.name_text=self.locators['name_text']
        self.desc_text=self.locators['desc_text']
        self.idx_text=self.locators['idx_text']
        self.add_btn=self.locators['add_btn']
        self.del_btns=self.locators['del_btns']
        self.confirm_btn=self.locators['confirm_btn']

    def add_course(self,name,desc,idx):
        self.click(self.course_btn)
        time.sleep(1)
        self.click(self.show_add_btn)

        self.input(self.name_text,name)
        self.input(self.desc_text,desc)
        self.input(self.idx_text,idx)

        self.click(self.add_btn)


    def deleteAllCourse(self):
        self.driver.implicitly_wait(1)
        while 1:
            #获取所有删除按钮
            del_btns = self.get_elements(self.del_btns)
            #如果删除所有课程，就退出
            if del_btns == []:
                break
            #每次都操作第一个删除按钮
            del_btns[0].click_element()
            #点击确认
            self.click(self.confirm_btn)
            time.sleep(1)
        self.driver.implicitly_wait(10)