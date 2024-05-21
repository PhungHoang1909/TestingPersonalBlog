import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class Author_Logout(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/dashboard.php')

    def tearDown(self):
        self.driver.quit()

    def testLogout(self):

        logout_button = self.driver.find_element(By.LINK_TEXT, "logout")

        logout_button.click()

        try:
            alert = self.driver.switch_to.alert

            alert.accept()
        except:
            pass

        expected_url = "http://localhost/project/index.php"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

if __name__ == '__main__':
    unittest.main()