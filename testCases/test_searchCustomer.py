import time
import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer

class Test_searchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail_05(self,setup):
          self.logger.info("***** Search customer by email_004 ******")
          self.driver = setup
          self.driver.get(self.baseURL)
          self.driver.maximize_window()
          self.lp = Login(self.driver)
          self.lp.setUserName(self.username)
          self.lp.setPassword(self.password)
          self.lp.clickLogin()
          self.logger.info("**** Login Successful ****")

          self.logger.info("**** Starting search customer by email ****")

          self.addCust = AddCustomer(self.driver)
          self.addCust.clickonCustomerMenu()
          self.addCust.clickonCustomerMenuItem()

          self.searchCust = SearchCustomer(self.driver)
          self.searchCust.setEmail("victoria_victoria@nopCommerce.com")
          self.searchCust.clickSearch()
          time.sleep(6)
          status = self.searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
          self.logger.info("it done ")
          assert True == status

          self.logger.info("****** Tc_search customer by email_004 finished ******")









