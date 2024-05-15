import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select

class Author_Register_AddPost(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/')

    def test_Login_Update_Success(self):
        self.driver.find_element(By.LINK_TEXT, "Author").click()
        self.driver.implicitly_wait(2)
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101c")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("admin101c")

        self.driver.find_element(By.XPATH, "//input[@value='login now']").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.LINK_TEXT, "Update Profile").click()

        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101")

        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("admin101c")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("admin101")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("admin101")

        self.driver.find_element(By.NAME, "submit").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "password updated successfully!","Password update message is not as expected")

    def test_Login_Update_FailOldPass(self):
        self.driver.find_element(By.LINK_TEXT, "Author").click()
        self.driver.implicitly_wait(2)
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101c")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("admin101c")

        self.driver.find_element(By.XPATH, "//input[@value='login now']").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.LINK_TEXT, "Update Profile").click()

        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101")

        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("admin101c")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("admin101")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("admin101")

        self.driver.find_element(By.NAME, "submit").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "old password not matched!","Password update message is not as expected")

    def test_Login_Update_FailNewPass(self):
        self.driver.find_element(By.LINK_TEXT, "Author").click()
        self.driver.implicitly_wait(2)
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101c")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("admin101c")

        self.driver.find_element(By.XPATH, "//input[@value='login now']").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.LINK_TEXT, "Update Profile").click()

        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101")

        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("admin101c")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("admin101")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("admin101")

        self.driver.find_element(By.NAME, "submit").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "confirm password not matched!","Password update message is not as expected")





