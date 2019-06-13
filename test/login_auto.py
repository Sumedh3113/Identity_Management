from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest 

class AssertLogin(unittest.TestCase):
	
	global browser
	browser= webdriver.Chrome();
	browser.maximize_window();
	browser.get('http://localhost:3000/register');
	
		

	def Register(self):
		# test all the registration fields and submit button
		self.selectFN =browser.find_element_by_name("first_name")
		self.selectFN.send_keys("sumedh")
		time.sleep(1)
		self.selectLN =browser.find_element_by_name("last_name")
		self.selectLN.send_keys("deshpande")
		time.sleep(1)
		self.selectID =browser.find_element_by_name("student_id")
		self.selectID.send_keys("123456")
		time.sleep(1)
		self.selectEmail =browser.find_element_by_name("email")
		self.selectEmail.send_keys("abcd@gmail.com")
		time.sleep(1)
		self.selectPass =browser.find_element_by_name("password")
		self.selectPass.send_keys("abcd@1234")
		time.sleep(1)

	def RegisterBtn(self):
		self.submits =browser.find_element_by_name("register")
		self.submits.click()

	def Login(self):
		browser.get('http://localhost:3000/login');
		self.selectEmail =browser.find_element_by_name("email")
		self.selectEmail.send_keys("ab@gmail.com")
		#self.asserEqual(self.selectEmail)
		time.sleep(1)
		self.selectPass =browser.find_element_by_name("password")
		self.selectPass.send_keys("abcd@1234")
		time.sleep(1)

	def LoginBtn(self):
		self.submits =browser.find_element_by_name("submit")
		self.submits.click()		

	def exitcode(self):
	 	browser.quit()

if __name__ == '__main__':
	import sys;sys.argv = ["",'AssertLogin.Register', 'AssertLogin.RegisterBtn','AssertLogin.Login','AssertLogin.LoginBtn' ,'AssertLogin.exitcode']
	unittest.main()
