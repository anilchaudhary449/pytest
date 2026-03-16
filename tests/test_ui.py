import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.saucedemo
def test_saucedemo_login(page: Page):
    # Arrange
    page.goto("https://www.saucedemo.com/")
    page.locator("id=user-name").fill("standard_user")
    page.locator("id=password").fill("secret_sauce")

    # Assert pre-condition: login button should be visible before clicking
    expect(page.locator("id=login-button")).to_be_visible()

    # Act
    page.locator("id=login-button").click()

    # Assert post-login
    expect(page).to_have_url(re.compile(r".*/inventory\.html$"))
    # after login the login button should no longer be visible
    expect(page.locator("id=login-button")).not_to_be_visible()
    expect(page.locator("text=Products")).to_be_visible()
