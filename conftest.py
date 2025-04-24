import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Use "new" headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for CI
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues in CI
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")  # Instead of maximize_window

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    yield driver
    driver.quit()
