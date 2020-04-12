from selenium import webdriver
class BasePage():
    def open_browser(self):
        if self.driver==None:
            self.driver=webdriver.Chrome()
            self.driver.implicitly_wait(10)

    def close_browser(self):
        self.driver.close()

    def go_to(self,url):
        self.driver.get(url)

    def click(self,locator):
        self.driver.find_element(locator[0],locator[1]).click()

    def input(self,locator,text):
        ele=self.driver.find_element(locator[0],locator[1])
        ele.clear()
        ele.send_keys(text)

    def get_elements(self,locator):
        return self.driver.find_elements(locator[0],locator[1])