import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calculate_cost(distance, departure_day, extra_baggage):
    # Step 1: launch browser
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:5000/")

    # Find Distance input field locator
    distance_element = driver.find_element(By.CSS_SELECTOR, "[name='distance']")
    distance_element.send_keys(distance)
    time.sleep(3)

    departure_date = driver.find_element(By.CSS_SELECTOR, "[name='departure_date']")
    departure_date.send_keys(departure_day)
    time.sleep(3)

    baggage = driver.find_element(By.CSS_SELECTOR, "[name='extra_baggage']")
    baggage.send_keys(extra_baggage)
    time.sleep(3)

    calculate_cost_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    calculate_cost_button.click()
    time.sleep(3)


calculate_cost(499, 6, 2)
