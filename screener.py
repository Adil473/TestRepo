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
# service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
#  =========================================================== #

EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')
print(EMAIL , PASSWORD)
# company_names = ['Reliance Industries Ltd' , 'HDFC Bank Ltd' , 'Nestle India Ltd' , 'Adani Enterprises Ltd']
company_names = ['RELIANCE' , 'HDFCBANK' , 'TATAMOTORS' , 'ADANIENT']
postgres_user = os.getenv('PG_USER')
postgres_pass = os.getenv('PG_PASS')
print("postgres user: ", postgres_user)
print("postgres pass: ", postgres_pass)
# email = "vgjmunq5q@rskfc.com"
# password = "2B00A2E5"
try:
    driver.get("https://www.screener.in/login/")
    time.sleep(5)
    driver.fullscreen_window()
    email_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    email_input.send_keys(EMAIL)
    password_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)
    for comp_name in company_names:
        # search_box = driver.find_element(By.XPATH , '//*[@id="desktop-search"]/div/input')
        # search_box.send_keys(Keys.CONTROL + "a")
        # search_box.send_keys(Keys.DELETE)
        # search_box.send_keys(f"{comp_name}")
        # time.sleep(7)
        # search_box.send_keys(Keys.ENTER)
        driver.get(f"https://www.screener.in/company/{comp_name}/consolidated/")
        time.sleep(12)
        # export_csv_button = driver.find_element(By.XPATH , '//*[@id="top"]/div[1]/form/button')
        export_csv_button = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "icon-download", " " ))]'))
        )
        export_csv_button.click()
        time.sleep(15)

    download_dir = current_dir
    print("Files in download directory before wait:", os.listdir(download_dir))

finally:
    driver.quit()
