from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.fullscreen_window()
driver.refresh()

dropdown_static = Select(driver.find_element(By.ID,"dropdown-class-example"))
dropdown_static.select_by_index(1)

time.sleep(3)
driver.quit()