from __future__ import annotations

import httpx
from pydantic import ValidationError

from api.controllers.base_controller import BaseController
from api.models.test import TestInput


class TestController(BaseController):
    BASE_PATH = "tests"

    def create_test(self, test_input: TestInput | dict) -> httpx.Response:
        data = self._validate(test_input, TestInput)
        return self.create(data)

    def update_test(self, test_id: str, test_input: TestInput | dict) -> httpx.Response:
        data = self._validate(test_input, TestInput)
        return self.update(test_id, data)

    @staticmethod
    def _validate(data: TestInput | dict, model: type[TestInput]) -> dict:
        if isinstance(data, dict):
            data = model.model_validate(data)
        return data.model_dump(exclude_none=True)
