from selenium import webdriver
import time

try:

    browser = webdriver.Chrome()
    link = "http://10.53.53.160/"
    browser.get(link)

    browser.find_element_by_id('basic_tennant').click()
    browser.find_element_by_css_selector('.ant-select-item-option:nth-child(1)').click()


    un = browser.find_element_by_id("basic_username")
    un.send_keys('111internal-user')

    pw = browser.find_element_by_id("basic_password")
    pw.send_keys('test')

    button = browser.find_element_by_class_name('ant-btn-primary')
    button.click()

    message = browser.switch_to.window
    # message_text = message.

    print(alert_text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()