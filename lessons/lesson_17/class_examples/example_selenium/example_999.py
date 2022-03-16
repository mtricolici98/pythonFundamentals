from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

page = webdriver.Chrome('chromedriver.exe')

page.get("https://simpalsid.com/user/register")

elements = page.find_elements_by_class_name('login__form__field')

for element in elements:
    elem = element.find_element_by_tag_name('input')
    if elem:
        if elem.get_attribute('type') == 'email':
            elem.send_keys('test@gmail.com')
        elif elem.get_attribute('type') == 'text':
            elem.send_keys('test123123123123123')
        elif elem.get_attribute('type') == 'password':
            elem.send_keys('secrted')
        elif elem.get_attribute('type') == 'checkbox':
            elem.click()
page.find_element_by_class_name('login__form__footer__submit').click()

errors = page.find_elements_by_class_name('login__form__field__message')
if errors:
    print('Registration failed')
