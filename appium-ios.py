import unittest
from appium import webdriver
import os


class IosAppTest(unittest.TestCase):
    test_name = "iOS App Test with Python"
    accessKey = os.environ["SEETEST_IO_ACCESS_KEY"]
    dc = {}
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['app'] = 'http://d242m5chux1g9j.cloudfront.net/eribank.ipa'
        self.dc['bundleId'] = 'com.experitest.ExperiBank'
        self.dc['platformName'] = 'ios'
        self.driver = webdriver.Remote('https://cloud.experitest.com:443/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.find_element_by_xpath("xpath=//*[@text='Username']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@text='Password']").send_keys('company')
        self.driver.find_element_by_xpath("xpath=//*[@text='loginButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='makePaymentButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Phone']").send_keys('123456')
        self.driver.find_element_by_xpath("xpath=//*[@text='Name']").send_keys('Test')
        self.driver.find_element_by_xpath("xpath=//*[@text='Amount']").send_keys('10')
        self.driver.find_element_by_xpath("xpath=//*[@text='Country']").send_keys('US')
        self.driver.find_element_by_xpath("xpath=//*[@text='sendPaymentButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Yes']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
