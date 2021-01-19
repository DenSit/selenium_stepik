from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

    
    x = int(browser.find_element_by_id("input_value").text)
    input = browser.find_element_by_id('answer')
    input.send_keys(calc(x))
    
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()