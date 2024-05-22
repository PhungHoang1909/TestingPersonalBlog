import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class Author_Update(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/update_profile.php')


    def tearDown(self):
        self.driver.quit()

    def test_InvalidNewPass_case1(self):

        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("StrongPassword!123")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("NewPassword123")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("NewPassword123")



        self.driver.find_element(By.NAME, "submit").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "Password must contain at least one uppercase letter, one number, and one special character!",
                         "Password update message is not as expected")

    def test_InvalidNewPass_case2(self):

        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("StrongPassword!123")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("123")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("123")

        self.driver.find_element(By.NAME, "submit").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "New password must at least have 8 characters",
                         "Password update message is not as expected")

if __name__ == '__main__':
    unittest.main()