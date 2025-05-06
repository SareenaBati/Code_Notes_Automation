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
from pages.create_new_snippet import CreateNewSnippet




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




def test_create_new_snippet_public(login):
    new_snippet = CreateNewSnippet(login)
    # new_snippet.click_code_snippet()
    # new_snippet.click_new_code_snippet()
    new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")

    time.sleep(2)
    new_snippet.fill_snippet_form(
        title="Test Snippet",
        language="Python",
        description="This is a test description for the snippet.",
        code="print('Hello, World!')"
    )
    time.sleep(2)
    new_snippet.select_first_tag()
    new_snippet.create_code_snippet_button()
    time.sleep(5)
    expected_result = "Code snippet was successfully created."
    actual_result = new_snippet.success_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed:Code snippet created successfully")
    # new_snippet.logout_button()
    # print("Test Passed:Code snippet logout successfully")



def test_create_snippet_with_empty_field(login):
    new_snippet = CreateNewSnippet(login)
    # new_snippet.click_code_snippet()
    # new_snippet.click_new_code_snippet()
    new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
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




#
def test_create_snippet_without_title(login,driver):
    new_snippet = CreateNewSnippet(driver)
    # new_snippet.click_code_snippet()
    # new_snippet.click_new_code_snippet()
    new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
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


def test_create_snippet_without_language(login,driver):
    new_snippet = CreateNewSnippet(driver)
    # new_snippet.click_code_snippet()
    # new_snippet.click_new_code_snippet()
    new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
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
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual_result}")
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed:language cant be blank:")



def test_create_snippet_without_description(login,driver):
    new_snippet = CreateNewSnippet(driver)
    # new_snippet.click_code_snippet()
    # new_snippet.click_new_code_snippet()
    new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
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



def test_create_snippet_without_code(login,driver):
    new_snippet = CreateNewSnippet(driver)
    # new_snippet.click_code_snippet()
    # new_snippet.click_new_code_snippet()
    new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
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



