import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Author_AddPosts(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/comments.php')


    def tearDown(self):
        self.driver.quit()

    def test_comments(self):
        # View Post
        #self.driver.find_element(By.LINK_TEXT, "view post").click()
        # # View post - Edit
        # edit_button = self.driver.find_element(By.XPATH,"//a[@class='inline-option-btn' and contains(@href, 'edit_post.php?id=17')]")
        # edit_button.click()
        # # View post - Delete
        # delete_button = self.driver.find_element(By.CLASS_NAME, "inline-delete-btn")
        # delete_button.click()
        # try:
        #     alert = self.driver.switch_to.alert
        #
        #     alert.accept()
        # except:
        #     pass
        # View post - Go back
        # go_back_button = self.driver.find_element(By.XPATH,"//a[@class='inline-option-btn' and @href='view_posts.php']")
        # go_back_button.click()

        # Delete Comment
        self.driver.find_element(By.NAME,"delete_comment").click()
        try:
            alert = self.driver.switch_to.alert

            alert.accept()
        except:
            pass

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "comment delete!", "change is not as expected")

