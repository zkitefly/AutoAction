import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def scut():
    global browser # 添加global关键字
    browser = webdriver.Chrome('/usr/bin/chromedriver') # 使用webdriver启动Chrome浏览器
    browser.get("https://www.ctfile.com/p/login?ref=https://home.ctfile.com/#item-files/action-index")
    browser.maximize_window()
    browser.find_element_by_xpath("//input[@id='signinSrEmail']").send_keys(os.environ['SCUT_USER'])
    browser.find_element_by_xpath("//input[@id='signinSrPassword']").send_keys(os.environ['SCUT_PASSWORD'])
    browser.find_element_by_xpath("//button[@type='submit']").click() # 将xpath中的单引号改为双引号
    time.sleep(10) # 缩短等待时间

if __name__ == '__main__':
    scut()
    browser.quit()
