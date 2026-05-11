import random

import pytest
from faker import Faker

from api.api_client import ApiClient
from web.app import App


@pytest.mark.smoke
def test_new_project_page_elements(logged_app: App):
    logged_app.new_projects_page.open()
    logged_app.new_projects_page.should_be_loaded()


@pytest.mark.smoke
def test_new_project_creation(logged_app: App):
    target_project_name = Faker().company()

    (
        logged_app.new_projects_page.open()
        .should_be_loaded()
        .select_classical()
        .fill_project_title(target_project_name)
        .click_create()
    )

    (logged_app.project_page.should_be_loaded().empty_project_name_is(target_project_name).close_read_me_left())

    (logged_app.project_page.side_bar.open().should_be_loaded().click_logo())


def test_open_project_and_create_from_side_bar(projects_api, logged_app: App):
    response = projects_api.get_projects()
    all_projects = response.json()["data"]

    empty_projects = [p for p in all_projects if p["attributes"].get("tests-count", 0) == 0]
    target_project = random.choice(empty_projects) if empty_projects else random.choice(all_projects)
    target_project_id = target_project["id"]

    logged_app.project_page.open(target_project_id).should_be_loaded()
    logged_app.project_page.side_bar.open()
    logged_app.project_page.side_bar.should_be_loaded()

    test_name = Faker().sentence()
    logged_app.project_page.side_bar.tests_link.click()
    logged_app.project_page.first_suite_input.fill(test_name)
    logged_app.project_page.suite_btn_is_visible()
    print(test_name)
