import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 用Service类来设置chromedrive路径
chromedriver_path = "/usr/bin/chromedriver"
service = webdriver.chrome.service.Service(chromedriver_path)
webdriver.chrome.service = service

browser = webdriver.Chrome(options=chrome_options)

def scut():

    try:
        browser.get('https://www.ctfile.com/p/login?ref=https%3A%2F%2Fhome.ctfile.com%2F%23item-files%2Faction-index')
        browser.maximize_window()

        username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "signinSrEmail")))
        username.send_keys(os.environ['SCUT_USER'])

        password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "signinSrPassword")))
        password.send_keys(os.environ['SCUT_PASSWORD'])

        login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn")))
        login_button.click()

        time.sleep(50)
    except Exception as e:
        print(e)
    finally:
        browser.quit()

if __name__ == '__main__':
    scut()
