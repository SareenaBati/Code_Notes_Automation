from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.code_snippet import SNIPPET



class Snippet:
    def __init__(self,driver):
        self.driver=driver
        self.wait= WebDriverWait(self.driver,10)

    def open_page(self,url):
        self.driver.get(url)

    def click_view_snippet(self):
        view_snippet=self.wait.until(EC.presence_of_element_located(SNIPPET.VIEW_LINKS))
        self.driver.execute_script("arguments[0].click();", view_snippet)

    def click_edit_snippet(self):
        edit_snippet = self.wait.until(EC.presence_of_element_located(SNIPPET.EDIT_LINKS))
        self.driver.execute_script("arguments[0].click();", edit_snippet)

    def click_delete_snippet(self):
        delete_snippet = self.wait.until(EC.presence_of_element_located(SNIPPET.DELETE_LINKS))
        self.driver.execute_script("arguments[0].click();", delete_snippet)

    def edit_error_message(self):
        message = self.wait.until(EC.presence_of_element_located(SNIPPET.ERROR_MESSAGE_EDIT_WITHOUT_SIGNIN))
        text=self.driver.execute_script(" return arguments[0].textContent",message)
        return text

    def delete_error_message(self):
        delete_message = self.wait.until(EC.presence_of_element_located(SNIPPET.ERROR_MESSAGE_DELETE_WITHOUT_SIGNIN))
        text=self.driver.execute_script(" return arguments[0].textContent",delete_message)
        return text


