import time
from selenium import webdriver


class Cookie(object):
    def __init__(self, url):
        self.browser = webdriver.Firefox()
        self.browser.get(url)
        self.browser.implicitly_wait(10)

    # 获取cookies
    def get_cookie(self):
        time.sleep(2)

        cookies = self.browser.get_cookies()
        print("cookies = " + str(cookies))

        for c in cookies:
            print("name", c["name"])
            print("value", c["value"])

    # 添加cookies
    def add_cookie(self):
        # 百度cookies
        self.browser.add_cookie({'name': 'BAIDUID', 'value': '47A4****FG=1'})
        self.browser.add_cookie({'name': 'BDUSS', 'value': 'tBdV****dbbW'})
        time.sleep(2)
        self.browser.refresh()  # 刷新


if __name__ == '__main__':
    cook = Cookie("https://www.baidu.com/")
    # cook = Cookie("https://mail.163.com/")
    print("================================登陆前cookies==============================")
    cook.get_cookie()
    print("================================登陆后cookies==============================")
    cook.add_cookie()
    cook.get_cookie()
