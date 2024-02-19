import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

load_dotenv()

# Parse config JSON file into object
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
        # options.add_argument('--ignore-certificate-errors')
        # ## Headless mode settings - must be for Docker, as of now ## 
        # options.add_argument("--headless")
        # options.add_argument("disable-gpu")
        # options.add_argument('--allow-running-insecure-content')
        driver = webdriver.Edge(options=options)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://www.linkedin.com')

    # Get elements and type credentials
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#session_key')
    ))
    password = driver.find_element(By.CSS_SELECTOR, '#session_password')
    username.send_keys(os.getenv("LI_USERNAME"))
    password.send_keys(os.getenv("LI_PASSWORD"))
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Find and click 'Jobs'
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Jobs')
    )).click()

    # Find and click 'Application settings'
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Application settings')
    )).click()

    ### Delete existing CV of same name ###
    for cv in paths_list:
        # To find correct button for each resume card, we start by finding its name and working up the DOM
        lpath = "//h3[contains(string()," +  cv['Name'] + ")]/../following-sibling::div//button[@class='artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view']"

        # Click '...'
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, lpath)
        )).click()

        # Click 'Delete'
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='artdeco-dropdown__content-inner']/div[contains(string(), 'Delete')]")
        )).click()
        time.sleep(3)
    
    ### Upload new CV ###
    for cv in paths_list:
        # Locate the file input and upload
        file_input_elem = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@type='file']")
        ))
        file_input_elem.send_keys(cv['Path'])
        time.sleep(3)

    print("SUCCESS")

except TimeoutException as ex:
    print("Timed out before element found")

finally:
    driver.quit()