from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


browser= webdriver.Chrome();
browser.maximize_window();
browser.get('http://localhost:3000/requestor');


# test all the registration fields and submit button
selectFN =browser.find_element_by_name("required_doc")
selectFN.send_keys("sumedh")
time.sleep(1)
selectLN =browser.find_element_by_name("name")
selectLN.send_keys("deshpande")
time.sleep(1)
selectID =browser.find_element_by_name("student_id")
selectID.send_keys("123456")
time.sleep(1)


submits =browser.find_element_by_name("send")
submits.send_keys(Keys.RETURN)

Decrypt =browser.find_element_by_name("decypt")
Decrypt.send_keys("aSum500")
time.sleep(1)
Dbutton =browser.find_element_by_name("decr")
Dbutton.send_keys(Keys.RETURN)