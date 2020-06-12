# 文章发布页面
# 对象库层
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Base.mp.base_page import BasePage, BaseHandle
from utils import DriverUtils, select_option


class PubPage(BasePage):

    def __init__(self):
        # super().__init__()
        BasePage.__init__(self)
        # 文章标题
        self.title = (By.CSS_SELECTOR, '[placeholder="文章名称"]')
        # frame元素
        self.frame = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 文章内容
        self.aritcal_content = (By.CSS_SELECTOR, "body")
        # 封面元素
        self.aritcal_cover = (By.XPATH, "//*[text()='自动']")
        # 下拉框
        self.channel = (By.CSS_SELECTOR, '[placeholder="请选择"]')
        # 下拉框选项
        self.channel_option = (By.XPATH, "//*[text()='区块链']")
        # 发表
        self.publish_btn = (By.XPATH, "//*[text()='发表']")

    def find_title(self):
        return self.find_elt(self.title)

    def find_frame(self):
        return self.find_elt(self.frame)

    def find_ar_content(self):
        return self.find_elt(self.aritcal_content)

    def find_ar_cover(self):
        return self.find_elt(self.aritcal_cover)

    def find_channel(self):
        return self.find_elt(self.channel)

    def find_ch_option(self):
        return self.find_elt(self.channel_option)

    def find_pb_btn(self):
        return self.find_elt(self.publish_btn)


# 操作层
class PubHandle(BaseHandle):
    def __init__(self):
        self.pub_page = PubPage()
        self.driver = DriverUtils.get_mp_driver()

    # 输入文章标题
    def input_title(self, title):
        self.input_text(self.pub_page.find_title(), title)

    # 输入文章内容
    def input_content(self, content):
        # 切换iframe
        self.driver.switch_to.frame(self.pub_page.find_frame())
        # 执行输入
        self.input_text(self.pub_page.find_ar_content(), content)
        # 返回默认主页
        self.driver.switch_to.default_content()

    # 选择封面
    def check_cover(self):
        self.pub_page.find_ar_cover().click()

    # 选择频道
    def check_channel(self, option):
        # # 点击频道元素对象
        # self.pub_page.find_channel().click()
        # # 点击选项的元素对象
        # self.pub_page.find_ch_option().click()
        select_option(self.driver, "请选择", option)

    # 点击发表
    def click_publish(self):
        self.pub_page.find_pb_btn().click()


# 业务层
class PubProxy:
    def __init__(self):
        self.pub_handle = PubHandle()

    # 发布文章
    def test_pub_aritcal(self, title, content, option):
        # 1.输入文章标题
        self.pub_handle.input_title(title)
        # 2.输入文章内容
        self.pub_handle.input_content(content)
        # 3.选择封面
        self.pub_handle.check_cover()
        # 4.选择频道option
        self.pub_handle.check_channel(option)
        # 5.点击发表
        self.pub_handle.click_publish()
