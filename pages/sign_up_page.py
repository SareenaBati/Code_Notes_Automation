from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def open_sign_up_page(self, url):
        self.driver.get(url)

    def click_sign_up_button(self):
        sign_up_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign Up']"))
        )
        sign_up_element.click()

    def enter_email(self, email):
        email_address_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='user_email']"))
        )
        email_address_input.send_keys(email)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='user_password']"))
        )
        password_input.send_keys(password)

    def enter_confirm_password(self, confirm_password):

        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='user_password_confirmation']"))
        )
        confirm_password_input.send_keys(confirm_password)

    def click_sign_up(self):

        sign_up_button_click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        )
        sign_up_button_click.click()
