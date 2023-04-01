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
        browser.get('CTFILE_CHECKUOTURL')
        browser.maximize_window()

        a = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "passcode")))
        a.send_keys(os.environ['CTFILE_CHECKUOTPASSWORD'])

        b = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
        b.click()

        time.sleep(50)

        c = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-outline-secondary")))
        c.click()

        time.sleep(100)
    except Exception as e:
        print(e)
    finally:
        browser.quit()

if __name__ == '__main__':
    scut()

