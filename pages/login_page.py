import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocator

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.EMAIL_INPUT)  # Correct reference to locator
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", email_input, email)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD_INPUT)  # Correct reference to locator
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", password_input, password)

    def click_remember_me(self):
        remember_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.REMEMBER_ME_CHECKBOX)  # Correct reference to locator
        )
        self.driver.execute_script("arguments[0].click();", remember_checkbox)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.LOGIN_BUTTON)  # Correct reference to locator
        )
        self.driver.execute_script("arguments[0].click();", login_button)
