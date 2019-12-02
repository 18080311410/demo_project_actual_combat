"""
后台管理系统登录页面
"""

import page

from base.base import Base

class PageMisLogin(Base):

    def page_mis_username(self,username):
        """用户名"""
        self.base_input(page.mis_username,username)

    def page_mis_pwd(self,pwd):
        """密码"""
        self.base_input(page.mis_pwd,pwd)

    def page_mis_login_btn(self):
        """登录按钮"""
        self.driver.execute_script("document.getElementById('inp1').disabled=false")
        self.base_click(page.mis_login_btn)

    def page_mis_nickname(self):
        """获取登录信息"""
        return self.base_get_text(page.mis_nickname)

    def page_combination_login(self,username,pwd):
        """业务组合"""
        self.page_mis_username(username)
        self.page_mis_pwd(pwd)
        self.page_mis_login_btn()

    def page_combination_login_success(self,username="testid",pwd="testpwd123"):
        """业务组合"""
        self.page_mis_username(username)
        self.page_mis_pwd(pwd)
        self.page_mis_login_btn()



