from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.base import Base
import page


class BaseApp(Base):

    def base_is_exists_element(self):
        loc = page.app_me
        try:
            self.base_find(loc, timeout=5)
            return True
        except:
            return False

    def base_swipe_screen_right_left(self, loc, channel_text):
        """屏幕区域从右到左滑动"""
        scope_ele = self.base_find(loc, timeout=5)
        x = scope_ele.location.get("x")
        y = scope_ele.location.get("y")
        width = scope_ele.size.get("width")
        height = scope_ele.size.get("height")
        start_x = x + width * 0.8
        start_y = y + height * 0.5
        end_x = x + width * 0.2
        end_y = y + height * 0.5
        page_source = self.driver.page_source
        ele = By.XPATH, "//*[contains(@text,'{}')]".format(channel_text)
        while True:
            try:
                self.base_find(ele, timeout=2).click()
                break
            except:
                self.driver.swipe(start_x, start_y, end_x, end_y, 3000)
            if page_source == self.driver.page_source:
                raise NoSuchElementException
            else:
                page_source = self.driver.page_source

    def base_swipe_screen_down_up(self, loc, article_text):
        """屏幕区域从下到上滑动"""
        scope_ele = self.base_find(loc, timeout=5)
        width = scope_ele.size.get("width")
        height = scope_ele.size.get("height")
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2
        page_source = self.driver.page_source
        ele = By.XPATH, "//*[contains(@text,'{}')]".format(article_text)
        while True:
            try:
                self.base_find(ele, timeout=2).click()
                break
            except:
                self.driver.swipe(start_x, start_y, end_x, end_y, 3000)
            if page_source == self.driver.page_source:
                raise NoSuchElementException
            else:
                page_source = self.driver.page_source
