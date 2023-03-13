import time
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
import string
import random

class Test_addCustomer:
    baseURL = ReadConfig.getApplicationURL()
    #email = "sry123@gmail.com"
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer_04(self,setup):
        self.logger.info("********Test_003_AddCustomer*********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()
        self.addcust.clickonAddnew()

        self.logger.info("******** Providing customer info *********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("Sry@03")
        self.addcust.setFirstname("Shreya")
        self.addcust.setLastname("Kumar")
        self.addcust.setGender("Female")
        self.addcust.setDOB("10/02/2023")
        self.addcust.setCompanyName("SwipeTech")
        self.addcust.setNewsLetter("Your store name")
        self.addcust.setCustomerRole("Registered")
        self.addcust.setManagerOfVendor("2")
        self.addcust.setAdminCmt("This is for testing.........")
        self.addcust.clickOnSave()

        self.logger.info("******** 1st Add customer Validation  *********")
        if "Customers / nopCommerce administration" == self.driver.title:
            assert True
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_AddCustomer_SS.png")
            self.logger.info("******** Add customer Test Pass *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Test_AddCustomer_SS.png")
            self.logger.info("******** Add customer Test Fail *********")
            assert False

        self.logger.info("******** 2st Add customer Validation  *********")
        self.massage = self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/div[1]").text
        print("Massage : ", self.massage)
        if "The new customer has been added successfully." in self.massage:
            assert True == True
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_AddCustomer_SS.png")
            self.logger.info("******** Add customer Test Pass *********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_AddCustomer_SS.png")
            self.logger.info("******** Add customer Test Fail *********")
            assert True == False
        time.sleep(10)
        self.driver.close()
        self.logger.info("******** Add customer TestCase Ended *********")



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# self.massage = self.driver.find_element(By.XPATH, "(//div[@class='alert alert-success alert-dismissable'])[1]").text
# print("Massage : ", self.massage)
# assert self.massage == " The new customer has been added successfully. "
