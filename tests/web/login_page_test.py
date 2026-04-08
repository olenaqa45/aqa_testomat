from faker import Faker
from playwright.sync_api import Page

from tests.conftest import Config
from web.pages.HomePage import HomePage
from web.pages.LoginPage import LoginPage


def test_login_invalid(page: Page, configs:Config):
    home_page = HomePage(page)
    home_page.open()
    home_page.is_loaded()
    home_page.click_login()

    login_page = LoginPage(page)
    login_page.is_loaded()
    login_page.login(configs.email, Faker().password(length=10))
    login_page.invalid_login_message_visible()
