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

    def test_MissTitle_Publish(self):

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("Hit a book")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        self.driver.find_element(By.NAME, "publish").click()

        title = self.driver.find_element(By.NAME, "title")
        is_required = title.get_attribute("required")
        self.assertEqual(is_required, "true", "Please fill out this field.")

    def test_MissTitle_Draft(self):

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("Hit a book")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        self.driver.find_element(By.NAME, "draft").click()

        title = self.driver.find_element(By.NAME, "title")
        is_required = title.get_attribute("required")
        self.assertEqual(is_required, "true", "Please fill out this field.")

if __name__ == '__main__':
    unittest.main()


