from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.common.by import By

class AddUserPage():
    def __init__(self,driver):
        self.driver = driver
        self.emp_name_id = "systemUser_employeeName_empName"
        self.user_name_id="systemUser_userName"
        self.emppassword_id="systemUser_password"
        self.empconfirmpassword_id="systemUser_confirmPassword"
        self.save_emp_id="btnSave"

    def enter_empname(self,empname):
        self.driver.find_element_by_id(self.emp_name_id).send_keys(empname)

    def enter_username(self, username):
        self.driver.find_element_by_id(self.user_name_id).send_keys(username)

    def enter_emppassword(self, epass):
        self.driver.find_element_by_id(self.emppassword_id).send_keys(epass)

    def enter_empcpassword(self, ecpass):
        self.driver.find_element_by_id(self.empconfirmpassword_id).send_keys(ecpass)
    def click_saveuser(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.ID, self.save_emp_id)))
            self.driver.find_element_by_id(self.save_emp_id).click()
        except TimeoutException:
            print("Desired text was not present")