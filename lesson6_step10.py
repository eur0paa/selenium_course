from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    inputFirstName = browser.find_element('css selector', '[placeholder="Input your first name"]')
    inputFirstName.send_keys('Петр')
    inputLastName = browser.find_element('css selector', '[placeholder="Input your last name"]')
    inputLastName.send_keys('Marchukov')
    inputEmail = browser.find_element('css selector', '[placeholder="Input your email"]')
    inputEmail.send_keys('quakew31@yandex.ru')
    time.sleep(2)
    button = browser.find_element('css selector', '[type="submit"]')
    button.click()
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element("tag name", "h1")
    time.sleep(2)
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    time.sleep(2)
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()