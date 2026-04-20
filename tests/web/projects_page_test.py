import pytest

from web.App import App

PROJECTS_NAME: str = "QA Club Lviv"
TARGET_PROJECT: str = "Jacobson LLC"

@pytest.mark.smoke
def test_projects_page_header(login: App):
    login.projects_page.open()
    login.projects_page.is_loaded()
    # login.projects_page.flash_message_visible()
    login.projects_page.select_projects_name(PROJECTS_NAME)
    login.projects_page.enterprise_plan_is_visible("Enterprise plan")

    login.projects_page.switch_to_table_view()
    login.projects_page.switch_to_grid_view()

    login.projects_page.get_project_names()
    login.projects_page.search_project(TARGET_PROJECT)
    login.projects_page.count_of_project_visible(1)

    card = login.projects_page.get_project_card(TARGET_PROJECT)
    card.is_visible()
    print(card.get_name())


def test_new_project_create(login: App):
    login.projects_page.open()
    login.projects_page.is_loaded()
    login.projects_page.select_projects_name(PROJECTS_NAME)
    login.projects_page.click_create()
