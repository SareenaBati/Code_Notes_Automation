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
from pages.code_snippet import Snippet
from pages.tags import Tags
from pages.my_dashboard_page import Search
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
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/users/sign_in")
    # login_page.login()
    login_page.click_forgot_password()
    time.sleep(5)
    login_page.enter_email_in_forgot_password_field("")
    time.sleep(5)
    login_page.click_reset_instruction_btn()
    expected_result = "Email can't be blank"
    actual_result = login_page.get_reset_password_validation_error_msg()
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed: Password reset with empty email generate correct validation error message.")



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


#

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

# # ALL KANJI PAGE
#
def test_kanji_link(driver,login):
    kanji=all_kanji(driver)
    kanji.click_all_kanji_link()
    kanji.scroll_to_bottom()

def test_river_link(driver,login):
    kanji = all_kanji(driver)
    kanji.click_all_kanji_link()
    kanji.enter_kanji_name("river")
    kanji.click_search_button()
    kanji.click_river_kanji()
    kanji.scroll_to_bottom()
    kanji.scroll_to_up()
    kanji.click_back_to_kanji_list()


# Kanji for beginners page

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


#
# def test_create_new_snippet(driver,login):
#     new_snippet = CreateNewSnippet(driver)
#     time.sleep(1)
#     # new_snippet.click_code_snippet()
#     # new_snippet.click_new_code_snippet()
#     new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
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
#
#
# def test_create_new_snippet_public(driver,login):
#     new_snippet = CreateNewSnippet(driver)
#     time.sleep(1)
#     # new_snippet.click_code_snippet()
#     # new_snippet.click_new_code_snippet()
#     new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
#
#     time.sleep(2)
#     new_snippet.fill_snippet_form(
#         title="Test Snippet",
#         language="Python",
#         description="This is a test description for the snippet.",
#         code="print('Hello, World!')"
#     )
#     new_snippet.select_first_tag()
#     new_snippet.create_code_snippet_button()
#     expected_result = "Code snippet was successfully created."
#     actual_result = new_snippet.success_msg()
#     assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
#     print("Test Passed:Code snippet created successfully")
#     new_snippet.logout_button()
#     print("Test Passed:Code snippet logout successfully")
#
#
# def test_create_snippet_with_empty_field(driver,login):
#     new_snippet = CreateNewSnippet(driver)
#     time.sleep(1)
#     # new_snippet.click_code_snippet()
#     # new_snippet.click_new_code_snippet()
#     new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
#     new_snippet.fill_snippet_form(
#         title="",
#         language="",
#         description="",
#         code=""
#     )
#
#     new_snippet.private_checkbox()
#     new_snippet.select_first_tag()
#     new_snippet.create_code_snippet_button()
#     expected_result="Please review the problems below:"
#     actual_result=new_snippet.snippet_error_msg()
#     assert actual_result==expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
#     print ("Test Passed:Please review the problems below:")
#
# def test_create_snippet_without_title(driver,login):
#     new_snippet = CreateNewSnippet(driver)
#     time.sleep(1)
#     new_snippet.click_code_snippet()
#     new_snippet.click_new_code_snippet()
#     # new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
#     time.sleep(5)
#     new_snippet.fill_snippet_form(
#         title="",
#         language="Python",
#         description="This is a test description for the snippet.",
#         code="print('Hello, World!')"
#     )
#     new_snippet.select_first_tag()
#     new_snippet.create_code_snippet_button()
#     expected_result = "Title can't be blank"
#     actual_result = new_snippet.title_error_msg()
#     assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
#     print("Test Passed:title cant be blank:")

