from selenium.webdriver.common.by import By

class SignUpLocators:
    SIGN_UP_LINK = (By.XPATH, "//a[normalize-space()='Sign Up']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='user_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='user_password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@id='user_password_confirmation']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
