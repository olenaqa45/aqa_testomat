import pytest
from playwright.sync_api import Browser, BrowserContext, Page

from tests.fixtures.playwright import (
    _create_context,
    save_screenshot,
    save_video,
    start_tracing,
    stop_tracing,
)
from web.app import App


@pytest.fixture(scope="function")
def app(page: Page) -> App:
    return App(page)


@pytest.fixture(scope="function")
def logged_context(browser: Browser, storage_state: str, request: pytest.FixtureRequest) -> BrowserContext:
    context = _create_context(browser, storage_state=storage_state)
    start_tracing(context)
    yield context
    stop_tracing(context, request)
    context.close()


@pytest.fixture(scope="function")
def logged_page(logged_context: BrowserContext, request: pytest.FixtureRequest) -> Page:
    page = logged_context.new_page()
    yield page
    try:
        save_screenshot(page, request)
    finally:
        page.close()
        save_video(page, request)


@pytest.fixture(scope="function")
def logged_app(logged_page: Page) -> App:
    return App(logged_page)


@pytest.fixture(scope="function")
def free_context(browser: Browser, free_storage_state: str, request: pytest.FixtureRequest) -> BrowserContext:
    context = _create_context(browser, storage_state=free_storage_state)
    start_tracing(context)
    yield context
    stop_tracing(context, request)
    context.close()


@pytest.fixture(scope="function")
def free_page(free_context: BrowserContext, request: pytest.FixtureRequest) -> Page:
    page = free_context.new_page()
    yield page
    try:
        save_screenshot(page, request)
    finally:
        page.close()
        save_video(page, request)


@pytest.fixture(scope="function")
def free_project_app(free_page: Page) -> App:
    return App(free_page)
