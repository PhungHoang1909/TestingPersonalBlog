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

        self.driver.find_element(By.LINK_TEXT, "Author").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.implicitly_wait(2)

        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("JaneDoe02")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("656565aA@")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("656565aA@")

        self.driver.find_element(By.NAME, "submit").click()
        self.driver.implicitly_wait(2)

    def test_LogOut(self):
        logout_button = self.driver.find_element(By.XPATH, "//span[text()='logout']")

        logout_button.click()

        try:
            alert = self.driver.switch_to.alert

            alert.accept()
        except:
            pass

        expected_url = "http://localhost/project/index.php"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"