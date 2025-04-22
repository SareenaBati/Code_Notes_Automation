from selenium.webdriver.common.by import By

# Login page locators
class LoginLocator:
    EMAIL_INPUT = (By.XPATH, "//input[@id='user_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='user_password']")
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//input[@id='user_remember_me']")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")
