from selenium import webdriver
import time
from math import *
def calc(x):
    return str(log(abs(12*sin(x))))
link = "https://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element('css selector', '#input_value.nowrap')
    x = int(x_element.text)
    inputKey = browser.find_element('css selector', '[type="text"]')
    inputKey.send_keys(calc(x))
    time.sleep(2)
    getCheckbox = browser.find_element("css selector", "[type='checkbox']")
    getCheckbox.click()
    getRadiobutton = browser.find_element("css selector", "[for='robotsRule']")
    time.sleep(2)
    getRadiobutton.click()
    button = browser.find_element('css selector', '[type="submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()