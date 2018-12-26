from selenium.webdriver.common.by import By
"""首页"""
# 我的按钮
my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")


"""注册页面"""
sign_in_id = (By.ID, "com.yunmall.lc:id/gotologon")


"""登录页面"""
# 用户名
login_username = (By.ID, "com.yunmall.lc:id/logon_account_textview")
# 密码
login_password = (By.ID, "com.yunmall.lc:id/logon_password_textview")
# 登录按钮
login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
# 关闭登录按钮
login_close_btn_id = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")


"""个人中心页面"""
# 全部订单
person_center_all_order = (By.ID, "com.yunmall.lc:id/order_more_txt")
# 设置按钮
person_center_setting_btn = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")


"""设置页面"""
# 退出按钮
setting_logout_btn = (By.ID, "com.yunmall.lc:id/setting_logout")
# 退出弹窗-确认退出按钮
setting_dialog_confirm_btn = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")


toast = By.XPATH,"//*[contains(@text,'不存在')]"