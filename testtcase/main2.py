import unittest
from selenium import webdriver
import page


import unittest
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):

    def __init__(self, driver = None):
        if driver is not None:
            self.driver = driver
        else:
            self.setUp()

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chrome-win64")
        self.driver.get("http://www.python.org")

    def test_example(self):
        print("test")
        assert True

    def not_a_test(self):
        print('this wont print')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
