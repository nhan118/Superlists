# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def can_start_a_list_and_retirvev_it_later(self):
        # Ryan hear about a new cool online to-do app.
        # He goes to check out its homepage.
        self.browser.get("http://localhost:8000")

        # He notices the page tile and header mention to-do list.
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # He is invited to enter a to-do item straight away

        # He types "Buy peacock feathers"(Ryan's hobby is tying fly-fishing lures)






if __name__ == '__main__':
    unittest.main(warnings='ignore')



