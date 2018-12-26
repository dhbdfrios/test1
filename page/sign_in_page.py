from base.base_aciton import BaseAciton
import page,allure

@allure.step(title="进入注册页面")
class SignInPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    @allure.step(title="点击已有账号")
    def click_exit_account(self):
        self.click_element(page.sign_in_id)

