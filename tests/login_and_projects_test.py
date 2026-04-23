from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest
from faker import Faker
from playwright.sync_api import Page, expect

from web.app import App

if TYPE_CHECKING:
    from tests.conftest import Config

TARGET_PROJECT: str = "Jacobson LLC"


@pytest.mark.regression
def test_login_with_invalid_creds(page: Page, configs: Config):
    open_home_page(page)
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    page.get_by_text("Log in", exact=True).click()

    invalid_password = Faker().password(length=10)
    login_user(page, configs.email, invalid_password)

    expect(page.locator("#content-desktop").get_by_text("Invalid email or password.")).to_be_visible()
    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid email or password.")


@pytest.mark.smoke
def test_search_project_in_company(authenticated_app: App):
    authenticated_app.projects_page.open().should_be_loaded()
    authenticated_app.projects_page.search_project(TARGET_PROJECT)

    expect(authenticated_app.page.get_by_title(TARGET_PROJECT)).to_be_visible()
    expect(authenticated_app.page.get_by_role("heading", name=TARGET_PROJECT)).to_be_visible()


@pytest.mark.regression
def test_should_be_possible_to_open_free_project(authenticated_app: App):
    authenticated_app.projects_page.open().should_be_loaded()
    authenticated_app.projects_page.select_projects_name("Free Projects")
    authenticated_app.projects_page.search_project(TARGET_PROJECT)

    expect(authenticated_app.page.get_by_role("heading", name=TARGET_PROJECT)).to_be_hidden()
    expect(authenticated_app.page.get_by_text("You have not created any projects yet")).to_be_visible(timeout=10000)


@pytest.mark.regression
def test_create_project_button_visible(authenticated_app: App):
    authenticated_app.projects_page.open().should_be_loaded()
    authenticated_app.projects_page.select_projects_name("Free Projects")

    expect(authenticated_app.page.get_by_role("link", name="Create project")).to_be_visible()


def open_home_page(page: Page) -> None:
    page.goto(os.getenv("BASE_URL"))


def login_user(page: Page, email: str, password: str) -> None:
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role("button", name="Sign in").click()
