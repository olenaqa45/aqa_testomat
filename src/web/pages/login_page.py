from typing import Self

from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self._container = page.locator("#content-desktop")

        # Locators
        self.form = self._container.locator("form#new_user")
        self.email_input = self._container.locator("#user_email")
        self.password_input = self._container.locator("#user_password")
        self.sign_in_btn = self._container.get_by_role("button", name="Sign in")
        self.remember_me = self._container.locator("#user_remember_me")
        self.google_btn = self._container.locator('a[href="/users/auth/google_oauth2"]')
        self.github_btn = self._container.locator('a[href="/users/auth/github"]')
        self.sso_btn = self._container.locator('a[href="/users/sso"]')
        self.sign_up_link = self._container.locator('a[href="/users/sign_up"]')
        self.forgot_password_link = self._container.locator('a[href="/users/password/new"]')
        self.invalid_login_msg = self._container.get_by_text("Invalid email or password.")

    def open(self) -> Self:
        self.page.goto("/users/sign_in")
        return self

    def should_be_loaded(self) -> Self:
        expect(self.form).to_be_visible()
        return self

    def login_user(self, email: str, password: str) -> Self:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.sign_in_btn.click()
        return self

    def login_with_google(self) -> Self:
        self.google_btn.click()
        return self

    def login_with_github(self) -> Self:
        self.github_btn.click()
        return self

    def login_with_sso(self) -> Self:
        self.sso_btn.click()
        return self

    def click_sign_up(self) -> Self:
        self.sign_up_link.click()
        return self

    def click_forgot_password(self) -> Self:
        self.forgot_password_link.click()
        return self

    def set_remember_me(self, checked: bool = True) -> Self:
        self.remember_me.set_checked(checked)
        return self

    def invalid_login_message_visible(self) -> Self:
        expect(self.invalid_login_msg).to_be_visible()
        return self
