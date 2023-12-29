import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

load_dotenv()
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options)
try:
    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    driver.get('https://www.linkedin.com')

    # Get elements and type credentials
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#session_key')
    ))
    password = driver.find_element(By.CSS_SELECTOR, '#session_password')
    username.send_keys(os.getenv("LI_Username"))
    password.send_keys(os.getenv("LI_Password"))
    time.sleep(10)
finally:
    driver.quit()