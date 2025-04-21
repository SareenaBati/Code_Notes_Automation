import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sign_up_page import SignUp


from selenium import webdriver




@pytest.fixture()
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
    sign_up_page.enter_email("sareena.bati@gmail.com")
    sign_up_page.enter_password("test")
    sign_up_page.enter_confirm_password("test")
    sign_up_page.click_sign_up()


def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/users/sign_in")
    login_page.enter_email("sareena.bati@gmail.com")
    login_page.enter_password("test")
    login_page.click_remember_me()
    login_page.click_login()
