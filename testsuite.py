import unittest

from HtmlTestRunner import HTMLTestRunner
from tests.common_test import CommonTest
from tests.registration_test import TestRegistration
from tests.alert_test import TestAlert

def suite():
    suite =  unittest.TestSuite()
    suite.addTest(TestRegistration('visit_registration_page_enter_name')) 
    suite.addTest(TestRegistration('enter_required_fields')) 
    suite.addTest(TestAlert('visit_alert_page'))
    suite.addTest(CommonTest('driver_quit'))
    return suite

if __name__ == '__main__':
	runner = HTMLTestRunner(output='./reports', combine_reports=True, report_title="UI_Automation_TestResults", report_name="UI_Automation_TestResults")
	runner.run(suite())

