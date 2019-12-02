"""
内容发布
"""

import sys,os
sys.path.append(os.getcwd())
import pytest,page
from tool.read_yaml import read_yaml
from tool.get_driver import GetWebDriver
from page.page_in import PageIn
from tool.get_log import GetLog
log=GetLog().get_log()


class TestMpArticlePublish:

    def setup_class(self):
        # 获取driver
        driver=GetWebDriver.get_web_driver(page.mp_url)
        # 实例化统一入口类
        self.pageIn=PageIn(driver)
        # 调用登录页面
        self.pageIn.page_get_mpLogin().page_login_success()
        # 调用发布页面
        self.ari=self.pageIn.page_get_mpArticle()

    def teardown_class(self):
        GetWebDriver.quit_web_driver()

    @pytest.mark.parametrize("title,content,result",read_yaml("mp_article.yaml"))
    def test_article_publish(self,title,content,result):
        self.ari.page_combination_publish(title,content)
        try:
            assert result in self.ari.page_new_add_result()
        except Exception as e:
            self.ari.base_get_img()
            log.error(e)
            raise







