import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.sign_up_locators import SignUpLocators

class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def open_sign_up_page(self, url):
        self.driver.get(url)

    def click_sign_up_button(self):
        sign_up_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignUpLocators.SIGN_UP_LINK)
        )
        self.driver.execute_script("arguments[0].click();", sign_up_element)

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignUpLocators.EMAIL_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", email_input, email)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignUpLocators.PASSWORD_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", password_input, password)

    def enter_confirm_password(self, confirm_password):
        confirm_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignUpLocators.CONFIRM_PASSWORD_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", confirm_input, confirm_password)

    def click_sign_up(self):
        sign_up_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignUpLocators.SUBMIT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", sign_up_button)
