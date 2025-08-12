import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://omayo.blogspot.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='textbox1']").clear()
driver.find_element(By.XPATH,"//input[@id='textbox1']").send_keys("Radhe QA")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='textbox1']").clear()
driver.find_element(By.XPATH,"//input[@id='textbox1']").send_keys(123)
time.sleep(2)
driver.quit()