from base.base_aciton import BaseAciton
import page

class LoginPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    def login_in(self,username,pwd):
        self.send_element_content(page.login_username,username)
        self.send_element_content(page.login_password,pwd)
        self.click_element(page.login_btn_id)

    def close_login(self):
        self.click_element(page.login_close_btn_id)

