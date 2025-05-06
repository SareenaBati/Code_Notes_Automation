import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.kanji_for_beginners import KANJI

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class KanjiSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_kanji_page(self, url):
        self.driver.get(url)

    def click_kanji_for_beginners(self):
        try:
            button = self.wait.until(
                EC.element_to_be_clickable(KANJI.KANJI_FOR_BEGINNERS_BUTTON)
            )
            self.driver.execute_script("arguments[0].click();", button)
            print("Clicked on Kanji for Beginners button")
        except TimeoutException:
            print("Kanji for Beginners button not clickable")

    def enter_search_text(self, text):
        try:
            search_box = self.wait.until(
                EC.presence_of_element_located(KANJI.SEARCH_KANJI)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
            self.driver.execute_script("arguments[0].focus();", search_box)

            # Avoid clear() to prevent JS error
            self.driver.execute_script("arguments[0].value = '';", search_box)
            search_box.send_keys(text)

            print(f"Entered search text: {text}")
        except TimeoutException:
            print("Search input field not found or not interactable")
            raise

    def click_search_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(KANJI.KANJI_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)

    def get_error_message(self):
        error_message = self.wait.until(EC.presence_of_element_located(KANJI.ERROR_MESSAGE))
        text = self.driver.execute_script("return arguments[0].textContent", error_message)
        return text

    def get_error_message_with_empty_input(self):
        error_message = self.wait.until(EC.presence_of_element_located(KANJI.ERROR_MESSAGE_WITH_EMPTY_INPUT))
        text = self.driver.execute_script("return arguments[0].textContent", error_message)
        return text