import httpx

from api.api_client import ApiClient


class ProjectsApi:
    def __init__(self, client: ApiClient):
        self._client = client

    def get_projects(self) -> httpx.Response:
        return self._client.get("/api/projects")
