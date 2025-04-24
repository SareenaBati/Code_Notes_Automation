from selenium.webdriver.common.by import  By

class CreateNewSnippetLocators:
    CODE_SNIPPET=(By.XPATH,'//a[text()="Code Snippets"]')
    NEW_CODE_SNIPPET = (By.XPATH, '(//a[contains(@class, "bg-blue-600") and @href="/code_snippets/new"])[1]')
    INPUT_TITLE = (By.XPATH,'//input[@type="text"]')
    LANGUAGE = (By.XPATH, "//label[@for='code_snippet_language']")
    INPUT_LANGUAGE=(By.XPATH,"//select[@id='code_snippet_language']")
    INPUT_DESCRIPTION = (By.XPATH,"//textarea[@id='code_snippet_description']")
    INPUT_CODE = (By.XPATH, "//textarea[@id='code_snippet_code']")
    PRIVATE_CHECKBOX = (By.ID, "code_snippet_private")
    INPUT_TAGS = (By.XPATH, '//input[@type="checkbox" and @name="code_snippet[tag_ids][]"]/following-sibling::label')
    CREATE_BTN = (By.XPATH, "//input[@name='commit']")
    SUCCESSFUL_MESSAGE=(By.XPATH, "//div[@role='alert']/p")
    ERROR_MESSAGE=(By.XPATH,'//div[@class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4"]')
    TITLE_ERROR_MESSAGE=(By.XPATH,' (//p[@class="mt-2 text-red-500 text-sm"])[1]')
    LANGUAGE_BLANK_ERROR_MESSAGE=(By.XPATH,' (//p[@class="mt-2 text-red-500 text-sm"])[2]')
    CODE_BLANK_ERROR_MESSAGE=(By.XPATH,' (//p[@class="mt-2 text-red-500 text-sm"])[3]')
    MANAGE_TAG_LINK = (By.XPATH, '//a[contains(text(),"Manage Tags")]')
