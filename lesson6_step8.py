from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element("tag name", "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element("name", "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element("class name", "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element("id", "country")
    input4.send_keys("Russia")
    button = browser.find_element("xpath", "//button[text()='Submit']")
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()