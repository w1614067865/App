from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pymongo import MongoClient

from config import *
from utils.common import *


class Moments(object):
    def __init__(self, ):
        """
        初始化
        """
        # Appium配置
        desired_caps = {}
        desired_caps.update(DESIRED_CAPS)
        self.driver = webdriver.Remote(DRIVER_SERVER, desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        # 坐标系
        self.window_size = self.driver.get_window_size()
        self.x = self.window_size['width'] * 0.5
        self.y_1 = self.window_size['height'] * 0.6
        self.y_2 = self.window_size['height'] * 0.2
        # 配置Mongo_DB
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]

    def login(self):
        """
        登陆
        """
        # 登陆按钮
        submit = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.Button[@resource-id='com.tencent.mm:id/e4g']"))
        )
        submit.click()
        # 手机账号输入
        username = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.EditText[@resource-id='com.tencent.mm:id/kh']"))
        )
        username.set_text(PHONE_NUMBER)
        # 下一步
        next = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.Button[@resource-id='com.tencent.mm:id/axt']"))
        )
        next.click()
        # 密码输入
        passwd = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//android.widget.LinearLayout[@resource-id='com.tencent.mm:id/d_t']/android.widget.EditText[1]"))
        )
        passwd.set_text(PASSWD)
        # 登陆
        submit = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.Button[@resource-id='com.tencent.mm:id/axt']"))
        )
        submit.click()

    def enter(self):
        """
        进入朋友圈
        """
        # 发现选项卡
        discover_tab = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.LinearLayout/android.widget.RelativeLayout[3]"))
        )
        discover_tab.click()
        # 进入朋友圈
        moments = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//android.widget.ListView[@resource-id='android:id/list']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]"))
        )
        moments.click()

    def parse_items(self):
        """
        解析朋友圈
        :return: data数据
        """
        while True:
            # 当前页
            items = self.wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "//android.widget.FrameLayout[@resource-id='com.tencent.mm:id/ej9']"))
            )
            # 向上滑动
            self.driver.swipe(self.x, self.y_1, self.x, self.y_2, duration=0)
            for item in items:
                try:
                    nickname = item.find_element_by_id("com.tencent.mm:id/b5o").get_attribute('text')
                    content = item.find_element_by_id("com.tencent.mm:id/ejc").get_attribute('text')
                    datetime = item.find_element_by_id("com.tencent.mm:id/eec").get_attribute('text')
                    datetime = handle_date(datetime)
                    data = {'nickname': nickname, 'content': content, 'datetime': datetime}
                    self.stock(data)
                except:
                    pass

    def stock(self, item):
        """
        入库
        :param item: 数据
        """
        # 存在则更新数据，否则插入数据
        print(item)
        self.collection.update(item, {'$set': item}, True)

    def main(self):
        """
        主入口
        """
        try:
            self.login()
        except:
            pass
        try:
            self.enter()
        except Exception as e:
            print(e)
        self.parse_items()


if __name__ == '__main__':
    moments = Moments()
    moments.main()