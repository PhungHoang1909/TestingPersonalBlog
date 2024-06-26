import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class Test_AuthorRegister(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/register_admin_2.php')

    def tearDown(self):
        self.driver.quit()

    def test_Register(self):
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("Johnny")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("strongpassword!123")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("strongpassword!123")

        self.driver.find_element(By.NAME, "submit").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "Password must contain at least one uppercase letter, one number, and one special character!", "not as expected")

if __name__ == '__main__':
    unittest.main()