import os
from dataclasses import dataclass

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from web.App import App

load_dotenv()

@dataclass(frozen=True)
class Config:
    base_url: str
    login_url: str
    email: str
    password: str


@pytest.fixture(scope="session")
def configs():
    return Config(
        base_url=os.getenv("BASE_URL"),
        login_url=os.getenv("BASE_APP_URL"),
        email=os.getenv("EMAIL"),
        password=os.getenv("PASSWORD"),
    )

@pytest.fixture(scope="function")
def app(page: Page) -> App:
    return App(page)

@pytest.fixture(scope="function")
def login(app: App, configs: Config):
    app.login_page.open()
    app.login_page.is_loaded()
    app.login_page.login(configs.email, configs.password)