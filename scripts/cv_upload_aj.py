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
    wait = WebDriverWait(driver, 30)
    action = ActionChains(driver)
    driver.get('https://www.alljobs.co.il')

     # Login link
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'כניסה')
    )).click()

    # Switch to signin iframe
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[id='signin_iframe']")))
    
    # Get elements and type credentials
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#inputEmail')
    ))
    password = driver.find_element(By.CSS_SELECTOR, '#inputPassword')
    username.send_keys(os.getenv("AJ_EMAIL"))
    password.send_keys(os.getenv("AJ_PASSWORD"))

    # Click submit
    driver.find_element(By.ID, 'btn-submit-form').click()
    # driver.get('https://www.alljobs.co.il/User/UserCVsPanel/CVManagement.aspx')

    # Get rid of popup
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@class='za_reset zoom_btn_c']")
    )).click()
    # Find and hover over user menu
    menu = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@id='nav-item-user-area']")
    ))
    action.move_to_element(menu).perform()
    time.sleep(10)

    # Enter CV area

finally:
    driver.quit()