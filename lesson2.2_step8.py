import os
from selenium import webdriver
import time


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("John")
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Smith")
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("@")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')   
    
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()