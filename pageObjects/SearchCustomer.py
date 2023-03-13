import time
from selenium.webdriver.common.by import By

class SearchCustomer:

    tablesearch_xpath =  "(//div[@class='dataTables_scroll'])[1]"
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFname_xpath = "//input[@id='SearchFirstName']"
    txtLname_xpath = "//input[@id='SearchLastName']"
    BtnSearch_xpath = "//button[@id='search-customers']"

    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']/tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txtFname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFname_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLname_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.BtnSearch_xpath).click()

    def getNoofRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))
        #self.Rows = self.len(self.driver.find_element(By.XPATH, self.tableRows_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
            return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if Name == name:
                flag = True
                break
            return flag









