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
    # options.add_argument('--headless=new')  # Use new headless mode for better compatibility
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--window-size=1920,1080')  # Instead of maximize_window()

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")


def test_signup_with_valid_credentials(driver):
    sign_up_page = SignUp(driver)
    sign_up_page.open_sign_up_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")
    sign_up_page.click_sign_up_button()
    sign_up_page.enter_email("test@gmail.com")
    sign_up_page.enter_password("password")
    sign_up_page.enter_confirm_password("password")
    sign_up_page.click_sign_up()
    time.sleep(2)




def test_signup_with_already_registered_email(driver):
    sign_up_page = SignUp(driver)
    sign_up_page.open_sign_up_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")
    sign_up_page.click_sign_up_button()
    sign_up_page.enter_email("test@gmail.com")
    sign_up_page.enter_password("password")
    sign_up_page.enter_confirm_password("password")
    sign_up_page.click_sign_up()
    time.sleep(2)

    expected_result = "Email has already been taken"

    actual_result = sign_up_page.get_field_validation_error_msg_signUp()

    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with aleardy registered email")

def test_signup_with_empty_credentials(driver):
    sign_up_page=SignUp(driver)
    sign_up_page.open_sign_up_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")
    sign_up_page.click_sign_up_button()
    sign_up_page.enter_email("")
    sign_up_page.enter_password("")
    sign_up_page.enter_confirm_password("")
    sign_up_page.click_sign_up()
    time.sleep(2)
    expected_result="Please review the problems below:"
    actual_result=sign_up_page.get_validation_error_signUp()
    assert actual_result==expected_result, f"Expected '{expected_result}',but got '{actual_result}'"
    print("Test passed:Received the correct validation message sign up with empty fields")

def test_signup_with_empty_email(driver):
    sign_up_page=SignUp(driver)
    sign_up_page.open_sign_up_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")
    sign_up_page.click_sign_up_button()
    sign_up_page.enter_email("")
    sign_up_page.enter_password("password")
    sign_up_page.enter_confirm_password("password")
    sign_up_page.click_sign_up()
    time.sleep(2)
    expected_result="Email can't be blank"
    actual_result=sign_up_page.get_field_validation_error_msg_signUp()
    assert actual_result==expected_result, f"Expected'{expected_result}',but got '{actual_result}'"
    print("Test Passed:Test passed:Received the correct validation message sign up with empty email")

def test_signup_with_empty_password(driver):
    sign_up_page=SignUp(driver)
    sign_up_page.open_sign_up_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")
    sign_up_page.click_sign_up_button()
    sign_up_page.enter_email("test@gmail.com")
    sign_up_page.enter_password("")
    sign_up_page.enter_confirm_password("")
    sign_up_page.click_sign_up()
    time.sleep(2)
    expected_result = "Password can't be blank"
    actual_result = sign_up_page.get_field_validation_empty_password()
    print(f"Expected Validation Message: '{expected_result}'")
    print(f"Actual Validation Message:   '{actual_result}'")

    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Received the correct validation message when signing up with empty password")


def test_signUp_with_different_password_and_confirmPassword(driver):
    sign_up_page = SignUp(driver)
    sign_up_page.open_sign_up_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")
    sign_up_page.click_sign_up_button()
    sign_up_page.enter_email("test@gmail.com")
    sign_up_page.enter_password("Sarina")
    sign_up_page.enter_confirm_password("Bati")
    sign_up_page.click_sign_up()
    time.sleep(2)
    expected_result = "Password confirmation doesn't match Password"

    actual_result = sign_up_page.get_field_validation_mismatched_password()

    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print(
        "Test Passed: Received the correct validation message when signing up with different password and confirm password")


#