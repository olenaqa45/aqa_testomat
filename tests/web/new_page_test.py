from faker.proxy import Faker
from playwright.sync_api import Page

from web.pages.NewProject import NewProject
from web.pages.NewProjectsPage import NewProjectsPage


def test_new_project_page_elements(page: Page, login):
    new_projects = NewProjectsPage(page)
    new_projects.open()
    new_projects.is_loaded()


def test_new_project_creation(page: Page, login):
    target_project_name = Faker().company()

    (NewProjectsPage(page)
     .open()
     .is_loaded()
     .select_classical()
     .fill_project_title(target_project_name)
     .click_create()
     )

    (NewProject(page)
     .is_loaded()
     .empty_project_name_is(target_project_name)
     .close_read_me_left()
     )
