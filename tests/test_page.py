from pages.login import SauceDemo

def test_valid_login(driver):
    page = SauceDemo(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
