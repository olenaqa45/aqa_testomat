from playwright.sync_api import Page, expect


# check that Start for free button2 is functional on #welcome_section. Open in New page
def test_start_for_free_2(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title('AI Test Management Tool | Testomat.io')

    with page.context.expect_page() as new_page_info:
        page.locator("#welcome_section").get_by_role("link", name="Start for free").click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    expect(new_page).to_have_url("https://app.testomat.io/users/sign_up")


# check that Start for free button2 is functional on #welcome_section. Open in the same tab
def test_start_for_free_3(page: Page):
    page.goto("https://testomat.io")
    expect(page).to_have_title('AI Test Management Tool | Testomat.io')
    page.locator("#welcome_section").get_by_role("link", name="Start for free").evaluate(
        "el => el.removeAttribute('target')"
    )
    page.locator("#welcome_section").get_by_role("link", name="Start for free").click()
    expect(page).to_have_url("https://app.testomat.io/users/sign_up")

    # some text


def test_search_project_in_company(page: Page):
    # arrange
    page.goto(LOGIN_URL)
    login_user(page, EMAIL, PASSWORD)

    # act
    target_project = "Brown PLC"
    search_for_project(page, target_project)

    # assert
    expect(page.get_by_title(target_project)).to_be_visible()
    expect(page.get_by_role("heading", name=target_project)).to_be_visible()
    expect(page.locator("ul li h3", has_text=target_project)).to_be_visible()
    expect(page.locator("ul li h3").filter(has_text=target_project)).to_have_text(target_project)

    # create new project some broken test
    # def test_create_new_project(page: Page):
    # page.goto("https://app.testomat.io/users/sign_in")
    # login_user(page, "olena.qa45@gmail.com", "fkjhadfgnj")

    # page.locator("#company_id").click()
    # page.locator("#company_id").select_option("Free Projects")

    # page.get_by_role("button", name="Create project").click()
    # page.get_by_role("link", name="href=/projects/new").click()

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
