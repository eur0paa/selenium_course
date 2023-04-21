from selenium import webdriver
import time
import os # импортируем модуль для работы с ОС
link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    firstName = browser.find_element('css selector', "[name='firstname']")
    firstName.send_keys('Peter')
    lastName = browser.find_element('css selector', "[name='lastname']")
    lastName.send_keys('Marchukov')
    email = browser.find_element('name', "email")
    email.send_keys('quakew31@yandex.ru')
    file = browser.find_element('css selector', "[type='file']")
    #file.send_keys('C:\\Users\\Peter\\selenium_course\\y.txt')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого скрипта
    file_name = "y.txt"     # имя файла, который будем загружать на сайт
    file_path = os.path.join(current_dir, file_name)    # получаем путь к file_example.txt
    file.send_keys(file_path)   # отправляем файл
    button = browser.find_element('css selector', "[type='submit']")
    button.click()
except BaseException as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()