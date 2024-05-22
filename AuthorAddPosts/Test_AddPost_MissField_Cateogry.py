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

    def test_MissCate_Publish(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("New Day")

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("Hit a book")

        self.driver.find_element(By.NAME, "publish").click()

        cate = self.driver.find_element(By.NAME, "category")
        is_required = cate.get_attribute("required")
        self.assertEqual(is_required, "true", "Please select an item in the list.")

    def test_MissCate_Draft(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("New Day")

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("Hit a book")

        self.driver.find_element(By.NAME, "draft").click()

        cate = self.driver.find_element(By.NAME, "category")
        is_required = cate.get_attribute("required")
        self.assertEqual(is_required, "true", "Please select an item in the list.")

if __name__ == '__main__':
    unittest.main()


