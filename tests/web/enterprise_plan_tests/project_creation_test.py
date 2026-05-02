import pytest
from faker import Faker

from web.app import App


@pytest.mark.smoke
def test_new_project_page_elements(logged_app: App):
    logged_app.new_projects_page.open()
    logged_app.new_projects_page.should_be_loaded()


@pytest.mark.smoke
def test_new_project_creation(logged_app: App):
    target_project_name = Faker().company()

    (logged_app.new_projects_page
     .open()
     .should_be_loaded()
     .select_classical()
     .fill_project_title(target_project_name)
     .click_create()
     )

    (logged_app.project_page
     .should_be_loaded()
     .empty_project_name_is(target_project_name)
     .close_read_me_left()
     )

    (logged_app.project_page.side_bar
     .open()
     .should_be_loaded()
     .click_logo()
     )
