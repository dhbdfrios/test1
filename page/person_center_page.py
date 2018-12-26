from base.base_aciton import BaseAciton
import page

class PersonCenterPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    #点击个人中心 设置按钮
    def click_setting_btn(self):
        self.click_element(page.person_center_setting_btn)

    #判断是否登录成功 通过全部订单
    def is_login_sucess(self):
        try:
          self.find_element(page.person_center_all_order)
          return True
        except:
            return False
