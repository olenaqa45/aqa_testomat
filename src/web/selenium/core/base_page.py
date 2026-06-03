from typing import Self

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from web.selenium.core.waits import Selector, SelectorOrElement, Wait


def _resolve(target: SelectorOrElement, driver: WebDriver, wait: Wait) -> WebElement:
    if isinstance(target, WebElement):
        return target
    return driver.find_element(*target)


def _resolve_visible(target: SelectorOrElement, wait: Wait) -> WebElement:
    if isinstance(target, WebElement):
        return target
    return wait.until_visible(target)


def _resolve_clickable(target: SelectorOrElement, wait: Wait) -> WebElement:
    if isinstance(target, WebElement):
        return target
    return wait.until_clickable(target)


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = Wait(driver)

    def open(self, url: str) -> Self:
        self.driver.get(url)
        return self

    def refresh(self) -> Self:
        self.driver.refresh()
        return self

    def find(self, target: SelectorOrElement) -> WebElement:
        return _resolve(target, self.driver, self.wait)

    def find_all(self, locator: Selector) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def find_visible(self, target: SelectorOrElement) -> WebElement:
        return _resolve_visible(target, self.wait)

    def find_clickable(self, target: SelectorOrElement) -> WebElement:
        return _resolve_clickable(target, self.wait)

    def click(self, target: SelectorOrElement) -> Self:
        _resolve_clickable(target, self.wait).click()
        return self

    def type_text(self, target: SelectorOrElement, text: str) -> Self:
        _resolve_visible(target, self.wait).send_keys(text)
        return self
