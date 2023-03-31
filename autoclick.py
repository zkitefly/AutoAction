import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless') # 添加无头模式选项
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

def scut():
    try: # 使用try语句捕获异常
        browser.get('https://www.ctfile.com/p/login?ref=https%3A%2F%2Fhome.ctfile.com%2F%23item-files%2Faction-index')
        # 将窗口最大化
        browser.maximize_window()
        # 格式是PEP8自动转的
        # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
        # 使用WebDriverWait和expected_conditions等待元素出现或者可交互
        username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "signinSrEmail")))
        username.send_keys(os.environ['SCUT_USER'])
        password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "signinSrPassword")))
        password.send_keys(os.environ['SCUT_PASSWORD'])
        # 在输入用户名和密码之后,点击登陆按钮
        login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn")))
        login_button.click()
        time.sleep(50)
    except Exception as e: # 如果发生异常，打印错误信息，并退出浏览器
        print(e)
        browser.quit()

if __name__ == '__main__':
    scut()
    # 脚本运行成功,退出浏览器
    browser.quit()
