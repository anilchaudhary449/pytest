import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Creates a Chrome WebDriver instance. Ensure chromedriver is installed and on PATH.
    driver = webdriver.Firefox()  # You can switch to webdriver.Chrome() if you prefer Chrome
    yield driver
    try:
        driver.quit()
    except Exception:
        pass
