from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

driver.get("https://omayo.blogspot.com/")

text_element = driver.find_element(By.XPATH,"//p[@id='pah']").text
print(text_element)
driver.quit()