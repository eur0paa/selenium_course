from selenium import webdriver
import time
from math import *
def calc(x):
    return str(log(abs(12 * sin(x))))
link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element('css selector', "[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element('id', 'input_value')
    x = int(x_element.text)
    inputKey = browser.find_element('css selector', "[name='text']")
    inputKey.location_once_scrolled_into_view
    inputKey.send_keys(calc(x))
    button1 = browser.find_element('css selector', "[type='submit']")
    button1.click()
except BaseException as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()