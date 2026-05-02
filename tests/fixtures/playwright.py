import os

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright

from tests.fixtures.config import Config
from web.app import App

STORAGE_STATE_PATH = "test-result/.auth.json"
FREE_STORAGE_STATE_PATH = "test-result/.free_auth.json"


@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> Browser:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=300,
    )
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def storage_state(browser: Browser, configs: Config) -> str:
    context = browser.new_context(
        base_url=configs.login_url,
        viewport={"width": 1920, "height": 1080},
    )
    page = context.new_page()
    app = App(page)
    app.login_page.open()
    app.login_page.should_be_loaded()
    app.login_page.login_user(configs.email, configs.password)
    app.projects_page.should_be_loaded()
    context.storage_state(path=STORAGE_STATE_PATH)
    page.close()
    context.close()
    return STORAGE_STATE_PATH


@pytest.fixture(scope="session")
def free_storage_state(browser: Browser, storage_state: str, configs: Config) -> str:
    context = browser.new_context(
        base_url=configs.login_url,
        viewport={"width": 1920, "height": 1080},
        storage_state=storage_state,
    )
    page = context.new_page()
    app = App(page)
    app.projects_page.open()
    app.projects_page.should_be_loaded()
    app.projects_page.select_projects_name("Free Projects")
    context.storage_state(path=FREE_STORAGE_STATE_PATH)
    page.close()
    context.close()
    return FREE_STORAGE_STATE_PATH


@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context(
        base_url=os.getenv("BASE_APP_URL"),
        viewport={"width": 1920, "height": 1080},
        locale="uk-UA",
        timezone_id="Europe/Kyiv",
        ignore_https_errors=True,
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()
