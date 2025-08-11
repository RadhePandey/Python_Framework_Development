from selenium import webdriver
#from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
viewport = [(100,299), (400,500), (540,800)]

driver.get("https://www.google.com/")

try:
    for width,height in viewport :
        driver.set_window_size(width,height)
        time.sleep(3)
finally:
    driver.close()