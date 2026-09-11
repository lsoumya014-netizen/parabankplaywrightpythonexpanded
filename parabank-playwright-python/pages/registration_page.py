from __future__ import annotations

from typing import Mapping
from playwright.sync_api import Page, expect


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self) -> "RegistrationPage":
        self.page.get_by_role("link", name="Register").click()
        expect(self.page.locator("#customerForm")).to_be_visible()
        return self

    def fill_all_details(self, data: Mapping[str, str]) -> None:
        fields = {
            "customer.firstName": data["first_name"],
            "customer.lastName": data["last_name"],
            "customer.address.street": data["address"],
            "customer.address.city": data["city"],
            "customer.address.state": data["state"],
            "customer.address.zipCode": data["zip_code"],
            "customer.phoneNumber": data["phone"],
            "customer.ssn": data["ssn"],
            "customer.username": data["username"],
            "customer.password": data["password"],
            "repeatedPassword": data["confirm_password"],
        }
        for name, value in fields.items():
            locator = self.page.locator(f'input[name="{name}"]')
            locator.fill(value)
            expect(locator).to_have_value(value)

    def submit(self) -> None:
        self.page.locator('input[type="submit"][value="Register"]').click()
