import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.devtools.v136.fed_cm import click_dialog_button

driver = webdriver.Chrome()

login_url = "https://www.saucedemo.com/"
user_name = "standard_user"
password = "secret_sauce"

driver.get(login_url)
driver.maximize_window()

username_field = driver.find_element(By.NAME,"user-name")
username_field.send_keys(user_name)
time.sleep(1)

password_field = driver.find_element(By.ID,"password")
password_field.send_keys(password)
time.sleep(1)

login_button = driver.find_element(By.NAME,"login-button")
assert not login_button.get_attribute("dis")
login_button.click()

time.sleep(5)
driver.quit()