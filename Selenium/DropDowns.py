from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
print("Launch")

# Static Dropdown example (optional, not needed for this task)
driver.find_element(By.ID, "dropdown-class-example").click()
time.sleep(1)
print("Static Dropdown")

# Type 'ind' into the dynamic dropdown
driver.find_element(By.ID, "autocomplete").send_keys("ind")
time.sleep(3)

# Fetch all options in the dropdown
dropdown_options = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li/div")

for option in dropdown_options:
    if option.text.strip() == "India":
        option.click()
        break

time.sleep(5)
driver.quit()
