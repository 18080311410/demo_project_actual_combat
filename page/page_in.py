from page.page_app_login import PageAppLogin
from page.page_mp_login import PageMpLogin
from page.page_mp_article import PagePublishArticle
from page.page_mis_login import PageMisLogin
from page.page_mis_audit import PageMisAudit
from page.page_app_channel import PageAppChannel

class PageIn:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_mpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle
    def page_get_mpArticle(self):
        return PagePublishArticle(self.driver)

    # 获取PageMidLogin
    def page_get_misLogin(self):
        return PageMisLogin(self.driver)

    # 获取PageMisAudit
    def page_get_misAudit(self):
        return PageMisAudit(self.driver)


    # 获取PageAppLogin
    def page_get_AppLogin(self):
        return PageAppLogin(self.driver)

    # 获取PageAppChannel
    def page_get_AppChannel(self):
        return PageAppChannel(self.driver)