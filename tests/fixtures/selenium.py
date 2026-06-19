import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.fixtures.config import Config


@pytest.fixture(scope="function")
def driver(configs: Config) -> webdriver.Chrome:
    options = Options()
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
