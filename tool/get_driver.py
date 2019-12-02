"""
实例化驱动对象
"""

from selenium import webdriver
import appium.webdriver
import page


class GetWebDriver:
    _driver = None
    _app_driver = None

    @classmethod
    def get_web_driver(cls, url):
        """获取web驱动对象"""
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.get(url)
        return cls._driver

    @classmethod
    def get_app_driver(cls):
        """获取app驱动对象"""
        if cls._app_driver is None:
            desired_caps = dict()
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "5.1"
            desired_caps["deviceName"] = "三星"
            desired_caps["appPackage"] = page.appPackage
            desired_caps["appActivity"] = page.appActivity
            # desired_caps["automationName"] = "Uiautomator2"
            cls._app_driver=appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls._app_driver

    @classmethod
    def quit_web_driver(cls):
        """关闭web驱动"""
        if cls._driver:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def quit_app_driver(cls):
        """关闭app驱动对象"""
        if cls._app_driver:
            cls._app_driver.quit()
            cls._app_driver = None