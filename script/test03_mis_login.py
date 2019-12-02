"""
后台管理系统登录脚本
"""

import sys,os
sys.path.append(os.getcwd())
import page,pytest
from tool.get_driver import GetWebDriver
from page.page_in import PageIn
from tool.read_yaml import read_yaml
from tool.get_log import GetLog
log=GetLog.get_log()


class TestMisLogin:

    def setup(self):
        # 获取driver
        driver=GetWebDriver.get_web_driver(page.mis_url)
        # 获取mis页面
        self.mis=PageIn(driver).page_get_misLogin()


    def teardown(self):
        # 退出驱动
        GetWebDriver.quit_web_driver()

    @pytest.mark.parametrize("username,pwd,nickname",read_yaml("mis_login.yaml"))
    def test_login(self,username,pwd,nickname):
        # 登陆业务方法
        self.mis.page_combination_login(username,pwd)
        # 断言
        try:
            assert nickname in self.mis.page_mis_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis.base_get_img()
            raise



