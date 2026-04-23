import pytest

from web.app import App

PROJECTS_NAME: str = "QA Club Lviv"
TARGET_PROJECT: str = "Jacobson LLC"


@pytest.mark.smoke
def test_projects_page_header(authenticated_app: App):
    authenticated_app.projects_page.open()
    authenticated_app.projects_page.should_be_loaded()
    # authenticated_app.projects_page.flash_message_visible()
    authenticated_app.projects_page.select_projects_name(PROJECTS_NAME)
    authenticated_app.projects_page.enterprise_plan_is_visible("Enterprise plan")

    authenticated_app.projects_page.switch_to_table_view()
    authenticated_app.projects_page.switch_to_grid_view()

    authenticated_app.projects_page.get_project_names()
    authenticated_app.projects_page.search_project(TARGET_PROJECT)
    authenticated_app.projects_page.count_of_project_visible(1)

    card = authenticated_app.projects_page.get_project_card(TARGET_PROJECT)
    card.is_visible()
    print(card.get_name())


@pytest.mark.smoke
def test_new_project_create(authenticated_app: App):
    authenticated_app.projects_page.open()
    authenticated_app.projects_page.should_be_loaded()
    authenticated_app.projects_page.select_projects_name(PROJECTS_NAME)
    authenticated_app.projects_page.click_create()
