from __future__ import annotations

from pydantic import BaseModel, Field


class ProjectAttributes(BaseModel):
    title: str
    tests_count: int | None = Field(None, alias="tests-count")


class Project(BaseModel):
    id: str
    attributes: ProjectAttributes
