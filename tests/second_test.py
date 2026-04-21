import os

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

LOGIN_URL = os.getenv("BASE_APP_URL") + "/users/sign_in"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# EXPECTED_TITLE = "AI Test Management Solutions & Automated Testing Tool | Testomat"
EXPECTED_TITLE = "AI Test Management Tool & Platform | QA Software Testomat.io"
TARGET_PROJECT: str = "Jacobson LLC"


# check that Start for free button is functional on the header
def test_start_for_free(page: Page, configs):
    page.goto("https://testomat.io")
    # open_home_page(page)
    expect(page).to_have_title(EXPECTED_TITLE)
    page.locator("#header").get_by_role("link", name="Start for free").click()
    expect(page).to_have_url("https://app.testomat.io/users/sign_up")


# check that Start for free button2 is functional on #welcome_section. Open in New page
def test_start_for_free_2(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title(EXPECTED_TITLE)

    with page.context.expect_page() as new_page_info:
        page.locator("#welcome_section").get_by_role("link", name="Start for free").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://app.testomat.io/users/sign_up")


# check that Start for free button2 is functional on #welcome_section. Open in the same tab
def test_start_for_free_3(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title(EXPECTED_TITLE)
    page.locator("#welcome_section").get_by_role("link", name="Start for free").evaluate(
        "el => el.removeAttribute('target')"
    )
    page.locator("#welcome_section").get_by_role("link", name="Start for free").click()
    expect(page).to_have_url("https://app.testomat.io/users/sign_up")


def test_search_project_in_company(page: Page):
    # arrange
    page.goto(LOGIN_URL)
    login_user(page, EMAIL, PASSWORD)

    # act
    search_for_project(page, TARGET_PROJECT)


    # assert
    expect(page.get_by_title(TARGET_PROJECT)).to_be_visible()
    expect(page.get_by_role("heading", name=TARGET_PROJECT)).to_be_visible()
    expect(page.locator("ul li h3", has_text=TARGET_PROJECT)).to_be_visible()
    expect(page.locator("ul li h3").filter(has_text=TARGET_PROJECT)).to_have_text(TARGET_PROJECT)


# assigned functions
def search_for_project(page: Page, target_project: str):
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    page.locator("#content-desktop #search").fill(target_project)


def open_home_page(page: Page):
    page.goto(os.getenv("BASE_URL"))


def login_user(page: Page, email: str, password: str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role("button", name="Sign in").click()
