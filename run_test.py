import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from Code_Notes_Automation.pages.main_page import MainPage

@pytest.fixture()
def driver():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager.install()))
    driver.implicitly_wait()
    yield driver
    driver.quit()


def test_main_page(driver):
    main_page=MainPage(driver)
    main_page.open_page("hhttps://ns-code-snippet-9eae23357ebe.herokuapp.com/")
    driver.maximize_window()
    time.sleep(5)