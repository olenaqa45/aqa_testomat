import pytest
from faker import Faker
from playwright.sync_api import expect

from tests.conftest import Config
from web.App import App


@pytest.mark.regression
def test_login_invalid(app: App, configs: Config):
    app.home_page.open()
    app.home_page.is_loaded()
    app.home_page.click_login()

    app.login_page.is_loaded()
    app.login_page.login(configs.email, Faker().password(length=10))
    app.login_page.invalid_login_message_visible()


@pytest.mark.smoke
def test_login_with_valid_credentials(app: App, configs: Config):
    app.home_page.open()
    app.home_page.is_loaded()
    app.home_page.click_login()

    app.login_page.is_loaded()
    app.login_page.login(configs.email, configs.password)

    app.projects_page.is_loaded()


def test_login_page_is_loaded(app: App):
    app.login_page.open()
    app.login_page.is_loaded()


def test_forgot_password_link(app: App):
    app.login_page.open()
    app.login_page.is_loaded()
    app.login_page.click_forgot_password()
    expect(app.page).to_have_url("/users/password/new", timeout=5000)


def test_sign_up_link(app: App):
    app.login_page.open()
    app.login_page.is_loaded()
    app.login_page.click_sign_up()
    expect(app.page).to_have_url("/users/sign_up", timeout=5000)


def test_remember_me_checkbox(app: App):
    app.login_page.open()
    app.login_page.is_loaded()
    app.login_page.set_remember_me(True)
    expect(app.login_page.remember_me).to_be_checked()


def test_google_login_redirect(app: App):
    app.login_page.open()
    app.login_page.is_loaded()
    app.login_page.login_with_google()
    expect(app.page).not_to_have_url("/users/sign_in", timeout=5000)


def test_github_login_redirect(app: App):
    app.login_page.open()
    app.login_page.is_loaded()
    app.login_page.login_with_github()
    expect(app.page).not_to_have_url("/users/sign_in", timeout=5000)
