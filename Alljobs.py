import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options)
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.alljobs.co.il')
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'כניסה')
    )).click() # Login link

    # Switch to signin iframe
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[id='signin_iframe']")))
    
    # Get elements and type credentials
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#inputEmail')
    ))
    password = driver.find_element(By.CSS_SELECTOR, '#inputPassword')
    username.send_keys(os.getenv("AJ_Email"))
    password.send_keys(os.getenv("AJ_Password"))
finally:
    driver.quit()