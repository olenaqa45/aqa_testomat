import os

import pytest
from faker import Faker
from playwright.sync_api import (Page, expect)


@pytest.fixture(scope="function")
def login(page: Page, configs):
    page.goto(configs.login_url)
    login_user(page, configs.email, configs.password)

TARGET_PROJECT: str = "Brown PLC"

# check login with invalid creds is not possible
def test_login_with_invalid_creds(page: Page, configs):
    # arrange
    open_home_page(page)
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    # act
    page.get_by_text("Log in", exact=True).click()

    invalid_password = Faker().password(length=10)

    login_user(page, configs.email, invalid_password)

    # assert
    expect(page.locator("#content-desktop").get_by_text("Invalid email or password.")).to_be_visible()
    expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid email or password.")


# search target_project by title
def test_search_project_in_company(page: Page, login):

    search_for_project(page, TARGET_PROJECT)

    expect(page.get_by_title(TARGET_PROJECT)).to_be_visible()
    expect(page.get_by_role("heading", name=TARGET_PROJECT)).to_be_visible()


# open free projects
def test_should_be_possible_to_open_free_project(page: Page, login):

    page.locator("#company_id").click()
    page.locator("#company_id").select_option("Free Projects")
    # assert
    search_for_project(page, TARGET_PROJECT)

    expect(page.get_by_role("heading", name=TARGET_PROJECT)).to_be_hidden()
    expect(page.get_by_text("You have not created any projects yet")).to_be_visible(timeout=10000)


# create new project button is visible
def test_create_new_project(page: Page, login):

    page.locator("#company_id").click()
    page.locator("#company_id").select_option("Free Projects")

    expect(page.get_by_role("link", name="Create project")).to_be_visible()


# assigned functions
def search_for_project(page: Page, target_project: str):
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    page.locator("#content-desktop #search").fill(target_project)


def open_home_page(page: Page):
    page.goto(os.getenv("BASE_URL"))


def login_user(page: Page, email: str, password: str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role("button", name="Sign in").click()
