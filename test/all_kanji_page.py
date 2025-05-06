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