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
        # Find the form for the post with post_id=11
        post_form = self.driver.find_element(By.XPATH, "//form[@method='post' and .//input[@name='post_id'][@value='11']]")

        # Click the edit button
        post_form.find_element(By.CLASS_NAME, "option-btn").click()

        # Wait for the edit page to load
        self.driver.implicitly_wait(3)

        # Upload a new image
        file_input = self.driver.find_element(By.NAME, "image")
        image_path = r"D:\Study\Năm 3\HKII\KiemThuPhanMem\UnitTest_PersonalBlog\newimg.jpg"
        file_input.send_keys(image_path)

        # Save the post
        self.driver.find_element(By.NAME, "save").click()

        # Capture all message elements
        message_elements = self.driver.find_elements(By.XPATH, "//div[@class='message']/span")
        messages = [element.text for element in message_elements]

        # Assert that both messages are present
        self.assertIn('post updated!', messages, "Post update message not found")
        self.assertIn('image updated!', messages, "Image update message not found")

if __name__ == '__main__':
    unittest.main()
