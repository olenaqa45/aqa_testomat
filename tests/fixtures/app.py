import os

import pytest
from playwright.sync_api import Browser, Page

from web.app import App


@pytest.fixture(scope="function")
def app(page: Page) -> App:
    return App(page)


@pytest.fixture(scope="function")
def logged_app(browser: Browser, storage_state: str):
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


@pytest.fixture(scope="function")
def free_project_app(browser: Browser, free_storage_state: str):
    context = browser.new_context(
        base_url=os.getenv("BASE_APP_URL"),
        viewport={"width": 1920, "height": 1080},
        locale="uk-UA",
        timezone_id="Europe/Kyiv",
        ignore_https_errors=True,
        storage_state=free_storage_state,
    )
    page = context.new_page()
    yield App(page)
    page.close()
    context.close()
