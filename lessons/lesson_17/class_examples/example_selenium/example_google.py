from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

page = webdriver.Chrome('chromedriver.exe')

page.get("http://google.com")

input_element = page.find_element(by=By.TAG_NAME, value='input')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)
