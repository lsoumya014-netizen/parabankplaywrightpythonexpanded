from __future__ import annotations

from typing import Mapping
from playwright.sync_api import Page, expect


class OpenAccountPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> "OpenAccountPage":
        self.page.get_by_role("link", name="Open New Account").click()
        expect(self.page.get_by_role("heading", name="Open New Account")).to_be_visible()
        return self

    def fill_details(self, account_type: str = "CHECKING") -> None:
        self.page.locator("#type").select_option(label=account_type)
        self.page.locator("#fromAccountId").select_option(index=0)
        expect(self.page.locator("#type")).to_have_value("0")


class BillPayPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> "BillPayPage":
        self.page.get_by_role("link", name="Bill Pay").click()
        expect(self.page.get_by_role("heading", name="Bill Payment Service")).to_be_visible()
        return self

    def fill_details(self, data: Mapping[str, str]) -> None:
        fields = {
            "payee.name": data["payee_name"],
            "payee.address.street": data["street"],
            "payee.address.city": data["city"],
            "payee.address.state": data["state"],
            "payee.address.zipCode": data["zip_code"],
            "payee.accountNumber": data["account_number"],
            "verifyAccount": data["verify_account"],
            "amount": data["amount"],
        }
        for name, value in fields.items():
            locator = self.page.locator(f'input[name="{name}"]')
            locator.fill(value)
            expect(locator).to_have_value(value)
        payee_form = self.page.locator('input[name="payee.name"]').locator("xpath=ancestor::form")
        phone_field = payee_form.locator("input").nth(5)
        phone_field.fill(data["phone"])
        expect(phone_field).to_have_value(data["phone"])
        self.page.locator("select[name=fromAccountId]").select_option(index=0)


class FindTransactionsPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> "FindTransactionsPage":
        self.page.get_by_role("link", name="Find Transactions").click()
        expect(self.page.get_by_role("heading", name="Find Transactions")).to_be_visible()
        return self

    def fill_details(self, data: Mapping[str, str]) -> None:
        self.page.locator("#accountId").select_option(index=0)
        values = {
            "transactionId": data["transaction_id"],
            "transactionDate": data["transaction_date"],
            "fromDate": data["from_date"],
            "toDate": data["to_date"],
            "amount": data["amount"],
        }
        for field_id, value in values.items():
            locator = self.page.locator(f"#{field_id}")
            locator.fill(value)
            expect(locator).to_have_value(value)


class ProfilePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> "ProfilePage":
        self.page.get_by_role("link", name="Update Contact Info").click()
        expect(self.page.get_by_role("heading", name="Update Profile")).to_be_visible()
        return self

    def fill_details(self, data: Mapping[str, str]) -> None:
        fields = {
            "customer.firstName": data["first_name"],
            "customer.lastName": data["last_name"],
            "customer.address.street": data["address"],
            "customer.address.city": data["city"],
            "customer.address.state": data["state"],
            "customer.address.zipCode": data["zip_code"],
            "customer.phoneNumber": data["phone"],
        }
        for name, value in fields.items():
            locator = self.page.locator(f'input[name="{name}"]')
            locator.fill(value)
            expect(locator).to_have_value(value)


class LoanPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> "LoanPage":
        self.page.get_by_role("link", name="Request Loan").click()
        expect(self.page.get_by_role("heading", name="Apply for a Loan")).to_be_visible()
        return self

    def fill_details(self, data: Mapping[str, str]) -> None:
        for field_id, value in {"amount": data["amount"], "downPayment": data["down_payment"]}.items():
            locator = self.page.locator(f"#{field_id}")
            locator.fill(value)
            expect(locator).to_have_value(value)
        self.page.locator("#fromAccountId").select_option(index=0)
