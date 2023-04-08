import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FormPage:
    
  def __init__(self, driver):
    self.driver = driver
    try:
      self.form_title = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'h3')))
      self.form_desc = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.card-header')))
      self.upload_multifiles = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'upload_files')))
      
      
      self.validate_files = 'span#validate_files'
      self.file1_path = 'utils/test_img.jpg'
      self.file2_path = 'utils/test_file.txt'

    except:
      print("Exception on form page", sys.exc_info()[0])
      raise

  def validate_form_elements_are_present(self):
    assert self.form_title.is_displayed()
    assert self.form_desc.is_displayed()
    assert self.upload_multifiles.is_displayed()    

  def get_list_of_files(self):
    list_of_files = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span#validate_files'))).text
    return list_of_files