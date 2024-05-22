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

    def test_Post_Delete(self):

        post_form = self.driver.find_element(By.XPATH, "//form[@method='post' and input[@name='post_id'][@value='12']]")

        self.driver.find_element(By.NAME, "delete").click()
        try:
            alert = self.driver.switch_to.alert

            alert.accept()
        except:
            pass

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "post deleted successfully!",
                         "not as expected")











