from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.search_snippet import SEARCH



class Search:
    def __init__(self,driver):
        self.driver=driver
        self.wait= WebDriverWait(self.driver,10)

    def open_page(self,url):
        self.driver.get(url)

    def click_dashboard(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.DASHBOARD)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def click_all_snippet(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.ALL_SNIPPET)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def click_public(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.PUBLIC_SNIPPET)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def click_private(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.PRIVATE_SNIPPET)
        )
        self.driver.execute_script("arguments[0].click();", button)