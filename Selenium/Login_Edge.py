from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)
driver.quit()