from playwright.sync_api import Page

from web.pages.ProjectsPage import ProjectsPage

PROJECTS_NAME: str = "QA Club Lviv"
TARGET_PROJECT: str = "Brown PLC"
SEARCH_PROJECT_VAlUE: str = "PLC"


def test_projects_page_header(page: Page, login):
    projects_page = ProjectsPage(page)
    projects_page.is_loaded()
    projects_page.flash_message_visible()
    projects_page.select_projects_name(PROJECTS_NAME)
    projects_page.enterprise_plan_is_visible("Enterprise plan")

    projects_page.switch_to_table_view()
    projects_page.switch_to_grid_view()

    projects_page.get_project_names()
    projects_page.search_project(TARGET_PROJECT)
    projects_page.count_of_project_visible(1)

    card = projects_page.get_project_card(TARGET_PROJECT)
    card.is_visible()
    print(card.get_name())


def test_new_project_create(page: Page, login):
    projects_page = ProjectsPage(page)
    projects_page.is_loaded()
    projects_page.select_projects_name(PROJECTS_NAME)
    projects_page.click_create()
    # write what to expect
