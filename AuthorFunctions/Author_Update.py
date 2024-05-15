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

    def test_Update_Success(self):

        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101")

        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("admin102b")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("admin101")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("admin101")

        self.driver.find_element(By.NAME, "submit").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "password updated successfully!","Password update message is not as expected")

    def test_Update_Fail(self):
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101")

        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("admin101")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("admin103")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("admin104")

        self.driver.find_element(By.NAME, "submit").click()

        # Fail: Old password not correct:
        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "old password not matched!",
                         "Password update message is not as expected")

        # Fail: New Password not the same:
        # message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        # self.assertEqual(message_element.text, "confirm password not matched!",
        #                  "Password update message is not as expected")



