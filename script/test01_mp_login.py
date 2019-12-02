"""
测试脚本
"""
import sys,os
sys.path.append(os.getcwd())
import pytest,page
from tool.read_yaml import read_yaml
from tool.get_driver import GetWebDriver
from page.page_in import PageIn
from tool.get_log import GetLog
log=GetLog().get_log()
class TestMpLogin:
    """自媒体登录测试脚本"""

    def setup(self):
        # 获取driver
        driver=GetWebDriver.get_web_driver(page.mp_url)
        # 实例化统一入口类
        self.mp=PageIn(driver).page_get_mpLogin()

    def teardown(self):
        # 关闭驱动
        GetWebDriver.quit_web_driver()

    @pytest.mark.parametrize("phone,code,nickname",read_yaml("mp_login.yaml"))
    def test_login(self,phone,code,nickname):
        # 调用登录业务方法
        self.mp.page_login(phone,code)
        try:
            # 断言
            assert nickname == self.mp.page_get_nickname()
        except Exception as e:
            # 截图
            self.mp.base_get_img()
            # 日志
            log.error("错误：{}".format(e))
            # 抛异常
            raise