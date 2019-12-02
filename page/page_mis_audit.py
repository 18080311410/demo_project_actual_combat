"""
审核文章页面
"""
import page
from base.base import Base
from time import sleep



class PageMisAudit(Base):

    mis_id=None

    # 点击信息管理
    def page_click_message_manage(self):
        sleep(2)
        self.base_click(page.mis_info_message)

    # 点击内容审核
    def page_click_content_audit(self):
        sleep(2)
        self.base_click(page.mis_content_audit)

    # 输入文章标题
    def page_input_title(self,title):
        self.base_input(page.mis_title,title)

    # 输入频道
    def page_input_channel(self,channel):
        self.base_input(page.mis_channel,channel)

    # 选择状态
    def page_select_status(self,view_text="请选择状态",click_text="待审核"):
        self.base_click_check_case(view_text,click_text)

    # 点击查询
    def page_click_find(self):
        self.base_click(page.mis_find)

    # 获取id
    def page_get_id(self):
        sleep(2)
        self.mis_id=self.base_get_text(page.mis_id)

    # 点击通过
    def page_click_pass(self):
        self.base_click(page.mis_pass)

    # 确认修改
    def page_click_affirm(self):
        self.base_click(page.mis_affirm_pass)

    # 组合业务方法
    def page_combination_method(self,title,channel):
        self.page_click_message_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_select_status()
        self.page_click_find()
        self.page_get_id()
        print("获取的id：",self.mis_id)
        self.page_click_pass()
        self.page_click_affirm()
        sleep(3)

    # 获取审核结果业务方法
    def page_get_audit_result(self,title,channel):
        self.driver.refresh()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_select_status(click_text="审核通过")
        self.page_click_find()
        sleep(8)
        return self.get_find_id_element_result(self.mis_id)



