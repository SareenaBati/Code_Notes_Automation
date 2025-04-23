import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocator

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(self.driver,10)

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.EMAIL_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", email_input, email)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD_INPUT)
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", password_input, password)

    def click_remember_me(self):
        remember_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.REMEMBER_ME_CHECKBOX)
        )
        self.driver.execute_script("arguments[0].click();", remember_checkbox)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.LOGIN_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", login_button)

    def get_login_validation_message(self):
        login_validation = self.wait.until(EC.presence_of_element_located(LoginLocator.VALIDATION_LOGIN))
        text = self.driver.execute_script("return arguments[0].textContent", login_validation)
        return text

    def get_email_validation_message(self):
        login_validation = self.wait.until(EC.presence_of_element_located(LoginLocator.EMAIL_VALIDATION))
        text = self.driver.execute_script("return arguments[0].textContent", login_validation)
        return text

    def click_forgot_password(self):
        forgot_password = self.wait.until(EC.presence_of_element_located(LoginLocator.FORGOT_PASSWORD))
        self.driver.execute_script('arguments[0].click()', forgot_password)

    def enter_email_in_forgot_password_field(self, email):
        send_email = self.wait.until(EC.presence_of_element_located(LoginLocator.INPUT_EMAIL_LOGIN))
        self.driver.execute_script("arguments[0].value = arguments[1];", send_email, email)

    def click_reset_instruction_btn(self):
        forgot_password = self.wait.until(EC.presence_of_element_located(LoginLocator.RESET_INSTRUCTION))
        self.driver.execute_script('arguments[0].click()', forgot_password)

    def get_reset_password_validation_error_msg(self):
        reset_validation = self.wait.until(EC.presence_of_element_located(LoginLocator.RESET_VALIDATION))
        text = self.driver.execute_script("return arguments[0].textContent", reset_validation)
        return text

    def get_reset_password_success_msg(self):
        reset_msg = self.wait.until(EC.presence_of_element_located(LoginLocator.VALID_RESET_MESSAGE))
        text = self.driver.execute_script("return arguments[0].textContent", reset_msg)
        return text

    def click_logout_button(self):
        reset_msg = self.wait.until(EC.presence_of_element_located(LoginLocator.LOGOUT_BUTTON))
        text = self.driver.execute_script("return arguments[0].textContent", reset_msg)
        return text
