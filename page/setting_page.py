from base.base_aciton import BaseAciton
import page,time,allure
@allure.step(title="进入设置页面")
class SettingPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    @allure.step(title="执退出登录操作")
    def click_logout_btn(self):
        # time.sleep(1)

        self.swipe_screen(1)
        allure.attach("退出操作", "点击退出按钮")
        self.click_element(page.setting_logout_btn)
        allure.attach("退出操作", "点击确定对话框按钮")
        self.click_element(page.setting_dialog_confirm_btn)
