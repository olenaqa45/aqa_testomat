import pytest

from web.app import App

PROJECTS_NAME: str = "QA Club Lviv"
TARGET_PROJECT: str = "Jacobson LLC"


@pytest.mark.smoke
def test_projects_page_header(logged_app: App):
    logged_app.projects_page.open()
    logged_app.projects_page.should_be_loaded()
    # authenticated_app.projects_page.flash_message_visible()
    logged_app.projects_page.select_projects_name(PROJECTS_NAME)
    logged_app.projects_page.enterprise_plan_is_visible("Enterprise plan")

    logged_app.projects_page.switch_to_table_view()
    logged_app.projects_page.switch_to_grid_view()

    logged_app.projects_page.get_project_names()
    logged_app.projects_page.search_project(TARGET_PROJECT)
    logged_app.projects_page.count_of_project_visible(1)

    card = logged_app.projects_page.get_project_card(TARGET_PROJECT)
    card.is_visible()
    print(card.get_name())


@pytest.mark.smoke
def test_new_project_create(logged_app: App):
    logged_app.projects_page.open()
    logged_app.projects_page.should_be_loaded()
    logged_app.projects_page.select_projects_name(PROJECTS_NAME)
    logged_app.projects_page.click_create()
