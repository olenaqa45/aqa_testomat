import pytest
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.fixtures.config import Config

TARGET_PROJECT: str = "Jacobson LLC"


@pytest.mark.regression
def test_login_search_and_open_project(driver: WebDriver, configs: Config):
    wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])

    # Login
    driver.get(f"{configs.login_url}/users/sign_in")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content-desktop #user_email")))
    driver.find_element(By.CSS_SELECTOR, "#content-desktop #user_email").send_keys(configs.email)
    driver.find_element(By.CSS_SELECTOR, "#content-desktop #user_password").send_keys(configs.password)
    driver.find_element(By.CSS_SELECTOR, "#content-desktop [value='Sign In']").click()
    # Verify projects page loaded
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content-desktop .common-page-header h2")))

    # Search project
    driver.find_element(By.CSS_SELECTOR, "#content-desktop #search").send_keys(TARGET_PROJECT)

    # Click on the project
    project_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'#content-desktop #grid li a[title="{TARGET_PROJECT}"]'))
    )
    project_link.click()

    # Verify project page loaded
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".sticky-header h2"), TARGET_PROJECT))
