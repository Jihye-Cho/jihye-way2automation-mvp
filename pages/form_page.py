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

      self.input_city = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'validationCustom03')))
      self.input_state = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'validationCustom04')))
      self.input_zip = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'validationCustom05')))
      self.input_terms = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'form.needs-validation label.form-check-label')))
      self.submit_form = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn')))
      
      self.file1_path = 'utils/test_img.jpg'
      self.file2_path = 'utils/test_file.txt'
      self.list_files = self.file1_path.split('/')[1] +' ' + self.file2_path.split('/')[1]
      self.validate_files = self.driver.find_element(By.CSS_SELECTOR,'span#validate_files')
      self.invalid_city = self.driver.find_element(By.ID, 'invalid_city')
      self.invalid_state = self.driver.find_element(By.ID, 'invalid_state')
      self.invalid_zip = self.driver.find_element(By.ID, 'invalid_zip')
      self.invalid_terms = self.driver.find_element(By.ID, 'invalid_terms')

      self.value_city = 'Suwon'
      self.value_state = 'Gyeonggi'
      self.value_zip = 16420

    except:
      print("Exception on form page", sys.exc_info()[0])
      raise

  def validate_form_elements_are_present(self):
    assert self.form_title.is_displayed()
    assert self.form_desc.is_displayed()
    assert self.upload_multifiles.is_displayed()    
    assert self.input_city.is_displayed()
    assert self.input_state.is_displayed()
    assert self.input_zip.is_displayed()    
    assert self.input_terms.is_displayed()
    assert self.submit_form.is_displayed()

  def get_list_of_files(self):
    return self.validate_files.text    
  
  def click_submit_form(self):
    self.submit_form.click()

  def validate_invalid_msgs(self):
    assert self.invalid_city.is_displayed()
    assert self.invalid_state.is_displayed()
    assert self.invalid_zip.is_displayed()

  def enter_values(self):
    self.input_city.send_keys(self.value_city)
    self.input_state.send_keys(self.value_state)
    self.input_zip.send_keys(self.value_zip)

  def validate_invalid_terms(self):
    assert self.invalid_terms.is_displayed()

  def check_terms(self):
    self.input_terms.click()
