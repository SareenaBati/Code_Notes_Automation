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
from pages.my_dashboard_page import Search




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

def test_dashboard_link(login,driver):
    dashboard_link =Search(driver)
    dashboard_link.click_dashboard()

def test_dashboard_all_snippet(login,driver):
    all_snippet = Search(driver)
    all_snippet.click_dashboard()
    all_snippet.click_all_snippet()

def test_dashboard_private_snippet(login,driver):
    private_snippet = Search(driver)
    private_snippet.click_dashboard()
    private_snippet.click_private()


def test_dashboard_public_snippet(login,driver):
    public_snippet = Search(driver)
    public_snippet.click_dashboard()
    public_snippet.click_public()


def test_sort_A_Z(login,driver):
    sort = Search(driver)
    sort.click_dashboard()

    # sort.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/dashboard")
    sort.click_all_snippet()
    sort.click_sort_dropdown()
    sort.select_a_z_sort("Sort:A-Z")
    sort.click_apply_button()

def test_sort_oldest(login,driver):
    sort=Search(driver)
    sort.click_dashboard()

    sort.open_page("https://ns-code-snippet-9eae23357ebe.herokuapp.com/dashboard")
