import sys,os
import pytest
sys.path.append(os.getcwd())
from base.init_driver import get_driver
from page.navigation_page import NavigationPage
from base.read_yaml_data import read_yaml_data

def get_data():
    data_list = []
    data = read_yaml_data("login.yaml")
    # print(data)
    for i in data.keys():
        # print(i)
        data2 = data.get(i)
        name = data2.get("name")
        passwd = data2.get("passwd")
        tag = data2.get("tag")
        toast_msg = data2.get("get_toast_msg")
        expect_msg = data2.get("expect_msg")
        data_list.append((name, passwd, tag, toast_msg, expect_msg))
    print(data_list)
    return data_list

class Test_Login:
    def setup_class(self):
        self.driver = get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navi_page = NavigationPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    #测试正确的数据
    @pytest.mark.parametrize("name, pwd,tag,get_toast_msg,except_data", get_data())
    def test_login(self,name,pwd,tag,get_toast_msg,except_data):
        #点击我的
        self.navi_page.get_home_page_obj().click_my_btn()
        #点击已有账号注册
        self.navi_page.get_sign_in_obj().click_exit_account()
        #输入用户名和密码
        self.navi_page.get_login_page_obj().login_in(name,pwd)
        if tag == 1: #说明登录成
            # 点击个人中心
            self.navi_page.get_person_center_obj().click_setting_btn()
            # 点击退出
            self.navi_page.get_setting_page_obj().click_logout_btn()
        else:
            #说明登录失败
            # 获取弹出的吐司 和预期结果进行对比
            login_result = self.navi_page.get_setting_page_obj().get_toast_message(get_toast_msg)
            print(login_result)
            assert except_data == login_result
            # 点击关闭按钮
            self.navi_page.get_login_page_obj().close_login()


