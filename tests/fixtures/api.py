import pytest

from api.api_client import ApiClient
from api.projects_api import ProjectsApi
from tests.fixtures.config import Config


@pytest.fixture(scope="session")
def api_client(configs: Config) -> ApiClient:
    client = ApiClient(base_url=configs.login_url, api_token=configs.api_token)
    yield client


@pytest.fixture(scope="session")
def projects_api(api_client: ApiClient) -> ProjectsApi:
    return ProjectsApi(api_client)
