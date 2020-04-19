from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_class_name("btn-primary").click()    
	
    y = str(calc(browser.find_element_by_css_selector("#input_value").text))
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("#solve").click()

    print(browser.switch_to.alert.text.split(': ')[-1])	
   
finally:
    time.sleep(5)
    browser.switch_to.alert.accept()
    browser.quit()