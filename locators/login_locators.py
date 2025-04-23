from selenium.webdriver.common.by import By

# Login page locators
class LoginLocator:
    EMAIL_INPUT = (By.XPATH, "//input[@id='user_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='user_password']")
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//input[@id='user_remember_me']")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a[href="/users/password/new"')
    SIGN_IN_BTN = (By.XPATH, '//input[@type="submit" and @name="commit" and @value="Sign in"]')
    SIGN_UP_LINK = (By.XPATH, '//a[contains(text(),"Sign up")]')
    VALIDATION_LOGIN = (By.XPATH,'//span[@class="block sm:inline"]')
    EMAIL_VALIDATION=(By.XPATH,"//div[@role='alert']")
    RESET_INSTRUCTION = (By.XPATH, '//input[@data-disable-with]')
    RESET_VALIDATION = (By.XPATH, '//input[@id="user_email"]/following-sibling::p[1]')
    VALID_RESET_MESSAGE = (By.XPATH, '//input[@id="user_email"]/following-sibling::p[1]')
    LOGOUT_BUTTON=(By.XPATH, "//a[@href='/users/sign_out']")
