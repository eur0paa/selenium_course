from selenium import webdriver
import time
from math import *
def calc(x):
    return str(log(abs(12*sin(x))))
link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element('id', 'treasure')
    x_element_get_attribute = x_element.get_attribute("valuex")
    x = int(x_element_get_attribute)
    inputKey = browser.find_element('css selector', '[type="text"]')
    inputKey.send_keys(calc(x))
    getCheckbox = browser.find_element("css selector", "[type='checkbox']")
    getCheckbox.click()
    getRadiobutton = browser.find_element("id", "robotsRule")
    getRadiobutton.click()
    time.sleep(2)
    button = browser.find_element('css selector', '[type="submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()