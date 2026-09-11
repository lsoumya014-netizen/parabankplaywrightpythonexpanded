from playwright.sync_api import Page
import pytest

from conftest import save_screenshot
from pages.login_page import LoginPage


def logged_in_accounts(page: Page, base_url: str, test_data: dict):
    return LoginPage(page, base_url).open().login(
        test_data["login"]["username"], test_data["login"]["password"]
    )


@pytest.mark.regression
def test_open_new_account_form_is_filled(page: Page, base_url: str, test_data: dict) -> None:
    accounts = logged_in_accounts(page, base_url, test_data)
    account_page = accounts.open_open_account()
    account_page.fill_details("CHECKING")
    save_screenshot(page, "open_new_account_filled")


@pytest.mark.regression
def test_bill_pay_form_is_filled(page: Page, base_url: str, test_data: dict) -> None:
    accounts = logged_in_accounts(page, base_url, test_data)
    bill_pay = accounts.open_bill_pay()
    bill_pay.fill_details(test_data["bill_pay"])
    save_screenshot(page, "bill_pay_all_details_filled")


@pytest.mark.regression
def test_find_transactions_form_is_filled(page: Page, base_url: str, test_data: dict) -> None:
    accounts = logged_in_accounts(page, base_url, test_data)
    transactions = accounts.open_find_transactions()
    transactions.fill_details(test_data["find_transactions"])
    save_screenshot(page, "find_transactions_all_details_filled")


@pytest.mark.regression
def test_update_profile_form_is_filled(page: Page, base_url: str, test_data: dict) -> None:
    accounts = logged_in_accounts(page, base_url, test_data)
    profile = accounts.open_profile()
    profile.fill_details(test_data["profile"])
    save_screenshot(page, "update_profile_all_details_filled")


@pytest.mark.regression
def test_request_loan_form_is_filled(page: Page, base_url: str, test_data: dict) -> None:
    accounts = logged_in_accounts(page, base_url, test_data)
    loan = accounts.open_loan()
    loan.fill_details(test_data["loan"])
    save_screenshot(page, "request_loan_all_details_filled")