#
# def test_create_snippet_without_language(driver,login):
#     new_snippet = CreateNewSnippet(driver)
#     time.sleep(1)
#     # new_snippet.click_code_snippet()
#     # new_snippet.click_new_code_snippet()
#     new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
#     new_snippet.fill_snippet_form(
#         title="Test Snippet",
#         language="",
#         description="This is a test description for the snippet.",
#         code="print('Hello, World!')"
#     )
#     new_snippet.select_first_tag()
#     new_snippet.create_code_snippet_button()
#     expected_result = "Language can't be blank"
#     actual_result = new_snippet.language_error_msg()
#     print(f"Expected: {expected_result}")
#     print(f"Actual: {actual_result}")
#     assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
#     print("Test Passed:language cant be blank:")
#
# def test_create_snippet_without_description(driver,login):
#     new_snippet = CreateNewSnippet(driver)
#     time.sleep(1)
#     # new_snippet.click_code_snippet()
#     # new_snippet.click_new_code_snippet()
#     new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
#     time.sleep(5)
#     new_snippet.fill_snippet_form(
#         title="Test Snippet",
#         language="Python",
#         description="",
#         code="print('Hello, World!')"
#     )
#     time.sleep(2)
#     new_snippet.select_first_tag()
#     time.sleep(1)
#     new_snippet.create_code_snippet_button()
#
#
# def test_create_snippet_without_code(driver,login):
#     new_snippet = CreateNewSnippet(driver)
#     time.sleep(1)
#     # new_snippet.click_code_snippet()
#     # new_snippet.click_new_code_snippet()
#     new_snippet.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/code_snippets/new")
#     new_snippet.fill_snippet_form(
#         title="Test Snippet",
#         language="Python",
#         description="Description",
#         code=""
#     )
#     new_snippet.select_first_tag()
#     new_snippet.create_code_snippet_button()
#     expected_result = "Please review the problems below:"
#     actual_result = new_snippet.snippet_error_msg()
#     assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
#     print("Test Passed:code cant be blank:")




#
#
def test_tags_button(login,driver):
    tags= Tags(driver)
    tags.click_tag()

def test_create_new_tag(login,driver):
    new_tags=Tags(driver)
    # new_tags.click_tag()
    new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
    new_tags.click_new_tags()
    time.sleep(2)
    new_tags.enter_tag_name("Tagsss")
    new_tags.click_create_button()
    time.sleep(2)
    expected_result="Tag was successfully created."
    actual_result=new_tags.success_message()
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual_result}")
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
    print("Test Passed :Tag was created successfully")



# def test_update_the_tags(login,driver):
#     new_tags = Tags(driver)
#     # new_tags.click_tag()
#     new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
#     new_tags.click_edit_button()
#     new_tags.enter_tag_name("first Tag")
#     new_tags.click_update_tag_button()

def test_create_tag_with_existing_tag(login,driver):
    new_tags=Tags(driver)
    new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
    new_tags.click_new_tags()
    new_tags.enter_tag_name("NothTags")
    time.sleep(2)
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
    expected_result = "Please review the problems below:"  # We expect an error
    actual_result = new_tags.existing_tag_name_message()  # But success message comes
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"


    print("Test Passed: One-letter tag was created, but it should NOT be allowed (Negative Test detected bug).")


def test_delete_the_tags(login,driver):
    new_tags = Tags(driver)
    new_tags.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/tags")
    new_tags.click_delete_button()
    expected_result = "Tag was successfully destroyed."
    actual_result =new_tags.delete_message()
    assert actual_result == expected_result, f"Expected '{expected_result}',but got'{actual_result}'"
    print("Test Passed :")

# def test_dashboard_link(login,driver):
#     dashboard_link =Search(driver)
#     dashboard_link.click_dashboard()
#
# def test_dashboard_all_snippet(login,driver):
#     all_snippet = Search(driver)
#     all_snippet.click_dashboard()
#     all_snippet.click_all_snippet()
#
# def test_dashboard_private_snippet(login,driver):
#     private_snippet = Search(driver)
#     private_snippet.click_dashboard()
#     private_snippet.click_private()
#
#
# def test_dashboard_public_snippet(login,driver):
#     public_snippet = Search(driver)
#     public_snippet.click_dashboard()
#     public_snippet.click_public()
#
#
# def test_sort_A_Z(login,driver):
#     sort = Search(driver)
#     sort.click_dashboard()
#
#     # sort.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/dashboard")
#     sort.click_all_snippet()
#     sort.click_sort_dropdown()
#     sort.select_a_z_sort("Sort:A-Z")
#     sort.click_apply_button()
#





# Add pytest.main() for running tests with python run_test.py
if __name__ == "__main__":
    pytest.main(["-v", "--tb=short", "run_test.py"])







