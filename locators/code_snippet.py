from selenium.webdriver.common.by import By

class SNIPPET:
    SNIPPET_CARDS = (By.CSS_SELECTOR,'div.bg-white.shadow-md.rounded-lg.overflow-hidden.border.border-gray-200')
    SNIPPET_CARDS_TITLE = (By.CSS_SELECTOR,'div.bg-white.shadow-md.rounded-lg div.px-6.py-4 > div.font-bold.text-xl.mb-2')
    VIEW_LINKS = (By.XPATH,'//a[@href="/code_snippets/4"]')
    EDIT_LINKS = (By.XPATH,'//a[contains(text(),"Edit")]')
    DELETE_LINKS = (By.XPATH,"//input[@type='submit' and @name='commit' and @value='Delete']")
    SNIPPET_CREATOR = (By.CSS_SELECTOR,'span.text-gray-500.text-xs')
    CUSTOM_TAGS = (By.CSS_SELECTOR,'a.bg-blue-100.rounded-full.text-blue-700')
    ERROR_MESSAGE_EDIT_WITHOUT_SIGNIN=(By.XPATH,'//span[@class="block sm:inline"]')
    ERROR_MESSAGE_DELETE_WITHOUT_SIGNIN = (By.XPATH, '//span[@class="block sm:inline"]')