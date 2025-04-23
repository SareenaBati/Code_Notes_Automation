from selenium.webdriver.common.by import By

class SignUpLocators:
    SIGN_UP_LINK = (By.XPATH, "//a[normalize-space()='Sign Up']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='user_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='user_password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@id='user_password_confirmation']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    VALIDATION = (By.CSS_SELECTOR, 'div.bg-red-100.border.border-red-400.text-red-700')
    VALIDATION_ERROR_MESSAGE = (By.CSS_SELECTOR,'p.mt-2.text-red-500.text-sm')
    SUCCESSFUL_SIGNUP_MESSAGE = (By.CSS_SELECTOR, 'span.block.sm\\:inline')
    EMPTY_PASSWORD = (By.XPATH, '//p[normalize-space()="Password can\'t be blank"]')
    MISMATCHED_PASSWORD=(By.XPATH,"(//p[@class='mt-2 text-red-500 text-sm'])[2]")
    LOG_OUT = (By.XPATH,'//a[contains(text(),"Logout")]')