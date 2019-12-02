"""
app登录方法测试
"""
import sys,os
sys.path.append(os.getcwd())
import pytest
from tool.get_driver import GetWebDriver
from page.page_in import PageAppLogin
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
log=GetLog.get_log()


class TestAppLogin:

    def setup_class(self):
        driver=GetWebDriver.get_app_driver()
        self.login=PageAppLogin(driver)


    def teardown_class(self):
        GetWebDriver.quit_app_driver()

    @pytest.mark.parametrize("phone,pwd",read_yaml("app_login.yaml"))
    def test_login(self,phone,pwd):
        self.login.page_combination_method(phone,pwd)
        try:
            assert self.login.page_login_is_success()
        except Exception as e:
            log.error(e)
            self.login.base_get_img()
            raise

