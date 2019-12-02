"""
首页频道选择
"""
from time import sleep

import page
from base.base_app import BaseApp



class PageAppChannel(BaseApp):

    # 获取频道信息
    def page_search_channel(self,channel_text):
        self.base_swipe_screen_right_left(page.app_channel,channel_text)

    # 获取文章
    def page_search_article(self,article_text):
        self.base_swipe_screen_down_up(page.app_article,article_text)

    # 业务组合
    def page_combination_method(self,channel_text,article_text):
        sleep(3)
        self.page_search_channel(channel_text)
        sleep(3)
        self.page_search_article(article_text)



