from playwright.sync_api import Page, expect
import pytest

from conftest import save_screenshot
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.mark.smoke
def test_registration_form_is_filled_from_json(page: Page, base_url: str, test_data: dict) -> None:
    login = LoginPage(page, base_url).open()
    registration = RegistrationPage(page).open()
    registration.fill_all_details(test_data["registration"])
    # ParaBank has no email field; the JSON keeps email as test data for
    # systems that extend the form, while all fields actually present are filled.
    expect(page.locator("#customerForm")).to_be_visible()
    save_screenshot(page, "registration_all_details_filled")
