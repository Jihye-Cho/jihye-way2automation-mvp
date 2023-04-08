import os
import sys
import time
import unittest

from utils.const import Const
from pages.form_page import FormPage
from tests.common_test import CommonTest

class TestForm(CommonTest):
    form_url = Const.form_page

    def verify_form_page(self):
      try:
        self.driver.get(self.form_url)
        time.sleep(3)
        formpage = FormPage(self.driver)
        formpage.validate_form_elements_are_present()      
        time.sleep(3)

        abspath_testfile1 = os.path.abspath(formpage.file1_path)
        abspath_testfile2 = os.path.abspath(formpage.file2_path)
        formpage.upload_multifiles.send_keys(abspath_testfile1)
        formpage.upload_multifiles.send_keys(abspath_testfile2)
        time.sleep(3)
        filelist = formpage.get_list_of_files()
        self.assertEqual('test_img.jpg test_file.txt',filelist)
        time.sleep(3)

      except:      
        print("Exception on verify_alert_page", sys.exc_info()[0])
        raise 

if __name__ == '__main__':
	unittest.main()

