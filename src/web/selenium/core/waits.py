from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

Selector = tuple[By, str]
SelectorOrElement = Selector | WebElement

TIMEOUT = 10
POLL = 0.2
IGNORED_EXCEPTIONS = [NoSuchElementException, StaleElementReferenceException]


class Wait:
    def __init__(self, driver: WebDriver, timeout: int = TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self._wait = WebDriverWait(driver, timeout, poll_frequency=POLL, ignored_exceptions=IGNORED_EXCEPTIONS)

    def until_visible(self, locator: Selector):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def until_clickable(self, locator: Selector):
        return self._wait.until(EC.element_to_be_clickable(locator))

    def until_text_in_element(self, locator: Selector, text: str) -> bool:
        return self._wait.until(EC.text_to_be_present_in_element(locator, text))
