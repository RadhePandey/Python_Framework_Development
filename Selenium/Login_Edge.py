import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
print("Radhe Testing")
time.sleep(3)
driver.quit()