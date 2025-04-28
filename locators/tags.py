from selenium.webdriver.common.by import  By

class TagsLocator:
    TAGS_BUTTON=(By.XPATH,"//a[normalize-space()='Tags']")
    NEW_TAG_BUTTON=(By.XPATH,'//a[@href="/tags/new"]')
    TAG_NAME=(By.XPATH,'//input[@name="tag[name]"]')
    CREATE_BUTTON=(By.XPATH,'//input[@name="commit"]')
    SUCCESS_MESSAGE=(By.XPATH,"//p[contains(text(),'Tag was successfully created.')]")
    EDIT_BUTTON=(By.XPATH,'//a[@href="/tags/21/edit"]')
    UPDATE_TAG_BUTTON=(By.XPATH,'//input[@type="submit"]')
    EDIT_MESSAGE=(By.XPATH,'//span[@class="block sm:inline"]')
    REPEAT_TAG_NAME=(By.XPATH,'//div[@class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4"]')
    DELETE_BUTTON=(By.XPATH,'(//input[@name="commit"])[2]')
    DELETE_MESSAGE = (By.XPATH, "//p[contains(text(), 'Tag was successfully destroyed')]")


