"""
自媒体的登录页面
"""

# 对象库层
from selenium.webdriver.common.by import By

from Base.mp.base_page import BasePage, BaseHandle


class LoginPage(BasePage):

    # 1. 定义初始化方法
    def __init__(self):
        super().__init__()
        # 2.将所要需要操作的元素定义一个对应的实例属性
        # 3.实例属性存储元素By类定位方式以及对应值
        # 手机号码
        self.mobile = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        # 验证码
        self.code = (By.CSS_SELECTOR, '[placeholder="验证码"]')
        # 登录按钮
        self.login_btn = (By.CSS_SELECTOR, '[class="el-button el-button--primary"]')

    # 4.定义找到所有元素实例方法
    def find_mobile(self):
        return self.find_elt(self.mobile)

    def find_code(self):
        return self.find_elt(self.code)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 手机号码输入
    def input_mobile(self, mobile):
        self.input_text(self.login_page.find_mobile(), mobile)

        # 验证码输入

    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 登录点击
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录操作方法
    def test_login(self, mobile, code):
        self.login_handle.input_mobile(mobile)
        self.login_handle.input_code(code)
        self.login_handle.click_login_btn()
