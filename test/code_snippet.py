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
from pages.code_snippet import Snippet

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


def test_edit_code_snippet_without_login(driver):
    snippet=Snippet(driver)
    snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    snippet.click_view_snippet()
    snippet.click_edit_snippet()

    expected_result="You need to sign in or sign up before continuing."
    actual_result=snippet.edit_error_message()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got'{actual_result}'"
    print("Test Passed:Without signing in, the snippet could not be edited .")


def test_delete_code_snippet_without_login(driver):
    snippet=Snippet(driver)
    snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    snippet.click_view_snippet()
    snippet.click_delete_snippet()

    expected_result="You need to sign in or sign up before continuing."
    actual_result=snippet.delete_error_message()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got'{actual_result}'"
    print("Test Passed:Without signing in, the snippet could not be deleted ")


