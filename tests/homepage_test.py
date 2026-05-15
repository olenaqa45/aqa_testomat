import pytest
from playwright.sync_api import Page, expect

EXPECTED_TITLE = "AI Test Management Tool | Testomat.io"


@pytest.mark.smoke
def test_start_for_free(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title(EXPECTED_TITLE)
    page.locator("#header").get_by_role("link", name="Start for free").click()
    expect(page).to_have_url("https://app.testomat.io/users/sign_up")


@pytest.mark.regression
def test_start_for_free_2(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title(EXPECTED_TITLE)

    with page.context.expect_page() as new_page_info:
        page.locator("#welcome_section").get_by_role("link", name="Start for free").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://app.testomat.io/users/sign_up")


@pytest.mark.regression
def test_start_for_free_3(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title(EXPECTED_TITLE)
    page.locator("#welcome_section").get_by_role("link", name="Start for free").evaluate(
        "el => el.removeAttribute('target')"
    )
    page.locator("#welcome_section").get_by_role("link", name="Start for free").click()
    expect(page).to_have_url("https://app.testomat.io/users/sign_up")
