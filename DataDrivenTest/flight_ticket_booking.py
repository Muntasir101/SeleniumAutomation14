import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


def test_flight_ticket():
    # Step 1: launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://127.0.0.1:5000/")

    distance_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='distance']")))
    date_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='departure_date']")))
    seat_class_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='service_class']")))
    baggage_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='extra_baggage']")))

    calculate_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='submit']")))

    test_data = pd.read_csv("Test_data2.csv")

    for index, row in test_data.iterrows():
        distance_data = row["DISTANCE"]
        date_data = row["DAY"]
        baggage_data = row["BAGGAGE(PER KG)"]
        seat_class = row["CLASS"]

        distance_field.clear()
        distance_field.send_keys(distance_data)

        date_field.clear()
        date_field.send_keys(date_data)

        dropdown_options = Select(seat_class_field)
        if seat_class == "E":
            dropdown_options.select_by_visible_text("Economy")
        elif seat_class == "B":
            dropdown_options.select_by_visible_text("Business")
        elif seat_class == "F":
            dropdown_options.select_by_visible_text("First")

        baggage_field.clear()
        baggage_field.send_keys(baggage_data)
        calculate_button.click()
        time.sleep(2)

        # Actual cost
        actual_cost_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".result-container > div:nth-of-type(3)")))
        actual_cost = actual_cost_field.text

        result_data = actual_cost
        test_data["ACTUAL COST"] = result_data
        test_data.to_csv("Test_data2.csv")
        time.sleep(2)

        driver.back()


test_flight_ticket()
