from __future__ import annotations

from playwright.sync_api import Page, expect


class AccountsPage:
    def __init__(self, page: Page):
        self.page = page

    def assert_loaded(self) -> None:
        expect(self.page.get_by_role("heading", name="Accounts Overview")).to_be_visible()
        expect(self.page.get_by_role("link", name="Log Out")).to_be_visible()

    def open_transfer(self):
        from pages.transfer_page import TransferPage
        self.page.get_by_role("link", name="Transfer Funds").first.click()
        return TransferPage(self.page)

    def open_open_account(self):
        from pages.customer_pages import OpenAccountPage
        return OpenAccountPage(self.page).open()

    def open_bill_pay(self):
        from pages.customer_pages import BillPayPage
        return BillPayPage(self.page).open()

    def open_find_transactions(self):
        from pages.customer_pages import FindTransactionsPage
        return FindTransactionsPage(self.page).open()

    def open_profile(self):
        from pages.customer_pages import ProfilePage
        return ProfilePage(self.page).open()

    def open_loan(self):
        from pages.customer_pages import LoanPage
        return LoanPage(self.page).open()

    def logout(self):
        from pages.login_page import LoginPage
        self.page.get_by_role("link", name="Log Out").click()
        return LoginPage(self.page, self.page.url.split("/parabank")[0] + "/parabank")
