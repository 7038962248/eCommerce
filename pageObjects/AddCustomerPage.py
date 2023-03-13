import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:

    lnk_Customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_Customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),' Customers')]"
    btnAddnew_xpath = "//i[@class='fas fa-plus-square']"
    txtEmail_xpath = "//input[@name='Email']"
    txtpassword_xpath = "//input[@id='Password']"
    txtFiestname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdBtnMale_xpath = "//input[@id='Gender_Male']"
    rdBtnFemale_xpath = "//input[@id='Gender_Female']"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCmName_xpath = "//input[@id='Company']"
    txtNewsletter_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    listYourstorename_xpath = "//li[normalize-space()='Your store name']"
    listTestStore2_xpath = "//li[normalize-space()='Test store 2']"
    txtCustomerRole_xpath = "(//div[@role='listbox'])[2]"
    listAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    listForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    listGuests_xpath = "//li[contains(text(),'Guests')]"
    listRegistered_xpath = "//li[contains(text(),'Registered')]"
    listVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpManagerofVenders_xpath = "//select[@id='VendorId']"
    txtAdminCmt_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_Customers_menu_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnk_Customers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtpassword_xpath).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFiestname_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastname_xpath).send_keys(lastname)

    def setGender(self, Gender):
        if Gender == "Male":
            self.driver.find_element(By.XPATH, self.rdBtnMale_xpath).click()
        elif Gender == "Female":
            self.driver.find_element(By.XPATH, self.rdBtnFemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdBtnMale_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txtCmName_xpath).send_keys(companyName)

    def setNewsLetter(self, newslt):
        self.driver.find_element(By.XPATH, self.txtNewsletter_xpath).click()
        time.sleep(2)
        if newslt == "Your store name":
            self.listItem1 = self.driver.find_element(By.XPATH, self.listYourstorename_xpath)
            time.sleep(3)
        elif newslt == "Test store 2":
            self.listItem1 = self.driver.find_element(By.XPATH, self.listTestStore2_xpath)
        else:
            self.listItem1 = self.driver.find_element(By.XPATH, self.listYourstorename_xpath)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", self.listItem1)

    def setCustomerRole(self, Role):
        self.driver.find_element(By.XPATH, self.txtCustomerRole_xpath).click()
        time.sleep(2)
        if Role == "Administrators":
            self.listItem = self.driver.find_element(By.XPATH, self.listAdministrators_xpath)
        elif Role == "Forum Moderators":
            self.listItem = self.driver.find_element(By.XPATH, self.listForumModerators_xpath)
        elif Role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "(//span[@title='delete'])[2]").click()
            self.listItem = self.driver.find_element(By.XPATH, self.listGuests_xpath)
        elif Role == "Registered":
            self.driver.find_element(By.XPATH, "(//span[@title='delete'])[2]").click()
            self.listItem = self.driver.find_element(By.XPATH, self.listRegistered_xpath)
        elif Role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH, self.listVendors_xpath)
        else:
            self.listItem = self.driver.find_element(By.XPATH, self.listGuests_xpath)
        time.sleep(2)
        #self.listItem.click()
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def setManagerOfVendor(self, value):
        drop = Select(self.driver.find_element(By.XPATH, self.drpManagerofVenders_xpath))
        #drop.deselect_by_visible_text(value)
        drop.select_by_index(value)

    def setAdminCmt(self, comment):
        self.driver.find_element(By.XPATH, self.txtAdminCmt_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
        time.sleep(4)




