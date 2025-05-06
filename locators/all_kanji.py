from selenium.webdriver.common.by import By

class KANJI:
    ALL_KANJI_LINK=(By.XPATH,'//a[@href="/kanjis"]')
    SEARCH=(By.XPATH,'//input[@id="query"]')
    KANJI_BUTTON = (By.XPATH, "//input[@type='submit']")
    RIVER_KANJI=(By.XPATH,'//a[@href="/kanjis/%E5%B7%9D"]')
    BACK_TO_KANJI_LIST=(By.XPATH,'(//a[@href="/kanjis"]) [2]')