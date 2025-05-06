import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import uuid
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.tags import Tags

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


def test_tags_button(login,driver):
    tags= Tags(driver)
    tags.click_tag()

# def test_create_new_tag(login,driver):
#     new_tags=Tags(driver)
#     # new_tags.click_tag()
#     new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
#     new_tags.click_new_tags()
#     new_tags.enter_tag_name("News Tag")
#     new_tags.click_create_button()
#     expected_result="Tag was successfully created."
#     actual_result=new_tags.success_message()
#     assert actual_result==expected_result, f"Expected'{expected_result}', but got '{actual_result}'"
#     print("Test Passed :Tag was created successfully")



def test_update_the_tags(login,driver):
    new_tags = Tags(driver)
    # new_tags.click_tag()
    new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
    new_tags.click_edit_button()
    new_tags.enter_tag_name("first Tag")
    new_tags.click_update_tag_button()

def test_create_tag_with_existing_tag(login,driver):
    new_tags=Tags(driver)
    new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
    new_tags.click_new_tags()
    new_tags.enter_tag_name("News Tag")
    new_tags.click_create_button()
    expected_result="Please review the problems below:"
    actual_result=new_tags.existing_tag_name_message()
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed :Name has already taken")


def test_create_tags_with_one_letter(login, driver):
    new_tags = Tags(driver)
    new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
    new_tags.click_new_tags()
    new_tags.enter_tag_name("N")
    new_tags.click_create_button()
 # In this system, even one letter is accepted (BUG).
    expected_result = "Please review the problems below:"  # We expect an error
    actual_result = new_tags.success_message()  # But success message comes
 # Force the test to fail if success message is seen
    assert actual_result != "Tag was successfully created.", \
        f"Test Failed: Tag was incorrectly created with one letter. Message shown: '{actual_result}'"

    print("Test Passed: One-letter tag was created, but it should NOT be allowed (Negative Test detected bug).")


def test_delete_the_tags(login,driver):
    new_tags = Tags(driver)
    new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
    new_tags.click_delete_button()
    expected_result = "Tag was successfully destroyed."
    actual_result =new_tags.delete_message()
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed :")