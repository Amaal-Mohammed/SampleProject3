from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.common.by import By
from OrangeHrmLiveWebSite.Utils import Utils as Utils
import time

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.adminmenu_id = "menu_admin_viewAdminModule"
        self.adminmenu_xpath= "//b[contains(text(),'Admin')]"
        self.addbtn_id = "btnAdd"
        self.welcome_class = "panelTrigger"
        self.savemsg ="div.message.success.fadable"

    def click_admin(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, self.adminmenu_xpath)))
            eadmin=self.driver.find_element_by_xpath(self.adminmenu_xpath)
            self.driver.implicitly_wait(2)
            actionchains =ActionChains(self.driver)
            actionchains.double_click(eadmin).perform()
        except TimeoutException:
            print("Desired text was not present")

    def click_addbtn(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.ID, self.addbtn_id)))
            self.driver.find_element_by_id(self.addbtn_id).click()
        except TimeoutException:
            print("Desired text was not present")
    def verify_savemsg(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, self.savemsg)))
            msg = self.driver.find_element_by_css_selector(self.savemsg).text
            assert msg == Utils.EXPECTEDMSG
        except TimeoutException:
            print("Desired text was not present")