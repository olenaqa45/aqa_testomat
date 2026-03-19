from playwright.sync_api import Page, expect


def test_start_for_free(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title('AI Test Management Tool | Testomat.io')
    page.locator("#header").get_by_role("link", name="Start for free").click()
    expect(page).to_have_url("https://app.testomat.io/users/sign_up")
    #expect(page).to_have_title('Testomat.io')