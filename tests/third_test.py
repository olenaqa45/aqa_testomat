from playwright.sync_api import Page, expect

#check that Start for free button2 is functional on #welcome_section. Open in New page
def test_start_for_free_2(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title('AI Test Management Tool | Testomat.io')

    with page.context.expect_page() as new_page_info:
        page.locator("#welcome_section").get_by_role("link", name="Start for free").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://app.testomat.io/users/sign_up")

#check that Start for free button2 is functional on #welcome_section. Open in the same tab
def test_start_for_free_3(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title('AI Test Management Tool | Testomat.io')
    page.locator("#welcome_section").get_by_role("link", name="Start for free").evaluate(
        "el => el.removeAttribute('target')"
    )
    page.locator("#welcome_section").get_by_role("link", name="Start for free").click()
    expect(page).to_have_url("https://app.testomat.io/users/sign_up")