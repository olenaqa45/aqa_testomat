from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("/users/sign_in")

    def is_loaded(self):
        expect(self.page.locator("#content-desktop form#new_user")).to_be_visible()

    def login(self, email: str, password: str):
        self.page.locator("#content-desktop #user_email").fill(email)
        self.page.locator("#content-desktop #user_password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()

    def login_with_google(self):
        self.page.locator('#content-desktop a[href="/users/auth/google_oauth2"]').click()

    def login_with_github(self):
        self.page.locator('#content-desktop a[href="/users/auth/github"]').click()

    def login_with_sso(self):
        self.page.locator('#content-desktop a[href="/users/sso"]').click()

    def click_sign_up(self):
        self.page.locator('#content-desktop a[href="/users/sign_up"]').click()

    def click_forgot_password(self):
        self.page.locator('#content-desktop a[href="/users/password/new"]').click()

    def set_remember_me(self, checked: bool = True):
        self.page.locator("#content-desktop #user_remember_me").set_checked(checked)

    def invalid_login_message_visible(self):
        expect(self.page.locator("#content-desktop").get_by_text("Invalid email or password.")).to_be_visible()
