import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from testCases.test_logout import Logout
from utilities import XLUtils

class Test_002_DDT_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username = "admin@yourstore.com"
    # password = "admin"
    baseURL = ReadConfig.getApplicationURL()

    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle_01(self,setup):
        #self.driver = webdriver.Chrome()
        self.logger.info("********Test_001_Login*********")
        self.logger.info("*********** Verifying Home Page Title ***************")

        self.driver = setup
        self.driver.get(self.baseURL)
        Ac_Title = self.driver.title


        if Ac_Title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******** Home page title test is pass **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("******** Home page title test is fail **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_02(self, setup):
        # self.driver = webdriver.Chrome()
        self.logger.info("*********** Test_002_DDT_Login ************")
        self.logger.info("******** Verifying login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        Ac_title = self.driver.title

        if Ac_title =="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******** Login test is pass **********")
            #self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("******** Login test is fail **********")
            assert False

        self.lp.clickLogout()
        time.sleep(3)






