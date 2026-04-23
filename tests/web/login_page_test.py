from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest
from faker import Faker
from playwright.sync_api import expect

from web.app import App

if TYPE_CHECKING:
    from tests.conftest import Config


fake = Faker()

VALID_EMAIL = os.getenv("EMAIL")
VALID_PASSWORD = os.getenv("PASSWORD")

# Equivalence classes & boundary values for EMAIL:
# Valid class: correct format (user@domain.com)
# Invalid classes: empty, no @, no domain, spaces, special chars, too long
EMPTY = ""
SPACES_ONLY = "   "
NO_AT = "userexample.com"
NO_DOMAIN = "user@"
NO_USER = "@example.com"
SPECIAL_CHARS_EMAIL = "user!#$%@example.com"
LONG_EMAIL = fake.pystr(min_chars=255, max_chars=255) + "@test.com"
SQL_INJECTION = "' OR 1=1 --"
XSS_INPUT = "<script>alert(1)</script>"
FAKE_EMAIL = fake.email()

# Equivalence classes & boundary values for PASSWORD:
# Valid class: correct password (8+ chars typically)
# Invalid classes: empty, 1 char (boundary min), too short, too long, spaces
ONE_CHAR_PASSWORD = "a"
SHORT_PASSWORD = "abc"
LONG_PASSWORD = fake.pystr(min_chars=256, max_chars=256)
FAKE_PASSWORD = fake.password(length=10)

invalid_login_data = [
    # Empty values
    # pytest.param(EMPTY, EMPTY, id="both_empty"),
    # pytest.param(EMPTY, VALID_PASSWORD, id="empty_email_valid_password"),
    pytest.param(VALID_EMAIL, EMPTY, id="valid_email_empty_password"),
    # pytest.param(SPACES_ONLY, VALID_PASSWORD, id="spaces_email"),
    # pytest.param(VALID_EMAIL, SPACES_ONLY, id="spaces_password"),

    # Invalid email format
    # pytest.param(NO_AT, VALID_PASSWORD, id="email_no_at_sign"),
    # pytest.param(NO_DOMAIN, VALID_PASSWORD, id="email_no_domain"),
    # pytest.param(NO_USER, VALID_PASSWORD, id="email_no_user"),
    pytest.param(SPECIAL_CHARS_EMAIL, VALID_PASSWORD, id="email_special_chars"),
    #
    # # Boundary: email length
    pytest.param(LONG_EMAIL, VALID_PASSWORD, id="email_too_long"),
    #
    # # Wrong credentials (valid format, wrong values)
    pytest.param(FAKE_EMAIL, VALID_PASSWORD, id="wrong_email_valid_password"),
    pytest.param(VALID_EMAIL, FAKE_PASSWORD, id="valid_email_wrong_password"),
    pytest.param(FAKE_EMAIL, FAKE_PASSWORD, id="wrong_email_wrong_password"),

    # Boundary: password length
    pytest.param(VALID_EMAIL, ONE_CHAR_PASSWORD, id="password_1_char"),
    # pytest.param(VALID_EMAIL, SHORT_PASSWORD, id="password_too_short"),
    # pytest.param(VALID_EMAIL, LONG_PASSWORD, id="password_too_long"),

    # Security
    pytest.param(SQL_INJECTION, VALID_PASSWORD, id="sql_injection_email"),
    pytest.param(VALID_EMAIL, SQL_INJECTION, id="sql_injection_password"),
    pytest.param(XSS_INPUT, VALID_PASSWORD, id="xss_email"),
    pytest.param(VALID_EMAIL, XSS_INPUT, id="xss_password"),
]


@pytest.mark.regression
@pytest.mark.parametrize("email, password", invalid_login_data)
def test_login_invalid(app: App, email: str, password: str):
    app.home_page.open()
    app.home_page.should_be_loaded()
    app.home_page.click_login()

    app.login_page.should_be_loaded()
    app.login_page.login_user(email, password)
    app.login_page.invalid_login_message_visible()


@pytest.mark.smoke
def test_login_with_valid_credentials(app: App, configs: Config):
    app.home_page.open()
    app.home_page.should_be_loaded()
    app.home_page.click_login()

    app.login_page.should_be_loaded()
    app.login_page.login_user(configs.email, configs.password)

    app.projects_page.should_be_loaded()


@pytest.mark.smoke
def test_login_page_is_loaded(app: App):
    app.login_page.open()
    app.login_page.should_be_loaded()


@pytest.mark.regression
def test_forgot_password_link(app: App):
    app.login_page.open()
    app.login_page.should_be_loaded()
    app.login_page.click_forgot_password()
    expect(app.page).to_have_url("/users/password/new", timeout=5000)


@pytest.mark.regression
def test_sign_up_link(app: App):
    app.login_page.open()
    app.login_page.should_be_loaded()
    app.login_page.click_sign_up()
    expect(app.page).to_have_url("/users/sign_up", timeout=5000)


@pytest.mark.regression
def test_remember_me_checkbox(app: App):
    app.login_page.open()
    app.login_page.should_be_loaded()
    app.login_page.set_remember_me(True)
    expect(app.login_page.remember_me).to_be_checked()


@pytest.mark.regression
def test_google_login_redirect(app: App):
    app.login_page.open()
    app.login_page.should_be_loaded()
    app.login_page.login_with_google()
    expect(app.page).not_to_have_url("/users/sign_in", timeout=5000)


@pytest.mark.regression
def test_github_login_redirect(app: App):
    app.login_page.open()
    app.login_page.should_be_loaded()
    app.login_page.login_with_github()
    expect(app.page).not_to_have_url("/users/sign_in", timeout=5000)
