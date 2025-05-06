from selenium.webdriver.common.by import  By

class KANJI:
    KANJI_FOR_BEGINNERS_BUTTON=(By.XPATH,'(//a[@class="hover:text-blue-200"])[4]')
    SEARCH_KANJI=(By.XPATH,"//input[@id='query']")
    KANJI_BUTTON=(By.XPATH,"//input[@type='submit']")
    ERROR_MESSAGE=(By.XPATH,'//div[@class="bg-red-100 border-red-400 text-red-700 px-4 py-3 rounded relative border mb-4"]')
    ERROR_MESSAGE_WITH_EMPTY_INPUT=(By.XPATH,'//div[@class="bg-red-100 border-red-400 text-red-700 px-4 py-3 rounded relative border mb-4"]')