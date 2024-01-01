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

    # To find correct button for each resume card, we start by finding its name and working up the DOM
    lpath = "//h3[contains(string(), 'SWE')]/../following-sibling::div//button[@class='artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view']"

    # Click '...'
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, lpath)
    )).click()

    # Click 'Delete'
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='artdeco-dropdown__content-inner']/div[contains(string(), 'Delete')]")
    )).click()
    time.sleep(3)

    # Upload new CV
    file_input_elem = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='file']")
    ))
    file_input_elem.send_keys(os.getenv("SWE_CV_PATH"))
    time.sleep(5) # TBD - Find a better way to do this!

    lpath = "//h3[contains(string(), 'Gen')]/../following-sibling::div//button[@class='artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view']"
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, lpath)
    )).click()
finally:
    driver.quit()