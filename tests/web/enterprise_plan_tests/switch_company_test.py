import pytest
from playwright.sync_api import expect

from web.app import App


@pytest.mark.smoke
def test_projects_page_header_free_project(logged_app: App) -> None:
    logged_app.projects_page.open()
    logged_app.projects_page.should_be_loaded()
    logged_app.projects_page.enterprise_plan_is_visible("Enterprise Plan")
    logged_app.projects_page.select_projects_name("Free Projects")
    expect(logged_app.page.get_by_text("You have not created any projects yet")).to_be_visible()
    expect(logged_app.projects_page.free_plan_label).to_be_visible()
    logged_app.projects_page.free_plan_label.hover(timeout=500)
    # logged_app.page.pause()
    expect(logged_app.page.get_by_text("You have a free subscription")).to_be_visible()
    logged_app.page.context.storage_state(path="test-result/.free_auth.json")
