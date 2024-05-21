import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class Author_Login(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/admin_login.php')

    def tearDown(self):
        self.driver.quit()

    def test_AuthorLogin(self):
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("JaneDoe")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("StrongPassword!123")

        self.driver.find_element(By.XPATH, "//input[@value='login now']").click()

        expected_url = "http://localhost/project/admin/dashboard.php"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

if __name__ == '__main__':
    unittest.main()