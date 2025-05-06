import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage

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


# def test_login_with_valid_credentials(driver):
#     login_page = LoginPage(driver)
#     login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
#     login_page.login()
#     login_page.enter_email("test@gmail.com")
#     login_page.enter_password("password")
#     login_page.click_remember_me()
#     login_page.click_login()
#     expected_result = "Signed in successfully."
#     actual_result = login_page.get_login_validation_message()
#     print(f"Expected: {expected_result}")
#     print(f"Actual: {actual_result}")
#
#     assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
#     print("Test Passed: Login with valid credentials successful.")
#     login_page.logout_button()
#     print(" Successfully logged out.")


def test_login_with_invalid_email_valid_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    login_page.login()
    login_page.enter_email("testing@gmail.com")
    login_page.enter_password("password")
    login_page.click_remember_me()
    login_page.click_login()
    expected_result = "Invalid Email or password."
    actual_result = login_page.get_email_validation_message().strip()
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual_result}")

    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Login with invalid email and valid password generates the expected error..")

def test_login_with_valid_email_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    login_page.login()
    login_page.enter_email("test@gmail.com")
    login_page.enter_password("Sarina")
    login_page.click_remember_me()
    login_page.click_login()
    expected_result = "Invalid Email or password."
    actual_result = login_page.get_email_validation_message().strip()
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual_result}")

    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Login with valid email and invalid password generates the expected error..")

def test_login_with_empty_field(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    login_page.login()
    login_page.enter_email("")
    login_page.enter_password("")
    login_page.click_remember_me()
    login_page.click_login()
    expected_result = "Invalid Email or password."
    actual_result = login_page.get_email_validation_message().strip()
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual_result}")

    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Login with empty field generates the expected error..")

# Password Recovery
def test_password_recovery_with_email_field(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    login_page.login()
    login_page.click_forgot_password()
    login_page.enter_email_in_forgot_password_field("test@gmail.com")
    login_page.click_reset_instruction_btn()

def test_password_recovery_with_empty_email_field(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    login_page.login()
    login_page.click_forgot_password()
    login_page.enter_email_in_forgot_password_field("")
    time.sleep(5)
    login_page.click_reset_instruction_btn()
    time.sleep(5)
    expected_result = "Email can't be blank"
    actual_result = login_page.get_reset_password_validation_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Password reset with empty email generate correct validation error message.")

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

def test_logout_button(driver,login):
    logout_button=LoginPage(driver)
    logout_button.logout_button()
