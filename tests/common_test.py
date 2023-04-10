import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class CommonTest(unittest.TestCase):

	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('--no-sandbox')
	options.add_argument('window-size=1920,1080')
	options.add_argument('disable-gpu')
	options.add_argument('--remote-debugging-port=9222')
	options.add_argument('--disable-dev-shm-usage')
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	# TODO run this test suite from CI tools, need to get chromedriver path on the image and provide options
	# driver = webdriver.Chrome('./chromedriver', options=options)
	driver = webdriver.Chrome('./chromedriver')
	driver.implicitly_wait(10)

	def driver_quit(self):
		self.driver.quit()
