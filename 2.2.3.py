from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
def sum(num_1, num_2):
        return num_1 + num_2
link = "https://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    num_1_element = browser.find_element('id', 'num1')
    num_2_element = browser.find_element('id', 'num2')
    num_1 = int(num_1_element.text)
    num_2 = int(num_2_element.text)
    select = Select(browser.find_element('id', 'dropdown'))
    select.select_by_visible_text(str(sum(num_1, num_2)))
    button = browser.find_element('css selector', '[type="submit"]')
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
    time.sleep(5)