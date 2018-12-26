from base.base_aciton import BaseAciton
import page,allure

@allure.step(title="进入app首次启动页面")
class HomePage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    @allure.step(title="点击我的")
    def click_my_btn(self):
        self.click_element(page.my_btn_id)


