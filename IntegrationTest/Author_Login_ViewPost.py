import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select

class Author_Register_AddPost(unittest.TestCase):
    def setUp(self):
        self.debugger_address = 'localhost:8989'
        self.c_options = Options()
        self.c_options.add_experimental_option("debuggerAddress", "localhost:8989")
        self.driver = webdriver.Edge(options=self.c_options)
        self.driver.get('http://localhost/project/')

        self.driver.find_element(By.LINK_TEXT, "Author").click()
        self.driver.implicitly_wait(2)
        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin101")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("admin101")

        self.driver.find_element(By.XPATH, "//input[@value='login now']").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.LINK_TEXT, "Check Posts").click()

    def test_Post_Delete(self):

        post_form = self.driver.find_element(By.XPATH, "//form[@method='post' and input[@name='post_id'][@value='19']]")

        self.driver.find_element(By.NAME, "delete").click()
        try:
            alert = self.driver.switch_to.alert

            alert.accept()
        except:
            pass

    def test_Post_Edit(self):
        post_form = self.driver.find_element(By.XPATH, "//form[@method='post' and input[@name='post_id'][@value='18']]")

        post_form.find_element(By.CLASS_NAME, "option-btn").click()
        self.driver.implicitly_wait(3)

        title = self.driver.find_element(By.NAME, "title")
        title.clear()
        title.send_keys("My Post Title change")

        content = self.driver.find_element(By.NAME, "content")
        content.clear()
        content.send_keys("This is my post content")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        file_input = self.driver.find_element(By.NAME, "image")
        image_path = r"D:\Study\Năm 3\HKII\KiemThuPhanMem\UnitTest_PersonalBlog\AuthorFunctions\img0.jpg"
        file_input.send_keys(image_path)

        # # Save post
        self.driver.find_element(By.NAME, "save").click()
        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "post updated!", "change is not as expected")

        # Go Back
        # self.driver.find_element(By.CLASS_NAME, "option-btn").click()

        # Delete Image
        # self.driver.find_element(By.CLASS_NAME, "inline-delete-btn").click()
        # message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        # self.assertEqual(message_element.text, "image deleted successfully!", "change is not as expected")

        # Delete Post
        # self.driver.find_element(By.NAME, "delete_post").click()
        # message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        # self.assertEqual(message_element.text, "post deleted successfully!", "change is not as expected")

    def test_View(self):
        post_form = self.driver.find_element(By.XPATH, "//form[@method='post' and input[@name='post_id'][@value='19']]")
        post_form.find_element(By.CLASS_NAME, "btn").click()
        self.driver.implicitly_wait(3)

        # delete post
        self.driver.find_element(By.CLASS_NAME, "inline-delete-btn").click()
        try:
            alert = self.driver.switch_to.alert

            alert.accept()
        except:
            pass

        # Go back
        # self.driver.find_element(By.XPATH, "//a[@class='inline-option-btn' and @href='view_posts.php']")

        # Edit
        # self.driver.find_element(By.XPATH,"//a[@class='inline-option-btn' and contains(@href, 'edit_post.php?id=18')]").click()

        # Delete comments
        # self.driver.find_element(By.NAME, "delete_comment").click()
        # try:
        #     alert = self.driver.switch_to.alert
        #
        #     alert.accept()
        # except:
        #     pass







