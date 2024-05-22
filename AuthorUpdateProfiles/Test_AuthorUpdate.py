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

    def test_UpdateSuccess(self):
        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("StrongPassword!123")

        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("JaneDoe2")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("NewPassword123@")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("NewPassword123@")

        self.driver.find_element(By.NAME, "submit").click()

        # Capture all message elements
        message_elements = self.driver.find_elements(By.XPATH, "//div[@class='message']/span")

        # Collect texts from all message elements
        messages = [element.text for element in message_elements]

        # Check if both expected messages are present
        self.assertIn("admin name updated successfully!", messages, "Username update message is not as expected")
        self.assertIn("password updated successfully!", messages, "Password update message is not as expected")


if __name__ == '__main__':
    unittest.main()