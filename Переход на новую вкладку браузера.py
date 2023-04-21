from selenium import webdriver
import time
from math import *
def calc(x):
    return str(log(abs(12 * sin(x))))
link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element('tag name', "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element('id', 'input_value')
    x = int(x_element.text)
    inputKey = browser.find_element('id', "answer")
    inputKey.location_once_scrolled_into_view
    inputKey.send_keys(calc(x))
    browser.find_element('tag name', "button").click()
# except BaseException as error:
   # print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()