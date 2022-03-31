from selenium import webdriver
import os
import time




try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    # ищем поля для ввода

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ivanpet@mail")
    
    file_input = browser.find_element_by_name("file")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'File.txt')           # добавляем к этому пути имя файла 
    file_input.send_keys(file_path)
    
     

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла