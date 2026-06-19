import pytest

from api.api_client import ApiClient
from api.controllers.project_controller import ProjectController
from api.controllers.suit_controller import SuiteController
from api.controllers.test_controller import TestController
from api.projects_api import ProjectsApi
from tests.fixtures.config import Config


@pytest.fixture(scope="session")
def api_client(configs: Config) -> ApiClient:
    client = ApiClient(base_url=configs.login_url, api_token=configs.api_token)
    yield client


@pytest.fixture(scope="session")
def projects_api(api_client: ApiClient) -> ProjectsApi:
    return ProjectsApi(api_client)


@pytest.fixture(scope="session")
def project_controller(configs: Config) -> ProjectController:
    controller = ProjectController(
        base_url=configs.login_url, api_token=configs.api_token, project_id=configs.project_id
    )
    yield controller
    controller.close()


@pytest.fixture(scope="session")
def test_controller(configs: Config) -> TestController:
    controller = TestController(base_url=configs.login_url, api_token=configs.api_token, project_id=configs.project_id)
    yield controller
    controller.close()


@pytest.fixture(scope="session")
def suite_controller(configs: Config) -> SuiteController:
    controller = SuiteController(base_url=configs.login_url, api_token=configs.api_token, project_id=configs.project_id)
    yield controller
    controller.close()
