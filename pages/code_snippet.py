from selenium.webdriver.support import expected_conditions as EC
import time

class CodeSnippet:
    def __init__(self, driver):
        self.driver = driver

    def open_sign_up_page(self, url):
        self.driver.get(url)