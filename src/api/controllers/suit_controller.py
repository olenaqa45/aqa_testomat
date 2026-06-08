from __future__ import annotations

import httpx

from api.controllers.base_controller import BaseController
from api.models.suite import SuiteInput


class SuiteController(BaseController):
    BASE_PATH = "suites"

    def create_suite(self, suite_input: SuiteInput | dict) -> httpx.Response:
        data = self._validate(suite_input, SuiteInput)
        return self.create(data)

    def update_suite(self, suite_id: str, suite_input: SuiteInput | dict) -> httpx.Response:
        data = self._validate(suite_input, SuiteInput)
        return self.update(suite_id, data)

    @staticmethod
    def _validate(data: SuiteInput | dict, model: type[SuiteInput]) -> dict:
        if isinstance(data, dict):
            data = model.model_validate(data)
        return data.model_dump(exclude_none=True)
