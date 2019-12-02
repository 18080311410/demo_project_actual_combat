"""
APP登录页面方法
"""

from base.base_app import BaseApp
import page

class PageAppLogin(BaseApp):

    # 输入手机号
    def page_input_phone(self,phone):
        self.base_input(page.app_phone,phone)

    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.app_pwd,pwd)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 判断登录结果
    def page_login_is_success(self):
        return self.base_is_exists_element()

    # 登录成功方法
    def page_login_success(self, phone="13012345678", pwd="246810"):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()


    # 业务组合方法
    def page_combination_method(self,phone,pwd):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()