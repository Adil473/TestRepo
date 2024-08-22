from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os

# ============================================================ #
current_dir = os.getcwd()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
prefs = {
    "download.default_directory": current_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service('/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(10)
#  =========================================================== #

# email = os.getenv('VAULT_EMAIL')
# password = os.getenv('VAULT_PASSWORD')
print(email , password)
try:
    driver.get("https://www.screener.in/login/")
    time.sleep(5)
    driver.fullscreen_window()
    email_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    email_input.send_keys(email)
    password_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.get("https://www.screener.in/company/RELIANCE/consolidated/")
    time.sleep(5)
    export_csv_button = driver.find_element(By.XPATH , '//*[@id="top"]/div[1]/form/button')
    export_csv_button.click()
    time.sleep(25)

finally:
    driver.quit()
