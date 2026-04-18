import pytest
from faker.proxy import Faker

from web.App import App


def test_new_project_page_elements(app: App, login):
    app.new_projects_page.open()
    app.new_projects_page.is_loaded()


@pytest.mark.smoke
def test_new_project_creation(app: App, login):
    target_project_name = Faker().company()

    (app.new_projects_page
     .open()
     .is_loaded()
     .select_classical()
     .fill_project_title(target_project_name)
     .click_create()
     )

    (app.project_page
     .is_loaded()
     .empty_project_name_is(target_project_name)
     .close_read_me_left()
     )

    # app.page.pause()

    (app.project_page.side_bar
     .open()
     .is_loaded()
     .click_logo()
     )
