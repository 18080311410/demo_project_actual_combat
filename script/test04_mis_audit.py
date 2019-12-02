"""
后台内容审核脚本
"""

import sys,os

sys.path.append(os.getcwd())
import page
from tool.get_driver import GetWebDriver
from tool.get_log import GetLog
from page.page_in import PageIn
log=GetLog.get_log()



class TestMisAudit:

    def setup_class(self):
        # 获取driver
        self.driver=GetWebDriver.get_web_driver(page.mis_url)
        # 实例化统一入口类
        self.page=PageIn(self.driver)
        self.page.page_get_misLogin().page_combination_login_success()
        self.mis=self.page.page_get_misAudit()

    def teardown_class(self):
        # 关闭driver
        GetWebDriver.quit_web_driver()

    #TODO:需要依赖登录条件
    def test_audit(self,title=page.article_title,channel=page.article_channel):
        # 审核业务方法
        self.mis.page_combination_method(title,channel)
        # 断言
        try:
            assert self.mis.page_get_audit_result(title,channel)
        except Exception as e:
            log.error(e)
            self.mis.base_get_img()
            raise


