from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


browser= webdriver.Chrome();
browser.maximize_window();
browser.get('http://localhost:3000/register');


# test all the registration fields and submit button
selectFN =browser.find_element_by_name("first_name")
selectFN.send_keys("sumedh")
time.sleep(1)
selectLN =browser.find_element_by_name("last_name")
selectLN.send_keys("deshpande")
time.sleep(1)
selectID =browser.find_element_by_name("student_id")
selectID.send_keys("123456")
time.sleep(1)
selectEmail =browser.find_element_by_name("email")
selectEmail.send_keys("test@gmail.com")
time.sleep(1)
selectPass =browser.find_element_by_name("password")
selectPass.send_keys("test")



time.sleep(2)

submits =browser.find_element_by_name("register")
submits.send_keys(Keys.RETURN)

