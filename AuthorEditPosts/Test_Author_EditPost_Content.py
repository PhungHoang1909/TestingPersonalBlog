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

    def test_Post_Edit(self):
        post_form = self.driver.find_element(By.XPATH, "//form[@method='post' and input[@name='post_id'][@value='11']]")

        post_form.find_element(By.CLASS_NAME, "option-btn").click()
        self.driver.implicitly_wait(3)

        content = self.driver.find_element(By.NAME, "content")
        content.clear()
        content.send_keys('New Content')

        # Save post
        self.driver.find_element(By.NAME, "save").click()

        message_elements = self.driver.find_elements(By.XPATH, "//div[@class='message']/span")
        messages = [element.text for element in message_elements]

        self.assertIn('post updated!', messages, "Post update message not found")












