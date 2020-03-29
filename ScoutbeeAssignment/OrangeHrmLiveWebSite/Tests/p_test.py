from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from OrangeHrmLiveWebSite.Pages.loginPage import LoginPage
from OrangeHrmLiveWebSite.Pages.homePage import HomePage
from OrangeHrmLiveWebSite.Helpers.helpers import helpers
from OrangeHrmLiveWebSite.Pages.adduserPage import AddUserPage
from OrangeHrmLiveWebSite.Utils import Utils as Utils

class TestLogin():
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get(Utils.URL)
        yield
        time.sleep(10)
        driver.close()

    def test_login(self,test_setup):
        login=LoginPage(driver)
        login.enter_username(Utils.USERNAME)
        login.enter_password(Utils.PASSWORD)
        login.click_login()
        actualtitle = driver.title
        assert actualtitle == Utils.EXPECTEDPAGETITLE

    def test_createuser(self,test_setup):
        homepage=HomePage(driver)
        homepage.click_admin()
        homepage.click_addbtn()
        adduser= AddUserPage(driver)
        adduser.enter_empname(Utils.EMPNAME)
        adduser.enter_username(helpers.generate_username('self'))
        adduser.enter_emppassword(Utils.EMPPASSWORD)
        adduser.enter_empcpassword(Utils.EMPPASSWORD)
        adduser.click_saveuser()
        homepage.verify_savemsg()





