"""
滑动屏幕业务方法
"""
import time

"""从右向左滑动屏幕"""
def screen_swipe(self, tag=1):
    """
    屏幕滑动方法
    :param tag: 1：向上滑动 2：向下滑动 3：向左滑动 4：向右滑动
    :return:
    """
    size = self.driver.get_window_size()
    width = size.get("width")
    height = size.get("height")
    time.sleep(3)
    if tag == 1:
        self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 2000)
    if tag == 2:
        self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 2000)
    if tag == 3:
        self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 2000)
    if tag == 4:
        self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 2000)

