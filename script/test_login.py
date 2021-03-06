import sys,os
import pytest
sys.path.append(os.getcwd())
from base.init_driver import get_driver
from page.navigation_page import NavigationPage
from base.read_yaml_data import read_yaml_data

def get_data1():
    data_list = []
    data = read_yaml_data("login1.yaml")
    for i in data.keys():
        data2 = data.get(i)
        data_list.append((data2.get("name"),data2.get("passwd")))
    print(data_list)
    return data_list

def get_data2():
    data_list = []
    data = read_yaml_data("login2.yaml")
    for i in data.keys():
        data2 = data.get(i)
        data_list.append((data2.get("name"),
                          data2.get("passwd"),
                          data2.get("get_toast_msg"),
                          data2.get("expect_msg")))
    print(data_list)
    return data_list


class Test_Login:

    def setup_class(self):
        self.driver = get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.navi_page = NavigationPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    #测试正确的数据
    @pytest.mark.parametrize("name, pwd", get_data1())
    def test_login1(self,name,pwd):
        #点击我的
        self.navi_page.get_home_page_obj().click_my_btn()
        #点击已有账号注册
        self.navi_page.get_sign_in_obj().click_exit_account()
        #输入用户名和密码
        self.navi_page.get_login_page_obj().login_in(name,pwd)
        #点击个人中心
        self.navi_page.get_person_center_obj().click_setting_btn()
        #点击退出
        self.navi_page.get_setting_page_obj().click_logout_btn()


    @pytest.mark.parametrize("name, pwd,get_toast_msg,except_data", get_data2())
    def test_login2(self, name, pwd,get_toast_msg,except_data):
        # 点击我的
        self.navi_page.get_home_page_obj().click_my_btn()
        # 点击已有账号注册
        self.navi_page.get_sign_in_obj().click_exit_account()
        # 输入用户名和密码
        self.navi_page.get_login_page_obj().login_in(name, pwd)
        # 获取弹出的吐司 和预期结果进行对比
        login_result = self.navi_page.get_setting_page_obj().get_toast_message(get_toast_msg)
        print(login_result)
        assert except_data == login_result
        # 点击关闭按钮
        self.navi_page.get_login_page_obj().close_login()


