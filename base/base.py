from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_log import GetLog
import allure

log=GetLog().get_log()
class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("定位元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 定位一组元素
    def base_finds(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_elements(*loc))
    # 输入
    def base_input(self, loc, value):
        log.info("对元素进行输入：{}".format(value))
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 点击
    def base_click(self, loc):
        log.info("对元素进行点击：{}".format(loc))
        self.base_find(loc).click()

    # 获取 文本方法
    def base_get_text(self, loc):
        log.info("获取文本内容：{}".format(loc))
        return self.base_find(loc).text

    def base_get_img(self):
        # 截图
        self.driver.get_screenshot_as_file("./image/err.png")
        # 调用将图片写入报告
        self.__base_write_report()

    def __base_write_report(self):
        # 将截图加入测试报告
        with open("./image/err.png","rb") as f:
            allure.attach("报告截图：",f.read(),allure.attach_type.PNG)

    def base_click_check_case(self,view_text,click_text):
        # 点击复选框
        loc=By.XPATH,"//*[@placeholder='{}']".format(view_text)
        self.base_click(loc)
        sleep(2)
        loc=By.CSS_SELECTOR,"ul>li"
        els=self.base_finds(loc)
        for i in els:
            if i.text == click_text:
                i.click()
                break

    def get_find_id_element_result(self,text):
        # 判断元素是否存在
        loc=By.XPATH,"//*[contains(text(),'{}')]".format(text)
        try:
            self.base_find(loc,timeout=5)
            print("获取到的数据：",text)
            return True
        except:
            return False



