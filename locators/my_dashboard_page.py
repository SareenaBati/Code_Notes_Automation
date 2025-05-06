from selenium.webdriver.common.by import By

class SEARCH:
    DASHBOARD=(By.XPATH,'//a[@href="/dashboard"]')
    ALL_SNIPPET=(By.XPATH,'//a[@href="/dashboard?tab=all"]')
    PUBLIC_SNIPPET=(By.XPATH,'//a[@href="/dashboard?tab=public"]')
    PRIVATE_SNIPPET=(By.XPATH,'//a[@href="/dashboard?tab=private"]')
    SORT=(By.XPATH,'//select [@id="sort"]')
    A_Z_SORT=(By.XPATH,'//option[@value="a-z"]')
    NEWEST_SORT=(By.XPATH,'//option[@value="newest"]')
    OLDEST_SORT=(By.XPATH,'//option[@value="oldest"]')
    APPLY_BUTTON=(By.XPATH,'//input[@value="Apply"]')
    SEARCH_BOX=(By.XPATH,'//input[@type="text"]')
    LANGUAGE=(By.XPATH,'//select [@id="language"]')
    ALL_LANGUAGES=(By.XPATH,'//option[@value="all"]')
    PYTHON=(By.XPATH,'//option[@value="Python"]')
    RUBY=(By.XPATH,'//option[@value="Ruby"]')
    SQL=(By.XPATH,'//option[@value="SQL"]')
