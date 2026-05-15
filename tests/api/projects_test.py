import pytest

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
