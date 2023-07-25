import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import BaseWebElement
from selenium.webdriver.common.by import By



ng = webdriver.Chrome()

ng.get("https://www.newgrounds.com")

movieHead = ng.find_element(By.CLASS_NAME, 'header-nav-button-movies')

#print(movieHead)

movieHead.click()

time.sleep(5)

ng.quit()