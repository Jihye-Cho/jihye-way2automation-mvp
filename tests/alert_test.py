import sys
import time
import unittest

from utils.const import Const
from pages.alert_page import AlertPage
from tests.common_test import CommonTest

class TestAlert(CommonTest):
  alert_url = Const.alert_page

  def verify_alert_page(self):
    try:
      self.driver.get(self.alert_url)
      time.sleep(3)
      alertpage = AlertPage(self.driver)
      alertpage.validate_alert_elements_are_present()
      alertpage.move_to_inputalert_tab()
      time.sleep(3)
      alertpage.switch_to_iframe()
      alertpage.click_button_to_show_alert()
      time.sleep(3)

      alert = self.driver.switch_to_alert()
      self.assertEqual(alert.text, alertpage.alert_msg) # TODO to show assertionerror in report
      
      alert.send_keys(alertpage.alert_newtext)
      alert.accept()
      time.sleep(3)
      alertpage.verify_iframe_text()
      time.sleep(3)
      
    except:      
      print("Exception on verify_alert_page", sys.exc_info()[0])
      raise 

if __name__ == '__main__':
	unittest.main()
