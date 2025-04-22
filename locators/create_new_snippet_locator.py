from selenium.webdriver.common.by import  By

class CreateNewSnippetLocators:
    NEW_CODE_SNIPPET = (By.XPATH, '//a[@href="/code_snippets/new"]')
    INPUT_TITLE = (By.XPATH,'//input[@type="text"]')
    LANGUAGE = (By.XPATH, "//label[@for='code_snippet_language']")
    INPUT_LANGUAGE=(By.XPATH,"//select[@id='code_snippet_language']")
    INPUT_DESCRIPTION = (By.XPATH,"//textarea[@id='code_snippet_description']")
    INPUT_CODE = (By.XPATH, "//textarea[@id='code_snippet_code']")
    INPUT_PRIVATE = (By.XPATH, "//input[@id='code_snippet_private']")
    INPUT_TAGS = (By.XPATH, '//input[@type="checkbox" and @name="code_snippet[tag_ids][]"]/following-sibling::label')
    CREATE_BTN = (By.XPATH, '//input[@type="submit" and @name="commit"]')
    MANAGE_TAG_LINK = (By.XPATH, '//a[contains(text(),"Manage Tags")]')
