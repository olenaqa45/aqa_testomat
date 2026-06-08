from __future__ import annotations

from api.controllers.base_controller import BaseController


class ProjectController(BaseController):
    BASE_PATH = "projects"

    @property
    def _path(self) -> str:
        return "/api/projects"

    def _resource_path(self, resource_id: str) -> str:
        return f"/api/projects/{resource_id}"
