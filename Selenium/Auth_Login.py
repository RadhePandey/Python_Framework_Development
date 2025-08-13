import time

from selenium import webdriver
import time

driver = webdriver.Firefox()
username = "admin"
password = "admin"
driver.get("")

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

#https://username:password@admin
time.sleep(20)
driver.quit()