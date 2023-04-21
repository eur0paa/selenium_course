from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    a = (str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link1 = browser.find_element("link text", a)
    time.sleep(5)
    link1.click()
    input1 = browser.find_element("tag name", "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element("name", "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element("class name", "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element("id", "country")
    input4.send_keys("Russia")
    button = browser.find_element("class name", "btn-default")
    button.click()

finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла