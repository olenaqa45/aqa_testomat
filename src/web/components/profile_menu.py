from typing import Self

from playwright.sync_api import Page


class ProfileMenu:
    def __init__(self, page: Page):
        self.page = page
        self._container = page.locator("#content-desktop .auth-header-nav-right")
        self._menu = page.locator("#profile-menu")

        # Locators
        self.toggle_btn = self._container.locator("#toggle-profile-menu")
        self.companies_link = self._menu.locator('a[href="/companies"]')
        self.account_link = self._menu.locator('a[href="/account"]')
        self.downloads_link = self._menu.locator('a[href="/account/files"]')
        self.sign_out_btn = self._menu.locator('button[type="submit"]')
        self.email_label = self._menu.locator(".auth-header-nav-right-dropdown-menu-block-email")

    def open(self) -> Self:
        self.toggle_btn.click()
        return self

    def click_my_companies(self) -> Self:
        self.open()
        self.companies_link.click()
        return self

    def click_account(self) -> Self:
        self.open()
        self.account_link.click()
        return self

    def click_downloads(self) -> Self:
        self.open()
        self.downloads_link.click()
        return self

    def sign_out(self) -> Self:
        self.open()
        self.sign_out_btn.click()
        return self

    def get_email(self) -> str:
        self.open()
        return self.email_label.inner_text()
