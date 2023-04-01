import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 用Service类来设置chromedrive路径
chromedriver_path = "/usr/bin/chromedriver"
service = Service(chromedriver_path)

browser = Chrome(options=chrome_options, service=service)


def scut():
    try:
        browser.get('CTFILE_CHECKUOTURL')
        browser.maximize_window()
        password_input = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "passcode")))
        password_input.send_keys(os.environ['CTFILE_CHECKUOTPASSWORD'])
        submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary")))
        submit_button.click()
        time.sleep(50)
        secondary_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-outline-secondary")))
        secondary_button.click()
        time.sleep(100)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        browser.quit()

if __name__ == '__main__':
    scut()