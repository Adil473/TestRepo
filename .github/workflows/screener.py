from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os
email = "vgjmunq5q@rskfc.com"
password = "2B00A2E5"
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
service = Service('C:/Users/Adil Shaikh/Desktop/code/ChromeDriver/chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(10)
#  =========================================================== #

# email = os.getenv('VAULT_EMAIL')
# password = os.getenv('VAULT_PASSWORD')
# company_names = ['Reliance Industries Ltd' , 'HDFC Bank Ltd' , 'Nestle India Ltd' , 'Adani Enterprises Ltd']
company_names = ['RELIANCE' , 'HDFCBANK' , 'TATAMOTORS' , 'ADANIENT']
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
    for comp_name in company_names:
        # search_box = driver.find_element(By.XPATH , '//*[@id="desktop-search"]/div/input')
        # search_box.send_keys(Keys.CONTROL + "a")
        # search_box.send_keys(Keys.DELETE)
        # search_box.send_keys(f"{comp_name}")
        # time.sleep(5)
        # search_box.send_keys(Keys.ENTER)
        driver.get(f"https://www.screener.in/company/{comp_name}/consolidated/")
        time.sleep(10)
        
        # name = driver.find_element(By.XPATH , '//*[@id="top"]/div[1]/div/h1')
        # print(name.text)
        # export_csv_button = driver.find_element(By.XPATH , '//*[@id="top"]/div[1]/form/button')
        driver.save_screenshot(f'before{comp_name}.png')
        export_csv_button = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "icon-download", " " ))]'))
        )
        export_csv_button.click()
        time.sleep(15)
        driver.save_screenshot(f'after{comp_name}.png')

finally:
    driver.quit()





#  =============================== FOR CONCOURSE PIPELINE ============================== #
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# import time
# import os
# # usernames = ["dhruvgogri014@gmail.com"]
# # passwords = ["Dg9892211065@"]
# def login_and_download_file(url, email, password, file_suffix):
#     current_dir = os.getcwd()
 
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--window-size=1920,1080")
#     prefs = {
#         "download.default_directory": current_dir,
#         "download.prompt_for_download": False,
#         "download.directory_upgrade": True,
#         "safebrowsing.enabled": True
#     }
#     chrome_options.add_experimental_option("prefs", prefs)
#     service = Service('/usr/local/bin/chromedriver-linux64/chromedriver')

#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.implicitly_wait(10)
#     try:
#         driver.get(url)
#         driver.save_screenshot('before_login.png')
#         WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "account")]'))
#         ).click()
#         email_input = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.ID, 'id_username'))
#         )
#         password_input = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.ID, 'id_password'))
#         )
#         email_input.send_keys(email)
#         password_input.send_keys(password)
#         password_input.send_keys(Keys.RETURN)
#         driver.save_screenshot('after_login.png')
#         driver.get("https://www.screener.in/company/RELIANCE/consolidated/")
#         download_button = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Export to Excel"]'))
#         )
#         print("Attempting to click the download button...")
#         driver.execute_script("arguments[0].scrollIntoView(true);", download_button)
#         driver.execute_script("arguments[0].click();", download_button)
#         print("Download button clicked.")
#         driver.save_screenshot('after_click.png')
#         download_dir = current_dir
#         file_name = "profit_and_loss.xlsx"
#         print("Files in download directory before wait:", os.listdir(download_dir))
#         if wait_for_file(download_dir, file_name):
#             print("File downloaded successfully.")
#         else:
#             print("File downloaded successfully.")
#     except Exception as e:
#         driver.save_screenshot('error_screenshot.png')
#         print(f"Error: {e}")
#         raise e
#     finally:
#         driver.quit()
# def wait_for_file(download_dir, file_name, timeout=120):
#    start_time = time.time()
#    while time.time() - start_time < timeout:
#        for file in os.listdir(download_dir):
#            if file == file_name:
#                return True
#            if file.endswith(".crdownload"):
#                time.sleep(30)  
#        time.sleep(30) 
#    return False
# if __name__ == '__main__':
#     # for i, (username, password) in enumerate(zip(usernames, passwords)):
#     login_and_download_file("https://www.screener.in/", email, password, 1)
