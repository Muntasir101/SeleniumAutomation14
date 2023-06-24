"""
1. Login
2. Go to My Info
3. Open Personal details
4. Fill up all input fields
5. Save
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login():
    # Step 1: launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # driver.implicitly_wait(10)

    # Find Distance input field locator
    username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='username']")))

    # username = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    username.send_keys("Admin")

    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='password']")))
    password.send_keys("admin123")

    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
    login_button.click()

    my_info = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                "#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a > span")))
    my_info.click()

    first_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='firstName']")))
    first_name.send_keys(Keys.CONTROL + 'a')
    first_name.send_keys(Keys.BACKSPACE)
    first_name.send_keys("Test First Name")

    # Country
    country = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div > div > div.oxd-select-text-input")))
    country.click()

    while country.text != "Bangladeshi":
        country.send_keys(Keys.ARROW_DOWN)

    country.send_keys(Keys.ENTER)

    time.sleep(10)


login()
