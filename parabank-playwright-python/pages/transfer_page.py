from __future__ import annotations

from typing import Mapping
from playwright.sync_api import Page, expect


class TransferPage:
    def __init__(self, page: Page):
        self.page = page
        self.amount = page.locator("#amount")
        self.from_account = page.locator("#fromAccountId")
        self.to_account = page.locator("#toAccountId")

    def assert_loaded(self) -> None:
        expect(self.page.get_by_role("heading", name="Transfer Funds")).to_be_visible()
        expect(self.amount).to_be_visible()
        expect(self.from_account).to_be_visible()
        expect(self.to_account).to_be_visible()

    def fill_transfer_details(self, data: Mapping[str, str]) -> None:
        self.amount.fill(data["amount"])
        expect(self.amount).to_have_value(data["amount"])
        # Selecting the first available account makes the test independent of
        # the account number assigned to the seeded demo user.
        self.from_account.select_option(index=0)
        self.to_account.select_option(index=0)
        expect(self.from_account).to_have_value(self.from_account.locator("option").first.get_attribute("value"))
        expect(self.to_account).to_have_value(self.to_account.locator("option").first.get_attribute("value"))
