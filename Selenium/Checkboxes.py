import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# time.sleep(5)
# driver.quit()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.quit()
