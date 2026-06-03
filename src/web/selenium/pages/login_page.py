from typing import Self

from selenium.webdriver.common.by import By

from web.selenium.core.base_page import BasePage
from web.selenium.core.waits import Selector

EMAIL_INPUT = (By.CSS_SELECTOR, "#content-desktop #user_email")
PASSWORD_INPUT = (By.CSS_SELECTOR, "#content-desktop #user_password")
SIGN_IN_BTN = (By.CSS_SELECTOR, "#content-desktop [value='Sign In']")
INVALID_LOGIN_MSG = (By.CSS_SELECTOR, "#content-desktop .common-flash-info")


class LoginPage(BasePage):
    URL = "/users/sign_in"

    def open(self, base_url: str) -> Self:
        super().open(f"{base_url}{self.URL}")
        return self

    def should_be_loaded(self) -> Self:
        self.wait.until_visible(EMAIL_INPUT)
        self.wait.until_visible(PASSWORD_INPUT)
        return self

    def login_user(self, email: str, password: str) -> Self:
        self.find_visible(EMAIL_INPUT).send_keys(email)
        self.find(PASSWORD_INPUT).send_keys(password)
        self.click(SIGN_IN_BTN)
        return self

    def invalid_login_message_visible(self) -> Self:
        self.find_visible(INVALID_LOGIN_MSG)
        return self
