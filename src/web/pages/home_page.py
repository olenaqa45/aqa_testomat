from typing import Self

from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page, base_url: str = "https://testomat.io"):
        self.page = page
        self._base_url = base_url

    def open(self) -> Self:
        self.page.goto(self._base_url)
        return self

    def should_be_loaded(self) -> Self:
        expect(self.page.locator("#headerMenuWrapper")).to_be_visible()
        expect(self.page.locator(".side-menu .login-item")).to_have_text("Log in")
        expect(self.page.locator(".side-menu .start-item")).to_have_text("Start for free")
        return self

    def click_login(self) -> Self:
        self.page.get_by_text("Log in", exact=True).click()
        return self
