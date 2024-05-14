import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class Author_Register(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/register_admin_2.php')

    def tearDown(self):
        self.driver.quit()

    def test_Register_Success(self):
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("admin101")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("admin101")

        self.driver.find_element(By.NAME, "submit").click()


    def test_Register_Fail(self):
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin102")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("admin101")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("admin102")

        self.driver.find_element(By.NAME, "submit").click()

if __name__ == '__main__':
    unittest.main()