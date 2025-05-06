import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.all_kanji import KANJI

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class all_kanji:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def open_kanji_page(self, url):
        self.driver.get(url)

    def click_all_kanji_link(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(KANJI.ALL_KANJI_LINK)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def enter_kanji_name(self,input):
        send_input = self.wait.until(EC.presence_of_element_located(KANJI.SEARCH))
        self.driver.execute_script("arguments[0].value = arguments[1];", send_input,input)


    def click_search_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(KANJI.KANJI_BUTTON ))
        self.driver.execute_script("arguments[0].click();", button)

    def click_river_kanji(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(KANJI.RIVER_KANJI ))
        self.driver.execute_script("arguments[0].click();", button)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def click_back_to_kanji_list(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(KANJI.BACK_TO_KANJI_LIST))
        self.driver.execute_script("arguments[0].click();", button)


