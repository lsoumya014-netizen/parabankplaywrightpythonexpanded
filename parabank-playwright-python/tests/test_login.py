from playwright.sync_api import Page, expect
import pytest

from conftest import save_screenshot
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_page_can_fill_valid_credentials(page: Page, base_url: str, test_data: dict) -> None:
    login = LoginPage(page, base_url).open()
    login.fill_login(test_data["login"]["username"], test_data["login"]["password"])
    save_screenshot(page, "login_valid_credentials_filled")
    accounts = login.login(test_data["login"]["username"], test_data["login"]["password"])
    accounts.assert_loaded()
    expect(page.get_by_text("Welcome John Smith")).to_be_visible()
    save_screenshot(page, "login_success_accounts_overview")


@pytest.mark.smoke
def test_invalid_login_shows_error(page: Page, base_url: str, test_data: dict) -> None:
    login = LoginPage(page, base_url).open()
    login.fill_login(test_data["invalid_login"]["username"], test_data["invalid_login"]["password"])
    save_screenshot(page, "login_invalid_credentials_filled")
    login.login(test_data["invalid_login"]["username"], test_data["invalid_login"]["password"])
    login.assert_invalid_login()
    save_screenshot(page, "login_invalid_error")
