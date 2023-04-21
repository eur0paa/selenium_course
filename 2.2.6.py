from selenium import webdriver
from math import *
import time
def calc(x):
        return str(log(abs(12 * sin(x))))
link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element('id', 'input_value')
    x = int(x_element.text)
    inputKey = browser.find_element('css selector', "[class='form-control']")
    inputKey.location_once_scrolled_into_view
    inputKey.send_keys(calc(x))
    getCheckbox = browser.find_element("id", "robotCheckbox")
    getCheckbox.click()
    getRadiobutton = browser.find_element("id", "robotsRule")
    getRadiobutton.click()
    button = browser.find_element('tag name', 'button')
    button.click()
except BaseException as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()