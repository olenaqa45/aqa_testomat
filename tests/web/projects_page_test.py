from web.App import App

PROJECTS_NAME: str = "QA Club Lviv"
TARGET_PROJECT: str = "Jacobson LLC"

def test_projects_page_header(app: App, login):
    app.projects_page.is_loaded()
    app.projects_page.flash_message_visible()
    app.projects_page.select_projects_name(PROJECTS_NAME)
    app.projects_page.enterprise_plan_is_visible("Enterprise plan")

    app.projects_page.switch_to_table_view()
    app.projects_page.switch_to_grid_view()

    app.projects_page.get_project_names()
    app.projects_page.search_project(TARGET_PROJECT)
    app.projects_page.count_of_project_visible(1)

    card = app.projects_page.get_project_card(TARGET_PROJECT)
    card.is_visible()
    print(card.get_name())


def test_new_project_create(app: App, login):
    app.projects_page.is_loaded()
    app.projects_page.select_projects_name(PROJECTS_NAME)
    app.projects_page.click_create()

