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



    def click_sort_dropdown(self, should_check=True):
        element= self.wait.until(EC.presence_of_element_located(SEARCH.SORT))
        is_selected = self.driver.execute_script("return arguments[0].checked;",element)
        if is_selected != should_check:
            self.driver.execute_script('arguments[0].click();', element)

    def select_a_z_sort(self,text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.A_Z_SORT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, text)

    def select_newest_sort(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.NEWEST_SORT)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def select_oldest_sort(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.OLDEST_SORT)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def click_apply_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.APPLY_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def enter_search_text(self, text):
        enter_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.SEARCH_BOX)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", enter_text, text)


    def click_language_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.LANGUAGE)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def select_all_languages(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.ALL_LANGUAGES)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def select_python(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.PYTHON)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def select_ruby(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.RUBY)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def select_sql(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SEARCH.SQL)
        )
        self.driver.execute_script("arguments[0].click();", element)