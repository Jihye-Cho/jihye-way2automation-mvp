import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AlertPage:

  def __init__(self, driver):
    self.driver = driver

    try:      
      self.tab_alert = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'INPUT ALERT')))

      self.iframe = 'div#example-1-tab-2 iframe'
      self.button = 'body>button'

    except:
      print("Exception on Registration page", sys.exc_info()[0])
      raise

  def validate_alert_elements_are_present(self):
    assert self.tab_alert.is_displayed()

  def move_to_inputalert_tab(self):
    self.tab_alert.click()

  def click_button_to_show_alert(self):
    curframe = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.iframe)))
    self.driver.switch_to.frame(curframe)
    self.driver.find_element(By.CSS_SELECTOR, self.button).click()
  #   self.driver.find_element(By.TAG_NAME, 'button').click()

