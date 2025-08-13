import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(3)

# Correct way: pass locator tuple
WebDriverWait(driver, 6).until(
    EC.element_to_be_clickable((By.XPATH, "//tbody/tr/td[3]/ul[1]/li[2]/a[1]"))
)

time.sleep(2)
driver.find_element(By.XPATH, "//tbody/tr/td[3]/ul[1]/li[2]/a[1]").click()
time.sleep(3)
driver.quit()
