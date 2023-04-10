import sys
import time
import unittest

from utils.const import Const
from pages.registration_page import RegistrationPage
from tests.common_test import CommonTest

class TestRegistration(CommonTest):
  
  registration_url = Const.registration_page

  def visit_registration_page_enter_name(self):
    try:
      self.driver.get(self.registration_url)

      registrationpage = RegistrationPage(self.driver)
      registrationpage.validate_registration_fields_are_present()      
      registrationpage.enter_name()
      time.sleep(3)
      registrationpage.click_submit()
      time.sleep(3)
      errmsg = self.driver.find_element_by_css_selector(registrationpage.error_field)
      assert registrationpage.error_message in errmsg.text

      ## TODO count length of the errorred elements. len(div.registration_form label.error_p)

    except:      
      print("Exception on visit_registration_page_enter_name", sys.exc_info()[0])
      raise

  def enter_required_fields(self):
    try:
      registrationpage = RegistrationPage(self.driver)
      registrationpage.select_hobby()
      time.sleep(3)

      registrationpage.enter_phone()
      registrationpage.enter_username()
      registrationpage.enter_email() ## TODO - validate invalid email address
      registrationpage.enter_password()
      time.sleep(3)
      registrationpage.click_submit()
      time.sleep(3)
      assert self.driver.current_url in self.registration_url
      #there's no validation logic on password & confirm password values match
       
    except:      
      print("Exception on enter_required_fields", sys.exc_info()[0])
      raise 

if __name__ == '__main__':
	unittest.main()
