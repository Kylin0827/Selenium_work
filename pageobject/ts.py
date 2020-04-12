from selenium import webdriver
from coursepage import CoursePage
from loginpage import LoginPage
import unittest


class webTest(unittest.TestCase):
    def setUp(self):  # 初始化
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.cp = CoursePage(self.driver)
        self.lp = LoginPage(self.driver)

    def test(self):  # 用例主体
        self.lp.login('auto', 'sdfsdfsdf')
        self.cp.deleteAllCourse()
        self.cp.add_course('初中语文', '语文课', '1')

    def tearDown(self):  # 清除环境
        self.cp.deleteAllCourse()
        self.driver.close()



if __name__ == '__main__':
    unittest.main()