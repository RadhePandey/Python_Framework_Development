import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium.Login import login_url
from Selenium.Login import user_name
from Selenium.Login import password

driver = webdriver.Firefox()

driver.get(login_url)
time.sleep(3)
driver.quit()


