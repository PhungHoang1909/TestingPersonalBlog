import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select


class Author_ViewPosts(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/view_posts.php')


    def tearDown(self):
        self.driver.quit()

    def test_DeleteComment(self):
        post_form = self.driver.find_element(By.XPATH, "//form[@method='post' and input[@name='post_id'][@value='16']]")
        post_form.find_element(By.CLASS_NAME, "btn").click()
        self.driver.implicitly_wait(3)

        # Delete comments
        self.driver.find_element(By.NAME, "delete_comment").click()
        try:
            alert = self.driver.switch_to.alert

            alert.accept()
        except:
            pass

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "comment delete!", "not as expected")













