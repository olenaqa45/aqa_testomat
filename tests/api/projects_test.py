import pytest
from faker import Faker

from api.controllers.suit_controller import SuiteController
from api.controllers.test_controller import TestController
from api.models.suite import Suite, SuiteInput
from api.models.test import Test, TestInput
from api.projects_api import ProjectsApi


@pytest.mark.api
def test_get_projects_returns_list(projects_api: ProjectsApi):
    response = projects_api.get_projects()

    assert response.status_code == 200
    data = response.json()["data"]
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.api
def test_get_projects_has_required_fields(projects_api: ProjectsApi):
    response = projects_api.get_projects()

    projects = response.json()["data"]
    for project in projects:
        assert "id" in project
        assert "attributes" in project
        assert "title" in project["attributes"]
        print(f"Project ID: {project['id']}, Title: {project['attributes']['title']}")


@pytest.mark.api
def test_create_project_suite(suite_controller: SuiteController, test_controller: TestController):
    # Step 1: Create a suite in the target project
    suite_input = SuiteInput(title=f"Suite {Faker().bs()}")
    suite_response = suite_controller.create_suite(suite_input)
    assert suite_response.status_code == 201
    suite_data = suite_response.json()["data"]
    suite_id = suite_data["id"]

    # Verify suite response matches the Suite model
    suite = Suite.model_validate(suite_data)
    assert suite.id is not None
    assert suite.title == suite_input.title
    assert suite.type is not None

    # Step 2: Create a test inside the suite
    test_input = TestInput(title=f"Test {Faker().sentence()}", suite_id=suite_id)
    test_response = test_controller.create_test(test_input)
    assert test_response.status_code == 201
    test_data = test_response.json()["data"]
    test_id = test_data["id"]

    # Verify test response matches the Test model
    test = Test.model_validate(test_data)
    assert test.id is not None
    assert test.title == test_input.title
    assert test.suite_id == suite_id

    # Step 3: Verify the test exists by fetching it back
    get_response = test_controller.get(test_id)
    assert get_response.status_code == 200
    fetched_test = Test.model_validate(get_response.json()["data"])
    assert fetched_test.title == test_input.title
    assert fetched_test.suite_id == suite_id

    # Print validated models
    print(f"\nSuite: {suite.model_dump_json(indent=2)}")
    print(f"\nTest: {fetched_test.model_dump_json(indent=2)}")

    # Step 4: Cleanup — delete test and suite to keep the project clean
    test_controller.delete(test_id)
    suite_controller.delete(suite_id)
