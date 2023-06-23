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


def login():
    # Step 1: launch browser
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # Find Distance input field locator
    username = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    username.send_keys("Admin")
    time.sleep(2)

    password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    password.send_keys("admin123")
    time.sleep(2)

    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
    login_button.click()
    time.sleep(3)

    my_info = driver.find_element(By.CSS_SELECTOR,
                                  "#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a > span")
    my_info.click()
    time.sleep(6)

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='firstName']")
    first_name.send_keys(Keys.CONTROL + 'a')
    first_name.send_keys(Keys.BACKSPACE)
    first_name.send_keys("Test First Name")
    time.sleep(10)


login()
