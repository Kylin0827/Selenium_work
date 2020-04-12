from basepage import BasePage
from commonlib import load_eles
class LoginPage(BasePage):


    def __init__(self,driver):
        self.driver=driver
        self.go_to('http://localhost/mgr/login/login.html')
        self.locators=load_eles('LoginPage')

        self.user = self.locators['user']
        self.passwd = self.locators['passwd']
        self.login_btn = self.locators['login_btn']

    def login(self,username,password):

        self.input(self.user,username)
        self.input(self.passwd,password)
        self.click(self.login_btn)
