"""
内容发布页面
"""
import page
from base.base import Base
from time import sleep

class PagePublishArticle(Base):

    # 点击内容管理
    def page_click_content_manage(self):
        sleep(2)
        self.base_click(page.mp_content_manage)

    # 点击发布文章
    def page_click_publish_article(self):
        sleep(2)
        self.base_click(page.mp_publish_article)

    # 输入文章标题
    def page_input_article_title(self,value):
        self.base_input(page.mp_title,value)

    # 输入文章内容
    def page_input_article_content(self,value):
        el = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(el)
        self.base_input(page.mp_article_content,value)
        self.driver.switch_to.default_content()

    # 选择封面
    def page_select_cover(self):
        self.base_click(page.mp_cover)

    # 选择频道
    def page_select_channer(self,view_text="请选择",click_text="数据库"):
        sleep(2)
        self.base_click_check_case(view_text,click_text)

    # 点击发布
    def page_click_publish(self):
        sleep(2)
        self.base_click(page.mp_publish_btn)

    # 获取新增结果
    def page_new_add_result(self):
        sleep(2)
        return self.base_get_text(page.mp_publish_result)

    # 组合文章发布方法
    def page_combination_publish(self,title,content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_article_title(title)
        self.page_input_article_content(content)
        self.page_select_cover()
        self.page_select_channer()
        self.page_click_publish()

