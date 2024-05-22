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
        self.driver.get('http://localhost/project/admin/add_posts.php')


    def tearDown(self):
        self.driver.quit()

    def test_Add_Success(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("New Day")

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("Hit a book")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        self.driver.find_element(By.NAME, "publish").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "post published!", "Post publishing message is not as expected")

    def test_Draft_Success(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("New Day")

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("Hit a book")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        self.driver.find_element(By.NAME, "draft").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "draft saved!", "Draft saving message is not as expected")


