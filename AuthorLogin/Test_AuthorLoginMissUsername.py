
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class Test_AuthorLoginMissUsername(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/admin_login.php')

    def tearDown(self):
        self.driver.quit()

    def test_AuthorLoginMissUsername(self):

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("StrongPassword!456")

        self.driver.find_element(By.XPATH, "//input[@value='login now']").click()

        username = self.driver.find_element(By.NAME, "name")
        is_required = username.get_attribute("required")
        self.assertEqual(is_required, "true", "Please fill out this field.")

if __name__ == '__main__':
    unittest.main()