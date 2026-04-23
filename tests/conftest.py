import os
from dataclasses import dataclass

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, Browser, BrowserContext, Playwright

from web.app import App

load_dotenv()

STORAGE_STATE_PATH = "test-result/.auth.json"


@dataclass(frozen=True)
class Config:
    base_url: str
    login_url: str
    email: str
    password: str


@pytest.fixture(scope="session")
def configs() -> Config:
    return Config(
        base_url=os.getenv("BASE_URL"),
        login_url=os.getenv("BASE_APP_URL"),
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
    )


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


@pytest.fixture(scope="function")
def app(page: Page) -> App:
    return App(page)


@pytest.fixture(scope="function")
def authenticated_app(browser: Browser, storage_state: str):
    context = browser.new_context(
        base_url=os.getenv("BASE_APP_URL"),
        viewport={"width": 1920, "height": 1080},
        locale="uk-UA",
        timezone_id="Europe/Kyiv",
        ignore_https_errors=True,
        storage_state=storage_state,
    )
    page = context.new_page()
    yield App(page)
    page.close()
    context.close()
