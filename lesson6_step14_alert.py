from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    # ищем кнопку
  

    button = browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
 
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла