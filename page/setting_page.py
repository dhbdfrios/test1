from base.base_aciton import BaseAciton
import page,time

class SettingPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    #点击退出按钮
    def click_logout_btn(self):
        # time.sleep(1)
        #1.把页面滑动到底部
        self.swipe_screen(1)
        self.click_element(page.setting_logout_btn)
        self.click_element(page.setting_dialog_confirm_btn)
