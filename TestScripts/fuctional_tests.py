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

        # When he hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do list.

        # There is still a text box inviting him to add another item. He
        # enters "Use peacock feathers to make a fly" (Ryan is very methodical)









if __name__ == '__main__':
    unittest.main(warnings='ignore')



