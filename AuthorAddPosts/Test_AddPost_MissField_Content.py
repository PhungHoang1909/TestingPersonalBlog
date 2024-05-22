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

    def test_MissContent_Publish(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("New Day")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        self.driver.find_element(By.NAME, "publish").click()

        content = self.driver.find_element(By.NAME, "content")
        is_required = content.get_attribute("required")
        self.assertEqual(is_required, "true", "Please fill out this field.")

    def test_MissContent_Draft(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("New Day")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        self.driver.find_element(By.NAME, "draft").click()

        content = self.driver.find_element(By.NAME, "content")
        is_required = content.get_attribute("required")
        self.assertEqual(is_required, "true", "Please fill out this field.")

if __name__ == '__main__':
    unittest.main()


