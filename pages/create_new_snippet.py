import sys
import os
from audioop import error
from gettext import textdomain

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.create_new_snippet_locator import CreateNewSnippetLocators
from selenium.common.exceptions import StaleElementReferenceException
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class CreateNewSnippet:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def open_page(self, url):
        self.driver.get(url)



    def click_code_snippet(self):
        code_snippet = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.CODE_SNIPPET))
        self.driver.execute_script("arguments[0].click();", code_snippet)

    def click_new_code_snippet(self):
        new_code_snippet = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.NEW_CODE_SNIPPET))
        self.driver.execute_script("arguments[0].click();", new_code_snippet)




    def fill_snippet_form(self, title, language, description, code):
        try:
            title_input = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.INPUT_TITLE))
            language_input = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.INPUT_LANGUAGE))
            desc_input = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.INPUT_DESCRIPTION))
            code_input = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.INPUT_CODE))

            self.driver.execute_script("arguments[0].value = arguments[1];", title_input, title)
            self.driver.execute_script("arguments[0].value = arguments[1];", language_input, language)
            self.driver.execute_script("arguments[0].value = arguments[1];", desc_input, description)

            if code_input.tag_name in ['textarea', 'input']:
                self.driver.execute_script("arguments[0].value = arguments[1];", code_input, code)
            else:
                self.driver.execute_script("arguments[0].innerText = arguments[1];", code_input, code)

        except StaleElementReferenceException:

            time.sleep(1)
            self.fill_snippet_form(title, language, description, code)

    def private_checkbox(self, should_check=True):
        private_checkbox = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.PRIVATE_CHECKBOX ))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", private_checkbox)  # Scroll into view
        is_selected = self.driver.execute_script("return arguments[0].checked;", private_checkbox)
        if is_selected != should_check:
            self.driver.execute_script('arguments[0].click();', private_checkbox)  # Click using JS if checkbox needs to be toggled

    def select_first_tag(self):
        tags = self.wait.until(EC.presence_of_all_elements_located(CreateNewSnippetLocators.INPUT_TAGS))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", tags[0])
        self.driver.execute_script("arguments[0].click();", tags[0])

    def create_code_snippet_button(self, should_check=True):
        button= self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.CREATE_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)  # Scroll into view
        is_selected = self.driver.execute_script("return arguments[0].checked;", button)
        if is_selected != should_check:
            self.driver.execute_script('arguments[0].click();', button)


    def success_msg(self):
        success_msg = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.SUCCESSFUL_MESSAGE))
        text = self.driver.execute_script("return arguments[0].textContent", success_msg)
        return text

    def snippet_error_msg(self):
        error_msg=self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.ERROR_MESSAGE))
        text=self.driver.execute_script("return arguments[0].textContent",error_msg)
        return text

    def title_error_msg(self):
        title_error_msg=self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.TITLE_ERROR_MESSAGE))
        text=self.driver.execute_script("return arguments[0].textContent",title_error_msg)
        return text

    def language_error_msg(self):
        language_error = self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.LANGUAGE_ERROR_MESSAGE))
        text = self.driver.execute_script("return arguments[0].textContent", language_error)
        return text


    def code_error_msg(self):
        code_error_message = self.wait.until(EC.visibility_of_element_located(CreateNewSnippetLocators.CODE_BLANK_ERROR_MESSAGE))
        text = self.driver.execute_script("return arguments[0].textContent", code_error_message)
        return text



    def logout_button(self, should_check=True):
        logout= self.wait.until(EC.presence_of_element_located(CreateNewSnippetLocators.LOGOUT_BUTTON))
        is_selected = self.driver.execute_script("return arguments[0].checked;", logout)
        if is_selected != should_check:
            self.driver.execute_script('arguments[0].click();', logout)



