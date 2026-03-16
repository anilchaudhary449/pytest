from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemo:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        # Use the driver passed into the page object (do not create a new Chrome here).
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()


    def login(self, username, password):
        self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def get_error_message(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        ).text