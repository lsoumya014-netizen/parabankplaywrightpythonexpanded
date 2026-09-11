from playwright.sync_api import Page, expect
import pytest

from conftest import save_screenshot
from pages.login_page import LoginPage


@pytest.mark.regression
def test_accounts_overview_loads_after_login(page: Page, base_url: str, test_data: dict) -> None:
    accounts = LoginPage(page, base_url).open().login(
        test_data["login"]["username"], test_data["login"]["password"]
    )
    accounts.assert_loaded()
    expect(page.locator("#accountTable")).to_be_visible()
    save_screenshot(page, "accounts_overview_filled_authenticated")
