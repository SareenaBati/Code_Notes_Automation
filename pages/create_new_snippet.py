import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, JavascriptException
from locators.create_new_snippet_locator import CreateNewSnippetLocators

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class CreateNewSnippet:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url):
        self.driver.get(url)

    def click_new_code_snippet(self):
        try:
            element = self.wait.until(EC.element_to_be_clickable(CreateNewSnippetLocators.NEW_CODE_SNIPPET))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            print(" ERROR: 'New Code Snippet' button not clickable.")
    #
    # def fill_snippet_form(self, title, language, description, code):
    #     try:
    #         title_input = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.INPUT_TITLE))
    #         language_input = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.INPUT_LANGUAGE))
    #         desc_input = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.INPUT_DESCRIPTION))
    #         code_input = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.INPUT_CODE))
    #
    #         self.driver.execute_script("arguments[0].value = arguments[1];", title_input, title)
    #         self.driver.execute_script("arguments[0].value = arguments[1];", language_input, language)
    #         self.driver.execute_script("arguments[0].value = arguments[1];", desc_input, description)
    #
    #         if code_input.tag_name in ['textarea', 'input']:
    #             self.driver.execute_script("arguments[0].value = arguments[1];", code_input, code)
    #         else:
    #             self.driver.execute_script("arguments[0].innerText = arguments[1];", code_input, code)
    #     except (TimeoutException, JavascriptException) as e:
    #         print(f" ERROR: Failed to fill snippet form: {str(e)}")
    #
    # def select_private(self):
    #     try:
    #         checkbox = self.wait.until(EC.element_to_be_clickable(CreateNewSnippetLocators.INPUT_PRIVATE))
    #         self.driver.execute_script("arguments[0].click();", checkbox)
    #     except TimeoutException:
    #         print(" ERROR: 'Private' checkbox not clickable.")
    #
    # def select_first_tag(self):
    #     try:
    #         tags = self.wait.until(EC.presence_of_all_elements_located(CreateNewSnippetLocators.INPUT_TAGS))
    #         if tags:
    #             self.driver.execute_script("arguments[0].scrollIntoView(true);", tags[0])
    #             self.driver.execute_script("arguments[0].click();", tags[0])
    #         else:
    #             print(" No tags found to select.")
    #     except TimeoutException:
    #         print(" ERROR: No tags available to select.")
    #
    # def submit_form(self):
    #     try:
    #         button = self.wait.until(EC.element_to_be_clickable(CreateNewSnippetLocators.CREATE_BTN))
    #         self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
    #         self.driver.execute_script("arguments[0].click();", button)
    #     except TimeoutException:
    #         print(" ERROR: Submit button not clickable.")
