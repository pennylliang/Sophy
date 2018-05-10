import unittest
from test_case.model.driver import browser


class MyTest(unittest.TestCase):
        def setUp(self):
            self.driver = browser()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
        unittest.main()