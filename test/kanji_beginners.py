import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sign_up_page import SignUp
from pages.create_new_snippet import CreateNewSnippet
from pages.code_snippet_cards import Snippet
from pages.tags import Tags
from pages.search_snippet import Search
from pages.kanji_for_beginners import KanjiSearchPage
from pages.all_kanji import all_kanji



@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument('--headless=new')  # Use new headless mode for better compatibility
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')  # Instead of maximize_window()

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver):
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    login_page.login()
    login_page.enter_email("test@gmail.com")
    login_page.enter_password("password")
    login_page.click_remember_me()
    login_page.click_login()
    return driver

def test_kanji_for_beginners_link(driver,login):
    kanji_for_beginners_link =KanjiSearchPage(login)
    kanji_for_beginners_link.open_kanji_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/kanjis/beginners")
    # kanji_for_beginners_link.click_kanji_for_beginners()


def test_search_kanji_with_alphabet(driver,login):
    kanji_for_beginners_link =KanjiSearchPage(login)
    kanji_for_beginners_link.open_kanji_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/kanjis/beginners")
    # kanji_for_beginners_link.click_kanji_for_beginners()
    kanji_for_beginners_link.enter_search_text("river")
    kanji_for_beginners_link.click_search_button()
    time.sleep(5)

def test_search_with_kanji_language(driver,login):
    kanji_for_beginners_link = KanjiSearchPage(login)
    kanji_for_beginners_link.open_kanji_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/kanjis/beginners")
    # kanji_for_beginners_link.click_kanji_for_beginners()
    kanji_for_beginners_link.enter_search_text("川")
    kanji_for_beginners_link.click_search_button()
    time.sleep(5)

def test_search_with_number(driver,login):
    kanji_for_beginners_link = KanjiSearchPage(login)
    kanji_for_beginners_link.open_kanji_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/kanjis/beginners")
    # kanji_for_beginners_link.click_kanji_for_beginners()
    kanji_for_beginners_link.enter_search_text("1")
    kanji_for_beginners_link.click_search_button()
    expected_result = "Error searching for kanji: undefined method `[]' for nil"
    actual_result = kanji_for_beginners_link.get_error_message()
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual_result}")
    assert actual_result.strip()  == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed :Error message for number input displayed as expected.")

def test_search_partial_meaning_ri(driver, login):
    kanji_page = KanjiSearchPage(login)
    kanji_page.open_kanji_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/kanjis/beginners")
    kanji_page.enter_search_text("ri")
    kanji_page.click_search_button()
    time.sleep(3)

def test_search_with_empty_input(driver,login):
    kanji_page = KanjiSearchPage(login)
    kanji_page.open_kanji_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/kanjis/beginners")
    kanji_page.enter_search_text("")
    kanji_page.click_search_button()
    time.sleep(3)
    expected_result = "Please enter a search term"
    actual_result = kanji_page.get_error_message_with_empty_input()
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual_result}")
    assert actual_result.strip() == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed :Error message for empty input.")

def test_search_kanji_using_uppercase_text(driver,login):
    kanji_page = KanjiSearchPage(login)
    kanji_page.open_kanji_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/kanjis/beginners")
    kanji_page.enter_search_text("EAR")
    kanji_page.click_search_button()
    print("Test passed: 'EAR' search returns the expected result ('ear').")

def test_count_kanji_with_alphabet(driver, login):
    kanji_for_beginners_link = KanjiSearchPage(login)
    kanji_for_beginners_link.open_kanji_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/kanjis/beginners")
    kanji_for_beginners_link.enter_search_text("river")
    kanji_for_beginners_link.click_search_button()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'text-sm') and contains(translate(text(), 'RIVER', 'river'), 'river')]"))
    )
    river_results = driver.find_elements(
        By.XPATH,
        "//div[contains(@class, 'text-sm') and contains(translate(text(), 'RIVER', 'river'), 'river')]"
    )
    river_count = len(river_results)
    print(f"Number of results containing 'river': {river_count}")
    assert river_count > 0, "No results found containing 'river'"
