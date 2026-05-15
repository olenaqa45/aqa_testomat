import os
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright

from tests.fixtures.config import Config
from web.app import App

STORAGE_STATE_PATH = "test-result/.auth.json"
FREE_STORAGE_STATE_PATH = "test-result/.free_auth.json"
TRACES_DIR = Path("test-result/traces")


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


def _create_context(
    browser: Browser,
    storage_state: str | None = None,
) -> BrowserContext:
    TRACES_DIR.mkdir(parents=True, exist_ok=True)
    return browser.new_context(
        base_url=os.getenv("BASE_APP_URL"),
        viewport={"width": 1920, "height": 1080},
        locale="uk-UA",
        timezone_id="Europe/Kyiv",
        ignore_https_errors=True,
        storage_state=storage_state,
        record_video_dir=str(TRACES_DIR / "videos"),
    )


def start_tracing(context: BrowserContext) -> None:
    context.tracing.start(screenshots=True, snapshots=True, sources=True)


def stop_tracing(context: BrowserContext, request: pytest.FixtureRequest) -> None:
    TRACES_DIR.mkdir(parents=True, exist_ok=True)
    failed = request.node.rep_call.failed if hasattr(request.node, "rep_call") else False
    if failed:
        context.tracing.stop(path=str(TRACES_DIR / f"{request.node.name}-trace.zip"))
    else:
        context.tracing.stop()


def save_screenshot(page: Page, request: pytest.FixtureRequest) -> None:
    failed = request.node.rep_call.failed if hasattr(request.node, "rep_call") else False
    if failed:
        TRACES_DIR.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(TRACES_DIR / f"{request.node.name}.png"))


def save_video(page: Page, request: pytest.FixtureRequest) -> None:
    failed = request.node.rep_call.failed if hasattr(request.node, "rep_call") else False
    video = page.video
    if video:
        if failed:
            TRACES_DIR.mkdir(parents=True, exist_ok=True)
            video.save_as(str(TRACES_DIR / f"{request.node.name}.webm"))
        else:
            video.delete()


@pytest.fixture(scope="function")
def context(browser: Browser, request: pytest.FixtureRequest) -> BrowserContext:
    context = _create_context(browser)
    start_tracing(context)
    yield context
    stop_tracing(context, request)
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext, request: pytest.FixtureRequest) -> Page:
    page = context.new_page()
    yield page
    try:
        save_screenshot(page, request)
    finally:
        page.close()
        save_video(page, request)
