from selenium.webdriver.common.by import By

from tool.read_yaml import read_yaml

"""以下为自媒体配置数据 """

# 文章标题
article_title = read_yaml("mp_article.yaml")[0][0]
# 频道
article_channel = "数据库"

"""以下为APP配置数据"""
appPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity"

"""web端元素定位方法"""
# Mpurl
mp_url = "http://ttmp.research.itcast.cn/"
# Misurl
mis_url = "http://ttmis.research.itcast.cn/#/"

# 手机号
mp_phone = By.CSS_SELECTOR, ".el-input__inner"
# 验证码
mp_verify_code = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录按钮
mp_login_btn = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"

# # 点击内容管理
# mp_article_manage=By.CSS_SELECTOR,""
# # 选择发布文章
# mp_article_publish=By.CSS_SELECTOR,".is-opened > ul:nth-child(2) > li:nth-child(1)"
# # 文章标题
# mp_title=By.CSS_SELECTOR,"div.filter-item > input:nth-child(1)"
# # 切换iframe
# mp_iframe=By.ID,"publishTinymce_ifr"
# # 文章内容
# mp_article_content=By.CSS_SELECTOR,"#tinymce"
# # 封面选择自动
# mp_cover_auto=By.CSS_SELECTOR,"label.el-radio:nth-child(4) > span:nth-child(2)"
# # 选择频道
# mp_channel=By.CSS_SELECTOR,".el-input--suffix > input:nth-child(1)"
# # 选择数据库
# mp_sql=By.CSS_SELECTOR,"li.el-select-dropdown__item:nth-child(6)"
# # 点击发布
# mp_publish_btn=By.CSS_SELECTOR,"button.filter-item:nth-child(1) > span:nth-child(1)"
# # 获取发布结果
# mp_publish_result=By.XPATH,"//*[contains(@text,'新增文章成功')]"


# 点击内容管理
mp_content_manage = By.XPATH, "//*[text()='内容管理']/.."
# 点击发布文章
mp_publish_article = By.XPATH, "//ul[@class='el-menu el-menu--inline']//*[contains(text(),'发布文章')]"
# 输入文章标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# 切换iframe
mp_iframe = By.ID, "publishTinymce_ifr"
# 输入文章内容
mp_article_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面
mp_cover = By.XPATH, "//*[contains(text(),'自动')]/.."
# 选择频道
mp_channel_select = By.CSS_SELECTOR, "[placeholder='请选择']"
mp_channel = By.XPATH, "//ul/li/*[text()='数据库']"
# 点击发布
mp_publish_btn = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取新增结果 ->文章新增成功
mp_publish_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

"""以下为后台管理系统元素定位信息"""
# 用户名
mis_username = By.CSS_SELECTOR, "[placeholder='用户名']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[placeholder='密码']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 获取昵称
mis_nickname = By.CSS_SELECTOR, ".user_info>span"
# 信息管理
mis_info_message = By.XPATH, "//*[text()='信息管理']"
# 内容审核
mis_content_audit = By.XPATH, "//*[text()='内容审核']"
# 文章标题
mis_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 频道选择
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 查询
mis_find = By.CSS_SELECTOR, ".find"
# id
mis_id = By.CSS_SELECTOR, "td>div>span"
# 通过
mis_pass = By.XPATH, "//button//*[text()='通过']"
# 确认
mis_affirm_pass = By.CSS_SELECTOR, ".el-button--primary"

"""以下为APP元素定位信息"""
# 登录手机号
app_phone = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
# 登录密码
app_pwd = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
# 登录按钮
app_login_btn = By.XPATH, "//*[@class='android.widget.Button']"
# 登录结果 -> 我的
app_me = By.XPATH, "//*[contains(@text,'我的') and @index='3']"
# 频道区域
app_channel=By.XPATH,"//*[@class='android.widget.HorizontalScrollView']"
# 文章区域
app_article=By.XPATH,"//*[@bounds='[0,520][1440,2288]']"


