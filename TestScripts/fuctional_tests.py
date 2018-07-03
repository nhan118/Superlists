# -*- coding:utf-8 -*-

from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("http://localhost:8000")
browser.maximize_window()
time.sleep(3)
assert 'Django' in browser.title
browser.quit()


