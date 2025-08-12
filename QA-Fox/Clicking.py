import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

login_url1 = "https://omayo.blogspot.com/"
driver.get(login_url1)
driver.maximize_window()

click_item = driver.find_element(By.XPATH,"//input[@id='alert1']")
click_item.click()

time.sleep(2)
driver.quit()