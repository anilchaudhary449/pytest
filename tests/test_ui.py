import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.saucedemo
def test_saucedemo_login(page: Page):
    # Arrange
    # ensure a clean state (clear cookies/localStorage) so the login page shows
    page.context.clear_cookies()
    page.add_init_script("window.localStorage.clear();")
    page.goto("https://www.saucedemo.com/")
    page.locator("id=user-name").fill("standard_user")
    page.locator("id=password").fill("secret_sauce")

    # Assert pre-condition: login button should be visible before clicking
    login_button = page.locator("id=login-button")
    # wait up to 5s for the login button to appear
    expect(login_button).to_be_visible(timeout=5000)

    # Act
    page.locator("id=login-button").click()

    # Assert post-login
    expect(page).to_have_url(re.compile(r".*/inventory\.html$"))
    # after login the login button should no longer be visible
    expect(login_button).not_to_be_visible(timeout=5000)
    expect(page.locator("text=Products")).to_be_visible()
