from playwright.sync_api import Page
import pytest

from conftest import save_screenshot
from pages.login_page import LoginPage


@pytest.mark.regression
def test_transfer_form_is_filled_from_json(page: Page, base_url: str, test_data: dict) -> None:
    accounts = LoginPage(page, base_url).open().login(
        test_data["login"]["username"], test_data["login"]["password"]
    )
    transfer = accounts.open_transfer()
    transfer.assert_loaded()
    transfer.fill_transfer_details(test_data["transfer"])
    save_screenshot(page, "transfer_all_details_filled")
