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

    def open(self):
        self.page.goto("/users/sign_in")

    def is_loaded(self):
        expect(self.form).to_be_visible()

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.sign_in_btn.click()

    def login_with_google(self):
        self.google_btn.click()

    def login_with_github(self):
        self.github_btn.click()

    def login_with_sso(self):
        self.sso_btn.click()

    def click_sign_up(self):
        self.sign_up_link.click()

    def click_forgot_password(self):
        self.forgot_password_link.click()

    def set_remember_me(self, checked: bool = True):
        self.remember_me.set_checked(checked)

    def invalid_login_message_visible(self):
        expect(self.invalid_login_msg).to_be_visible()
