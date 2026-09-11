from __future__ import annotations

import re
from playwright.sync_api import Page, expect

from pages.accounts_page import AccountsPage


class LoginPage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.username = page.locator('input[name="username"]')
        self.password = page.locator('input[name="password"]')
        self.login_button = page.locator('input[type="submit"][value="Log In"]')

    def open(self) -> "LoginPage":
        self.page.goto(f"{self.base_url}/index.htm")
        expect(self.page.get_by_role("heading", name="Customer Login")).to_be_visible()
        return self

    def fill_login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        expect(self.username).to_have_value(username)
        expect(self.password).to_have_value(password)

    def login(self, username: str, password: str) -> AccountsPage:
        self.fill_login(username, password)
        self.login_button.click()
        return AccountsPage(self.page)

    def assert_invalid_login(self) -> None:
        expect(self.page.locator("#rightPanel")).to_contain_text(
            re.compile("error|could not be verified", re.IGNORECASE)
        )
