# 对象库层
from selenium.webdriver.common.by import By

from Base.app.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 滑动区域的元素
        self.channel_area = (By.XPATH, "//")
        # 频道
        self.channel_option = ()
        # 第一条文章
        self.first_aritcal = ()
# 操作层
class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()


# 业务层
class IndexProxy():
    def __init__(self):
        self.index_handle = IndexHandle()