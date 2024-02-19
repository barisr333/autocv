import time
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

load_dotenv()

# Parse config JSON file into objects
with open('path_config.json') as f:
    paths_list = json.load(f)

match os.getenv("browser"):
    case 'Chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        ## Headless mode settings - must be for Docker, as of now ## 
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options)
    case 'Edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        ## Headless mode settings - must be for Docker, as of now ## 
        # options.add_argument("--headless")
        # options.add_argument("disable-gpu")
        # options.add_argument('--allow-running-insecure-content')
        driver = webdriver.Edge(options=options)


try:
    wait = WebDriverWait(driver, 20)
    # driver.get_screenshot_as_file("screenshot.png")
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

    ### Update CVs - Drushim has nice update functionality so no need to delete ###
    for cv in paths_list:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='layout cv-short-view wrap pointer' and contains(string()," + "'"+cv['Name'] +"')]//input")
        )).send_keys(cv['Path'])
        time.sleep(3)
    
    print("SUCCESS")

except TimeoutException as ex:
    print("Timed out before element found")

finally:
    driver.quit()