from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open login page
driver.get("https://www.saucedemo.com/")

# Enter username and password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click login
driver.find_element(By.ID, "login-button").click()

# Optional: wait for inventory page to load
time.sleep(3)  # or you can use WebDriverWait

# Close browser
driver.quit()
