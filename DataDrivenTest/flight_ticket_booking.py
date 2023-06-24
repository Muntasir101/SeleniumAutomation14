import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


def test_flight_ticket():
    # Step 1: launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://c33b-103-150-20-2.ngrok-free.app")

    distance_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='distance']")))
    date_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='departure_date']")))
    seat_class_flied = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='service_class']")))
    baggage_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='extra_baggage']")))

    calculate_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='submit']")))

    test_data = pd.read_csv("Test_data2.csv")

    for index, row in test_data.iterrows():
        distance_data = row["DISTANCE"]
        date_data = row["DAY"]
        baggage_data = row["BAGGAGE(PER KG)"]

        distance_field.clear()
        distance_field.send_keys(distance_data)

        date_field.clear()
        date_field.send_keys(date_data)

        baggage_field.clear()
        baggage_field.send_keys(baggage_data)
        calculate_button.click()
        time.sleep(2)

        # Actual cost
        actual_cost_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".result-container > div:nth-of-type(3)")))
        actual_cost = actual_cost_field.text

        column_name = "ACTUAL COST"
        new_data = actual_cost

        test_data[column_name] = new_data

        test_data.to_csv("Test_data2.csv", index=False)

        driver.back()


test_flight_ticket()



