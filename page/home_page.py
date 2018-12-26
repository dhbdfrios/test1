from base.base_aciton import BaseAciton
import page

class HomePage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    #点击我的
    def click_my_btn(self):
        self.click_element(page.my_btn_id)


