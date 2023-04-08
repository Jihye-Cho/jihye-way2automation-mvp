import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class RegistrationPage:

  def __init__(self, driver):
    self.driver = driver

    try:
      self.form = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'register_form')))
      self.input_firstname = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, 'name')))
      self.input_hobby = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, 'hobby')))
      self.value_hobby = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//label[contains(text(), "Reading")]')))      
      self.input_phone = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, 'phone')))
      self.input_username = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, 'username')))
      self.input_email = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, 'email')))
      self.input_password = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, 'password')))
      self.input_cpassword = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, 'c_password')))

      self.input_submit = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="submit"]:first-of-type')))

      self.error_field = 'label.error_p:first-of-type'
      
      self.input_error = 'input.error_p:first-of-type'

      
      self.value_firstname = 'test_firstname'
      self.value_lastname = 'test_lastname'
      self.value_phone = '0123456789'
      self.value_username = 'testuser'
      self.value_invalid_email = 'test'
      self.value_valid_email = 'test@test.com'
      self.value_password = 'password'
      
      self.error_message = 'This field is required.'
      
    except:
      print("Exception on Registration page", sys.exc_info()[0])
      raise
	
  def validate_registration_fields_are_present(self):    
    assert self.form.is_displayed()
    assert self.input_firstname.is_displayed()
    assert self.input_hobby.is_displayed()
    assert self.input_phone.is_displayed()
    assert self.input_username.is_displayed()
    assert self.input_email.is_displayed()
    assert self.input_password.is_displayed()
    assert self.input_cpassword.is_displayed()

  def enter_name(self):
    self.input_firstname.send_keys(self.value_firstname + Keys.TAB + self.value_lastname)    

  def select_hobby(self):
    self.value_hobby.click()

  def enter_phone(self):
    self.input_phone.send_keys(self.value_phone)

  def enter_username(self):
    self.input_username.send_keys(self.value_username)

  def enter_email(self):
    self.input_email.send_keys(self.value_valid_email)

  def enter_password(self):
    self.input_password.send_keys(self.value_password)
    self.input_cpassword.send_keys(self.value_password)

  def click_submit(self):
    self.input_submit.click()
