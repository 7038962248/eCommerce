import time

from pageObjects.LoginPage import Login

class Logout:
    def __init__(self,driver):
        self.driver = driver

    def test_logout01(self,setup):
        self.driver = setup
        print(self.driver.title)
        self.lp = Login(self.driver)
        self.lp.clickLogout()
        time.sleep(5)
        self.driver.close()
