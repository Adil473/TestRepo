from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os

# current_directory = "C:/Users/Adil Shaikh/Desktop/code/concourse_vault/pipeline"
# prefs = {"download.default_directory": current_directory,
#           "download.prompt_for_download": False,
#           "download.directory_upgrade": True,
#           }
# options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs" , prefs)
# options=ChromeOptions()
# service =Service("C:/Users/Adil Shaikh/Desktop/code/ChromeDriver/chromedriver-win64/chromedriver.exe")

# driver = webdriver.Chrome(service=service , options=options)
driver = webdriver.Chrome()
email = os.getenv('VAULT_EMAIL')
password = os.getenv('VAULT_PASSWORD')
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



    # Search for "Samsung Galaxy S10"
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Samsung Galaxy S10")
# search_box.send_keys(Keys.RETURN)



#     # Click on "Mobiles" in Categories
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Mobiles"))).click()


#     #Apply Filters
#     # Brand: Samsung
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='_167Mu3 _2hbLCH']//div[@class='_3FPh42']//div[@class='_2d0we9']//div[@title='SAMSUNG']//div[@class='_1Y4Vhm _4FO7b6']//label[@class='_2iDkf8 t0pPfW']//div[@class='_24_Dny']")))
# element.click()


#     # Sort by Price -> High to Low
# wait = WebDriverWait(driver, 10) # Wait up to 10 s
# driver.find_element(By.XPATH, "//div[normalize-space()='Price -- High to Low']").click()
    
#     # Select Flipkart Assured
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='_2hbLCH _24gLJx']//label[@class='_2iDkf8 shbqsL']//div[@class='_24_Dny _3tCU7L']")))
# element.click()



# driver.implicitly_wait(5)


#     #Read and Print Product Details
#     # Wait for search results to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']")))

#     # Read and print product details
# products = driver.find_elements(By.XPATH, "//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']")
# for product in products:
#     name = product.find_element(By.CSS_SELECTOR, "._4rR01T").text
#     price = product.find_element(By.CSS_SELECTOR, "._30jeq3").text
#     link = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#     print(f"Product Name: {name}, \nDisplay Price: {price}, \nLink: {link} \n\n\n")
#     message = f"Product Name: {name}, Display Price: {price}, Link: {link}"
    
#         # Execute JavaScript to print the message in the browser's console
#     driver.execute_script(f"console.log('{message}');")

    # Step 8: Close the Browser
# driver.quit() 




# # Example usage
# browsers = ['Chrome', 'Firefox','Edge', 'Safari' , 'ChromeW8']

# # Run tests in parallel
# Parallel(n_jobs=-1)(delayed(run_test)(browser) for browser in browsers)






# # List of desired capabilities for different browser/OS combinations
# desired_caps_list = [
#     {
#         'os': 'Windows',
#         'os_version': '10',
#         'browser': 'Chrome',
#         'browser_version': 'latest',
#         'name': 'BStack-[Python] Sample Test'
#     },
#     {
#         'os': 'Windows',
#         'os_version': '10',
#         'browser': 'Firefox',
#         'browser_version': 'latest',
#         'name': 'BStack-[Python] Sample Test'
#     },
#     # Add more combinations as needed
# ]


# # options = Options()
# # options.set_capability("os", "Windows")
# # options.set_capability("os_version", "10")
# # options.set_capability("browser", "Chrome")
# # options.set_capability("browser_version", "latest")
# # options.set_capability("name", "BStack-[Python] Sample Test")

# # driver = webdriver.Remote(
# #     command_executor='https://adilshaikh_yfq8GJ:xMtQqxgpztGYscyuXZ8E@hub.browserstack.com/wd/hub',
# #     options=options)



# # Iterate over the list and run the test for each combination
# for desired_cap in desired_caps_list:
#     driver = webdriver.Remote(
#         command_executor='https://adilshaikh_yfq8GJ:xMtQqxgpztGYscyuXZ8E@hub.browserstack.com/wd/hub',
#         desired_capabilities=desired_cap)
    
#     # Your existing Selenium code to interact with the Flipkart website goes here


# #Initializing WebDriver

# service = Service('D:\\ChromeDriver\\chromedriver-win64\\chromedriver.exe')

# # Initialize the WebDriver with the specified service
# driver = webdriver.Chrome(service=service)

# #Load Flipkart Home Page
# driver.get("https://www.flipkart.com")
# # driver.fullscreen_window()

# # Search for "Samsung Galaxy S10"
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Samsung Galaxy S10")
# search_box.send_keys(Keys.RETURN)



# # Click on "Mobiles" in Categories
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Mobiles"))).click()


# #Apply Filters
# # Brand: Samsung
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='_167Mu3 _2hbLCH']//div[@class='_3FPh42']//div[@class='_2d0we9']//div[@title='SAMSUNG']//div[@class='_1Y4Vhm _4FO7b6']//label[@class='_2iDkf8 t0pPfW']//div[@class='_24_Dny']")))
# element.click()


# # Sort by Price -> High to Low
# driver.find_element(By.XPATH, "//div[normalize-space()='Price -- High to Low']").click()
# wait = WebDriverWait(driver, 10) # Wait up to 10 s


# # Select Flipkart Assured
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@class='_2hbLCH _24gLJx']//label[@class='_2iDkf8 shbqsL']//div[@class='_24_Dny _3tCU7L']")))
# element.click()


# driver.implicitly_wait(5)


# #Read and Print Product Details
# # Wait for search results to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']")))

# # Read and print product details
# products = driver.find_elements(By.XPATH, "//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']")
# for product in products:
#     name = product.find_element(By.CSS_SELECTOR, "._4rR01T").text
#     price = product.find_element(By.CSS_SELECTOR, "._30jeq3").text
#     link = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#     print(f"Product Name: {name}, \nDisplay Price: {price}, \nLink: {link} \n\n\n")

# # Step 8: Close the Browser
# driver.quit()
