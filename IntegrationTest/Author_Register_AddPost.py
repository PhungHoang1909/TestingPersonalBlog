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

    def test_Register_AddPost(self):
        self.driver.find_element(By.LINK_TEXT, "Author").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.implicitly_wait(2)

        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("admin104")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("admin104")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("admin104")

        self.driver.find_element(By.NAME, "submit").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(By.XPATH, "//a[@href='add_posts.php' and @class='btn']").click()

        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("My Post Title")

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("This is my post content")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        file_input = self.driver.find_element(By.NAME, "image")
        image_path = r"D:\Study\Năm 3\HKII\KiemThuPhanMem\UnitTest_PersonalBlog\AuthorFunctions\img0.jpg"
        file_input.send_keys(image_path)

        self.driver.find_element(By.NAME, "publish").click()

        message_element = self.driver.find_element(By.XPATH, "//div[@class='message']/span")
        self.assertEqual(message_element.text, "post published!", "Post publishing message is not as expected")



