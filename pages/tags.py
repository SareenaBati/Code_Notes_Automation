import sys
import os

from h11 import SEND_BODY
from pyexpat.errors import messages

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

    def click_new_tags(self):
        new_tag=self.wait.until(EC.presence_of_element_located(TagsLocator.NEW_TAG_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);",new_tag)
        self.driver.execute_script("arguments[0].click();",new_tag)

    def enter_tag_name(self,tag):
        tag_name=self.wait.until(EC.presence_of_element_located(TagsLocator.TAG_NAME))
        self.driver.execute_script("arguments[0].value = arguments[1];",tag_name,tag)

    def click_create_button(self):
        create_button=self.wait.until(EC.presence_of_element_located(TagsLocator.CREATE_BUTTON))
        self.driver.execute_script("arguments[0].click();",create_button)

    def success_message(self):
        message=self.wait.until(EC.presence_of_element_located(TagsLocator.SUCCESS_MESSAGE))
        text=self.driver.execute_script("arguments[0].textContent",message)
        return text

    def click_edit_button(self):
        edit_button=self.wait.until(EC.presence_of_element_located(TagsLocator.EDIT_BUTTON))
        self.driver.execute_script("arguments[0].click();",edit_button)

    def click_update_tag_button(self):
        update_button=self.wait.until(EC.presence_of_element_located(TagsLocator.UPDATE_TAG_BUTTON ))
        self.driver.execute_script("arguments[0].click();",update_button)

    def edit_message(self):
        message=self.wait.until(EC.presence_of_element_located(TagsLocator.EDIT_MESSAGE))
        text=self.driver.execute_script("arguments[0].textContent",message)
        return text

    def existing_tag_name_message(self):
        message = self.wait.until(EC.presence_of_element_located(TagsLocator.REPEAT_TAG_NAME))

        text = self.driver.execute_script("return arguments[0].textContent;", message)
        return text

    def click_delete_button(self):
        delete_button=self.wait.until(EC.presence_of_element_located(TagsLocator.UPDATE_TAG_BUTTON ))
        self.driver.execute_script("arguments[0].click();",delete_button)


    def delete_message(self):
        message = self.wait.until(EC.presence_of_element_located(TagsLocator.DELETE_MESSAGE))

        text = self.driver.execute_script("return arguments[0].textContent;", message)
        return text


