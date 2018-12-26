from base.base_aciton import BaseAciton
import page

class SignInPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    def click_exit_account(self):
        self.click_element(page.sign_in_id)

