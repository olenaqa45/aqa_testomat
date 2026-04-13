from playwright.sync_api import Page, expect

#AI generated
class ProfileMenu:

    def __init__(self, page: Page):
        self.page = page
        self._container = page.locator("#content-desktop .auth-header-nav-right")

    def open(self):
        self._container.locator("#toggle-profile-menu").click()

    def click_my_companies(self):
        self.open()
        self.page.locator('#profile-menu a[href="/companies"]').click()

    def click_account(self):
        self.open()
        self.page.locator('#profile-menu a[href="/account"]').click()

    def click_downloads(self):
        self.open()
        self.page.locator('#profile-menu a[href="/account/files"]').click()

    def sign_out(self):
        self.open()
        self.page.locator('#profile-menu button[type="submit"]').click()

    def get_email(self) -> str:
        self.open()
        return self.page.locator("#profile-menu .auth-header-nav-right-dropdown-menu-block-email").inner_text()
