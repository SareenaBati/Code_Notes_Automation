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
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sign_up_page import SignUp
from pages.create_new_snippet import CreateNewSnippet
from pages.tags import Tags

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



# # def test_password_recovery_with_empty_email_field(driver):
# #     login_page = LoginPage(driver)
# #     login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
#       login_page.login()
# #     login_page.click_forgot_password()
# #     time.sleep(1)
# #
# #     login_page.enter_email_in_forgot_password_field("")
# #     login_page.click_reset_instruction_btn()
# #     expected_result = "Email can't be blank"
# #
# #
# #     actual_result = login_page.get_reset_password_validation_error_msg()
# #     assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
# #     print("Test Passed: Password reset with empty email generate correct validation error message.")


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
    time.sleep(2)
    return driver

# def test_create_new_snippet(login,driver):
#     new_snippet = CreateNewSnippet(driver)
#     new_snippet.click_code_snippet()
#     new_snippet.click_new_code_snippet()
#     new_snippet.fill_snippet_form(
#         title="Test ",
#         language="Python",
#         description="This is a test description for the snippet.",
#         code="print('Hello, World!')"
#     )
#     new_snippet.private_checkbox()
#     new_snippet.select_first_tag()
#     new_snippet.create_code_snippet_button()
#     time.sleep(2)
#
#     expected_result="Code snippet was successfully created."
#     actual_result=new_snippet.success_msg()
#     print(f"Expected: {expected_result}")
#     print(f"Actual: {actual_result}")
#     assert actual_result==expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
#     assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
#     print ("Test Passed:Code snippet created successfully")
#     new_snippet.logout_button()
#     print("Test Passed:Code snippet logout successfully")

# def test_create_new_snippet_public(login,driver):
#     new_snippet = CreateNewSnippet(driver)
#     new_snippet.click_code_snippet()
#     new_snippet.click_new_code_snippet()
#     time.sleep(2)
#     new_snippet.fill_snippet_form(
#         title="Test Snippet",
#         language="Python",
#         description="This is a test description for the snippet.",
#         code="print('Hello, World!')"
#     )
#     time.sleep(2)
#     new_snippet.select_first_tag()
#     new_snippet.create_code_snippet_button()
#     time.sleep(5)
#     expected_result = "Code snippet was successfully created."
#     actual_result = new_snippet.success_msg()
#     assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
#     assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
#     print("Test Passed:Code snippet created successfully")
#     new_snippet.logout_button()
#     print("Test Passed:Code snippet logout successfully")
#
def test_create_snippet_with_empty_field(login,driver):
    new_snippet = CreateNewSnippet(driver)
    new_snippet.click_code_snippet()
    new_snippet.click_new_code_snippet()
    new_snippet.fill_snippet_form(
        title="",
        language="",
        description="",
        code=""
    )

    new_snippet.private_checkbox()
    new_snippet.select_first_tag()
    new_snippet.create_code_snippet_button()
    expected_result="Please review the problems below:"
    actual_result=new_snippet.snippet_error_msg()
    assert actual_result==expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print ("Test Passed:Please review the problems below:")
    new_snippet.logout_button()
    print("Test Passed:Code snippet logout successfully")


#
def test_create_snippet_without_title(login,driver):
    new_snippet = CreateNewSnippet(driver)
    new_snippet.click_code_snippet()
    new_snippet.click_new_code_snippet()
    time.sleep(5)
    new_snippet.fill_snippet_form(
        title="",
        language="Python",
        description="This is a test description for the snippet.",
        code="print('Hello, World!')"
    )
    new_snippet.select_first_tag()
    new_snippet.create_code_snippet_button()
    expected_result = "Title can't be blank"
    actual_result = new_snippet.title_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed:title cant be blank:")
    new_snippet.logout_button()
    print("Test Passed:Code snippet logout successfully")

def test_create_snippet_without_language(login,driver):
    new_snippet = CreateNewSnippet(driver)
    new_snippet.click_code_snippet()
    new_snippet.click_new_code_snippet()
    new_snippet.fill_snippet_form(
        title="Test Snippet",
        language="",
        description="This is a test description for the snippet.",
        code="print('Hello, World!')"
    )
    time.sleep(2)
    new_snippet.select_first_tag()
    time.sleep(1)
    new_snippet.create_code_snippet_button()
    expected_result = "Language can't be blank"
    actual_result = new_snippet.language_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed:language cant be blank:")
    new_snippet.logout_button()
    print("Test Passed:Code snippet logout successfully")
#
#
def test_create_snippet_without_description(login,driver):
    new_snippet = CreateNewSnippet(driver)
    new_snippet.click_code_snippet()
    new_snippet.click_new_code_snippet()
    time.sleep(5)
    new_snippet.fill_snippet_form(
        title="Test Snippet",
        language="Python",
        description="",
        code="print('Hello, World!')"
    )
    time.sleep(2)
    new_snippet.select_first_tag()
    time.sleep(1)
    new_snippet.create_code_snippet_button()
    time.sleep(5)
    new_snippet.logout_button()
    print("Test Passed:Code snippet logout successfully")

def test_create_snippet_without_code(login,driver):
    new_snippet = CreateNewSnippet(driver)
    new_snippet.click_code_snippet()
    new_snippet.click_new_code_snippet()
    new_snippet.fill_snippet_form(
        title="Test Snippet",
        language="Python",
        description="Description",
        code=""
    )
    time.sleep(2)
    new_snippet.select_first_tag()
    time.sleep(1)
    new_snippet.create_code_snippet_button()
    time.sleep(1)
    expected_result = "Code can't be blank"
    actual_result = new_snippet.code_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed:code cant be blank:")
    new_snippet.logout_button()
    print("Test Passed:Code snippet logout successfully")


def test_tags(login,driver):
    tags= Tags(driver)
    tags.click_tag()
    time.sleep(5)


# Add pytest.main() for running tests with python run_test.py
if __name__ == "__main__":
    pytest.main(["-v", "--tb=short", "run_test.py"])







