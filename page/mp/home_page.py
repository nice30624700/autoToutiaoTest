# 自媒体主页
"""
自媒体的登录页面
"""

# 对象库层
from selenium.webdriver.common.by import By

from Base.mp.base_page import BasePage, BaseHandle


class HomePage(BasePage):

    # 1. 定义初始化方法
    def __init__(self):
        super().__init__()
        # 2.将所要需要操作的元素定义一个对应的实例属性
        # 3.实例属性存储元素By类定位方式以及对应值
        # 内容管理
        self.content_manager = (By.XPATH, "//*[text()='内容管理']")
        # 发布文章
        self.publish_atrical = (By.XPATH, "//*[contains(text(),'发布文章')]")

    # 4.定义找到所有元素实例方法
    def find_content_manager(self):
        return self.find_elt(self.content_manager)

    def find_publish_atrical(self):
        return self.find_elt(self.publish_atrical)


# 操作层
class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    # 点击内容管理
    def click_content_manager(self):
        self.home_page.find_content_manager().click()

    # 点击发布文章
    def click_publish_atrical(self):
        self.home_page.find_publish_atrical().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 进入发布文章页面
    def to_publish_page(self):
        # 1.点击北荣管理
        self.home_handle.click_content_manager()
        # 2.点击发布文章
        self.home_handle.click_publish_atrical()
