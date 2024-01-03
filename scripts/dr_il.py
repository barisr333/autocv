import time
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

load_dotenv()

# Parse config JSON file into object
with open('path_config.json') as f:
    paths_list = json.load(f)

# Set up Chromedriver
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options)

try:
    wait = WebDriverWait(driver, 20)
    action = ActionChains(driver)
    driver.get('https://www.drushim.co.il/')

    # Click login
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'התחברות')]")
    )).click()

    # Enter credentials
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#email-login-field')
    )).send_keys(os.getenv("DR_EMAIL"))
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#password-login-field')
    )).send_keys(os.getenv("DR_PASSWORD"))

    # Click submit
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@id='submit-login-btn']")
    )).click()

    # Enter CV area
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(text(), 'קבצי קורות חיים')]")
    )).click()
    
    time.sleep(5)


finally:
    driver.quit()