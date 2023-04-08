import sys
import time
import unittest

from utils.const import Const
from pages.alert_page import AlertPage
from tests.common_test import CommonTest

class TestAlert(CommonTest):
  alert_url = Const.alert_page

  def visit_alert_page(self):
    try:
      self.driver.get(self.alert_url)
      time.sleep(3)
      alertpage = AlertPage(self.driver)
      alertpage.validate_alert_elements_are_present()
      alertpage.move_to_inputalert_tab()
      time.sleep(3)
      alertpage.click_button_to_show_alert()
      time.sleep(3)
      
    except:      
      print("Exception on enter_required_fields", sys.exc_info()[0])
      raise 

if __name__ == '__main__':
	unittest.main()
