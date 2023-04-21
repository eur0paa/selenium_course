from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
import time
def calc(x):
    return str(log(abs(12 * sin(x))))
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    # говорим Selenium проверять в течение 12 секунд, пока цена не станет равной 100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(("id", "price"), '100'))
    browser.find_element('id', 'book').click()
    x_element = browser.find_element('id', 'input_value')
    x = int(x_element.text)
    inputKey = browser.find_element('id', "answer")
    inputKey.location_once_scrolled_into_view
    inputKey.send_keys(calc(x))
    browser.find_element('id', "solve").click()
except BaseException as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    time.sleep(10)
    browser.quit()