import time

from selenium import webdriver

class  webOpAdmin():

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://localhost/mgr/ps/mgr/index.html#/')

    #操作删除课程
    #1.点击删除按钮

    def del_all_lessons(self):

        self.driver.implicitly_wait(1)
        while 1:
            del_btns = self.driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')


            if del_btns==[]:
                break
            del_btns[0].click_element()#取第一个元素操作
            self.driver.find_element_by_css_selector('.btn-primary').click_element()
            time.sleep(1)

        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    webop=webOpAdmin()
    webop.setUp()
    webop.del_all_lessons()
    webop.teardown()