import unittest
import os
from appium import webdriver


class TestWebsiteiOSSafari(unittest.TestCase):
    dc = {}
    test_name = 'Test Mobile Website on iOS Safari'
    # if you have configured an access key as environment variable,
    # use the line below. Otherwise, specify the key directly.
    accessKey = os.environ['SEETEST_IO_ACCESS_KEY']
    driver = None

    def setUp(self):
        self.dc['testName'] = self.test_name
        self.dc['accessKey'] = self.accessKey
        self.dc['platformName'] = 'ios'
        self.dc['browserName'] = 'safari'
        self.driver = webdriver.Remote('https://stage.experitest.com:443/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.get('https://google.com')
        self.driver.find_element_by_xpath("//*[@name='q']").send_keys('mobile automation testing')
        self.driver.find_element_by_xpath("//*[@name='btnG']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

