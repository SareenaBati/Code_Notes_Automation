import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.tags import TagsLocator

class Tags:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Increased wait time for reliability

    def open_page(self, url):
        self.driver.get(url)

    def click_tag(self):

        snippet = self.wait.until(EC.presence_of_element_located(TagsLocator.TAGS_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", snippet)
        self.driver.execute_script("arguments[0].click();", snippet)
