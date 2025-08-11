import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium.Login import login_url

browser = webdriver.Firefox()

browser.get(login_url)
browser.minimize_window()
browser.fullscreen_window()

time.sleep(3)
browser.forward()
browser.refresh()

browser.fullscreen_window()
browser.refresh()
browser.quit()


