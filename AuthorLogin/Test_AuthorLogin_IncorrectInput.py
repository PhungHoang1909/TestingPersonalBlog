import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class Test_AuthorLogin_IncorrectInput(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/admin_login.php')

    def tearDown(self):
        self.driver.quit()

    def test_AuthorLogin_IncorrectInput(self):
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("JaneDoe")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("StrongPassword!456")

        self.driver.find_element(By.XPATH, "//input[@value='login now']").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "incorrect username or password!", "not as expected")

if __name__ == '__main__':
    unittest.main()