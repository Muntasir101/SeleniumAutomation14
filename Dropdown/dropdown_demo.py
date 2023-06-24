from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dropdown")))
dropdown_options = Select(dropdown)
#dropdown_options.select_by_value("1")
dropdown_options.select_by_visible_text("Option 2")