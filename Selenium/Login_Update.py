import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium.Login import login_url
from Selenium.Login import user_name
from Selenium.Login import password

browser = webdriver.Firefox()

browser.get(login_url)
browser.fullscreen_window()
time.sleep(3)
browser.quit()


