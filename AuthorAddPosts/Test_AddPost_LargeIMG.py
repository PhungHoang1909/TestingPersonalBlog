import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Author_AddPosts(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/admin/add_posts.php')

    def tearDown(self):
        self.driver.quit()

    def test_LarIMG_Publish(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("New Day")

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("Hit a book")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        file_input = self.driver.find_element(By.NAME, "image")
        image_path = r"D:\Study\Năm 3\HKII\KiemThuPhanMem\UnitTest_PersonalBlog\largeimg.jpg"
        file_input.send_keys(image_path)

        self.driver.find_element(By.NAME, "publish").click()

        # Wait for message elements to be visible
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='message']/span")))

        # Capture all message elements
        message_elements = self.driver.find_elements(By.XPATH, "//div[@class='message']/span")

        # Assert the count of message elements
        self.assertIn(len(message_elements), [1, 2], "Expected 1 or 2 messages displayed")

        # Assert the message text
        for message_element in message_elements:
            self.assertEqual(message_element.text, "images size is too large!", "Message text is not as expected")

    def test_LarIMG_Draft(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("New Day")

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("Hit a book")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        file_input = self.driver.find_element(By.NAME, "image")
        image_path = r"D:\Study\Năm 3\HKII\KiemThuPhanMem\UnitTest_PersonalBlog\largeimg.jpg"
        file_input.send_keys(image_path)

        self.driver.find_element(By.NAME, "draft").click()

        # Wait for message elements to be visible
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//div[@class='message']/span")))

        # Capture all message elements
        message_elements = self.driver.find_elements(By.XPATH, "//div[@class='message']/span")

        # Assert the count of message elements
        self.assertIn(len(message_elements), [1, 2], "Expected 1 or 2 messages displayed")

        # Assert the message text
        for message_element in message_elements:
            self.assertEqual(message_element.text, "images size is too large!", "Message text is not as expected")

if __name__ == '__main__':
    unittest.main()
