from playwright.sync_api import (Page, expect)

def test_login_with_invalid_creds(page: Page):
    # arrange
    open_home_page(page)
    expect(page.locator("[href*='sign_in'].login-item")).to_be_visible()

    # act
    page.get_by_text("Log in",exact=True).click()
    login_user(page, "olena.qa45@gmail.com", "awwqedfcdfdf1!s")

    # assert
    expect(page.locator("#content-desktop").get_by_text("Invalid Email or password.")).to_be_visible()
    # expect(page.locator("#content-desktop .common-flash-info")).to_have_text("Invalid Email or password.")


# search target_project by title
def test_search_project_in_company(page: Page):
    # arrange
    page.goto("https://app.testomat.io/users/sign_in")
    login_user(page, "olena.qa45@gmail.com", "olololl")

    # act
    target_project = "Brown PLC"
    search_for_project(page, target_project)

    # assert
    expect(page.get_by_title(target_project)).to_be_visible()
    expect(page.get_by_role("heading", name=target_project)).to_be_visible()
    # expect(page.locator("ul li h3",has_text=target_project)).to_be_visible()
    # expect(page.locator("ul li h3").filter(has_text=target_project)).to_have_text(target_project)


# open free projects
def test_should_be_possible_to_open_free_project(page: Page):
    # arrange
    page.goto("https://app.testomat.io/users/sign_in")
    login_user(page, "olena.qa45@gmail.com", "oll123Oll#testnew")
    # act
    page.locator("#company_id").click()
    page.locator("#company_id").select_option("Free Projects")
    # assert
    target_project: str = "Brown PLC"
    search_for_project(page, target_project)

    expect(page.get_by_role("heading", name=target_project)).to_be_hidden()
    expect(page.get_by_text("You have not created any projects yet")).to_be_visible(timeout=10000)


# create new project some broken test
# def test_create_new_project(page: Page):
# page.goto("https://app.testomat.io/users/sign_in")
# login_user(page, "olena.qa45@gmail.com", "oll123Oll#testnew")

# page.locator("#company_id").click()
# page.locator("#company_id").select_option("Free Projects")

# page.get_by_role("button", name="Create project").click()
# page.get_by_role("link", name="href=/projects/new").click()


# assigned functions
def search_for_project(page: Page, target_project: str):
    expect(page.get_by_role("searchbox", name="Search")).to_be_visible()
    page.locator("#content-desktop #search").fill(target_project)


def open_home_page(page: Page):
    page.goto("https://testomat.io")


def login_user(page: Page, email: str, password: str):
    page.locator("#content-desktop #user_email").fill(email)
    page.locator("#content-desktop #user_password").fill(password)
    page.get_by_role("button", name="Sign in").click()