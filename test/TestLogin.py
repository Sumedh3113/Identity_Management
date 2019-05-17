from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


browser= webdriver.Chrome();
browser.maximize_window();
browser.get('http://localhost:3000/login');


# test email, password field and submit button
select =browser.find_element_by_name("email")
select.send_keys("test@gmail.com")

selectPass =browser.find_element_by_name("password")
selectPass.send_keys("test")

time.sleep(2)

submits =browser.find_element_by_name("submit")
submits.send_keys(Keys.RETURN)

