from base.base_aciton import BaseAciton
import page,allure
@allure.step(title="进入登录页面")
class LoginPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    @allure.step(title="输入用户名密码")
    def login_in(self,username,pwd):

        allure.attach("用户名","{}".format(username))
        self.send_element_content(page.login_username,username)
        allure.attach("密码", "{}".format(pwd))
        self.send_element_content(page.login_password,pwd)
        allure.attach("点击登录", "{}")
        self.click_element(page.login_btn_id)

    @allure.step(title="关闭登录页面")
    def close_login(self):
        self.click_element(page.login_close_btn_id)

