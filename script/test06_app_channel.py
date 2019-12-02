"""
频道选择测试方法
"""
import sys, os
from time import sleep

sys.path.append(os.getcwd())

from tool.get_driver import GetWebDriver
from page.page_in import PageIn
from tool.get_log import GetLog

log = GetLog().get_log()


class TestAppChannel:

    def setup_class(self):
        driver = GetWebDriver.get_app_driver()
        self.page_in = PageIn(driver)
        self.page_in.page_get_AppLogin().page_login_success()
        self.channel = self.page_in.page_get_AppChannel()

    def teardown_class(self):
        GetWebDriver.quit_app_driver()

    def test_channel(self, channel_text="python", article_text="Python"):
        try:
            self.channel.page_combination_method(channel_text, article_text)
            sleep(3)
            self.channel.base_get_img()
        except Exception as e:
            log.error(e)
            sleep(3)
            self.channel.base_get_img()
            raise


