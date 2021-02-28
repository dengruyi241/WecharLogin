import json
from time import sleep

from selenium import webdriver

from base import Base


class TestWechar(Base):
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.vars = {}

    # 复用已有浏览器登录
    def test_login_tmp(self):
        self.driver.get("https://work.weixin.qq.com")
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()

    def test_login_cookie(self):
        # 存入cookies
        # cookies = self.driver.get_cookies()
        # with open("cookie2.txt", "w", encoding="utf-8") as f:
        #     # 采用写文件的方法
        #     f.write(json.dumps(cookies))
        #     #采用dump的方法写入
        #     # json.dump(cookies,f)
        self.driver.get("https://work.weixin.qq.com")
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        with open("cookie.txt", "r", encoding="utf-8") as f:
            # #采用读取文件的方法
            # raw_cookies = f.read()
            # cookies = json.loads(raw_cookies)
            # 采用反序列化的方法
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        # 刷新浏览器
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="menu_manageTools"]/span').click()
        sleep(5)
