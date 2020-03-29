class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        self.usernametxtbox_id="txtUsername"
        self.passwordtxtbox_id="txtPassword"
        self.loginbtn_id="btnLogin"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.usernametxtbox_id).clear()
        self.driver.find_element_by_id(self.usernametxtbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.passwordtxtbox_id).clear()
        self.driver.find_element_by_id(self.passwordtxtbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.loginbtn_id).click()