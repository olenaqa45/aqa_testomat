from __future__ import annotations

import logging

import httpx

logger = logging.getLogger(__name__)


class BaseController:
    """Base controller for API v2 project-scoped resources with API key auth."""

    BASE_PATH: str = ""

    def __init__(self, base_url: str, api_token: str, project_id: str):
        self.base_url = base_url
        self.api_token = api_token
        self._client = httpx.Client(base_url=base_url, timeout=30)
        self._project_id = project_id
        logger.info("Initialized %s for project '%s'", self.__class__.__name__, project_id)

    @property
    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_token}"}

    @property
    def _path(self) -> str:
        return f"/api/v2/{self._project_id}/{self.BASE_PATH}"

    def _resource_path(self, resource_id: str) -> str:
        return f"{self._path}/{resource_id}"

    def _log_response(self, response: httpx.Response, data: dict | None = None) -> None:
        logger.info("%s %s → %d", response.request.method, response.request.url.path, response.status_code)
        if data:
            logger.info("Request body: %s", data)

    def list(self, **params) -> httpx.Response:
        response = self._client.get(self._path, headers=self._headers, params=params)
        self._log_response(response)
        response.raise_for_status()
        return response

    def get(self, resource_id: str) -> httpx.Response:
        response = self._client.get(self._resource_path(resource_id), headers=self._headers)
        self._log_response(response)
        response.raise_for_status()
        return response

    def create(self, data: dict) -> httpx.Response:
        response = self._client.post(self._path, headers=self._headers, json=data)
        self._log_response(response, data)
        response.raise_for_status()
        return response

    def update(self, resource_id: str, data: dict) -> httpx.Response:
        response = self._client.put(self._resource_path(resource_id), headers=self._headers, json=data)
        self._log_response(response, data)
        response.raise_for_status()
        return response

    def delete(self, resource_id: str) -> httpx.Response:
        response = self._client.delete(self._resource_path(resource_id), headers=self._headers)
        self._log_response(response)
        response.raise_for_status()
        return response

    def close(self) -> None:
        logger.info("Closing HTTP client")
        self._client.close()
