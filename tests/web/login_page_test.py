from faker import Faker
from playwright.sync_api import Page, expect

from tests.conftest import Config
from web.pages.HomePage import HomePage
from web.pages.LoginPage import LoginPage
from web.pages.ProjectsPage import ProjectsPage


def test_login_invalid(page: Page, configs: Config):
    home_page = HomePage(page)
    home_page.open()
    home_page.is_loaded()
    home_page.click_login()

    login_page = LoginPage(page)
    login_page.is_loaded()
    login_page.login(configs.email, Faker().password(length=10))
    login_page.invalid_login_message_visible()


def test_login_with_valid_credentials(page: Page, configs: Config):
    home_page = HomePage(page)
    home_page.open()
    home_page.is_loaded()
    home_page.click_login()

    login_page = LoginPage(page)
    login_page.is_loaded()
    login_page.login(configs.email, configs.password)

    ProjectsPage(page).is_loaded()


def test_login_page_is_loaded(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.is_loaded()

# AI Generated
def test_forgot_password_link(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.is_loaded()
    login_page.click_forgot_password()
    expect(page).to_have_url("/users/password/new", timeout=5000)


def test_sign_up_link(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.is_loaded()
    login_page.click_sign_up()
    expect(page).to_have_url("/users/sign_up", timeout=5000)


def test_remember_me_checkbox(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.is_loaded()
    login_page.set_remember_me(True)
    expect(page.locator("#content-desktop #user_remember_me")).to_be_checked()


def test_google_login_redirect(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.is_loaded()
    login_page.login_with_google()
    expect(page).not_to_have_url("/users/sign_in", timeout=5000)


def test_github_login_redirect(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.is_loaded()
    login_page.login_with_github()
    expect(page).not_to_have_url("/users/sign_in", timeout=5000)
