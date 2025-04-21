from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def open_sign_up_page(self, url):
        self.driver.get(url)

    def click_sign_up_button(self):
        sign_up_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign Up']"))
        )
        self.driver.execute_script("arguments[0].click();", sign_up_element)

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user_email']"))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", email_input, email)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user_password']"))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", password_input, password)

    def enter_confirm_password(self, confirm_password):
        confirm_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user_password_confirmation']"))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", confirm_input, confirm_password)

    def click_sign_up(self):
        sign_up_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='submit']"))
        )
        self.driver.execute_script("arguments[0].click();", sign_up_button)
