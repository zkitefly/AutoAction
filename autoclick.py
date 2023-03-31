import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = '/usr/bin/chromedriver'

def scut():
    browser.get('https://www.ctfile.com/p/login?ref=https%3A%2F%2Fhome.ctfile.com%2F%23item-files%2Faction-index')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath("//*[@id='signinSrEmail']").send_keys(os.environ['SCUT_USER'])
    browser.find_element_by_xpath("//*[@id='signinSrPassword']").send_keys(os.environ['SCUT_PASSWORD'])
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("//*[@type='submit']").click()
    time.sleep(50)

if __name__ == '__main__':
    scut()
    # 脚本运行成功,退出浏览器
    browser.quit()
