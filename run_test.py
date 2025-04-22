import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sign_up_page import SignUp
from pages.create_new_snippet import CreateNewSnippet
from pages.code_snippet import CodeSnippet

@pytest.fixture(scope="module")

def driver():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)  # Uses implicit wait globally
    yield driver
    driver.quit()


def test_main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")


def test_sign_up_page(driver):
    sign_up_page = SignUp(driver)
    sign_up_page.open_sign_up_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com")
    sign_up_page.click_sign_up_button()
    time.sleep(2)
    sign_up_page.enter_email("sareena.bati@gmail.com")
    time.sleep(2)
    sign_up_page.enter_password("test")
    time.sleep(2)
    sign_up_page.enter_confirm_password("test")
    time.sleep(2)
    sign_up_page.click_sign_up()
    time.sleep(2)


def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/users/sign_in")
    login_page.enter_email("sareena.bati@gmail.com")
    time.sleep(1)
    login_page.enter_password("test")
    time.sleep(1)
    login_page.click_remember_me()
    time.sleep(1)
    login_page.click_login()
    time.sleep(5)



@pytest.fixture(scope="module")
def login(driver):
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/users/sign_in")
    login_page.enter_email("sareena.bati@gmail.com")
    login_page.enter_password("Sarinagmail@9#")
    login_page.click_remember_me()
    login_page.click_login()
    time.sleep(2)
    return driver

def test_create_new_snippet(login,driver):
    create_new_snippet = CreateNewSnippet(driver)

    create_new_snippet.click_new_code_snippet()
    create_new_snippet.fill_snippet_form(
        title="Test Snippet",
        language="Python",
        description="This is a test description for the snippet.",
        code="print('Hello, World!')"
    )
    create_new_snippet.select_private()
    time.sleep(1)
    create_new_snippet.select_first_tag()
    time.sleep(1)
    create_new_snippet.submit_form()
    time.sleep(1)


def test_code_snippet(login,driver):
    code_snippet= CodeSnippet(driver)
    code_snippet.click_third_code_snippet()








