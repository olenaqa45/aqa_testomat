from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class Type(Enum):
    test = "test"


class Priority(Enum):
    low = "low"
    normal = "normal"
    important = "important"
    high = "high"
    critical = "critical"
    none_type_none = None


class Action(Enum):
    add = "add"
    remove = "remove"


class LinkType(Enum):
    label = "label"
    custom_field = "custom_field"
    tag = "tag"
    milestone = "milestone"
    issue = "issue"
    jira = "jira"
    requirement = "requirement"


class LabelAttachment(BaseModel):
    id: str | None = Field(None, description="Label slug")
    title: str | None = None
    color: str | None = None
    position: int | None = None
    visibility: str | None = None
    list: bool | None = None
    value: str | None = Field(None, description="Custom field value (if label has a field type)")
    short: str | None = Field(None, description="Short display format for the field")


class LinkAction(BaseModel):
    action: Action
    type: LinkType
    value: str | None = Field(
        None,
        description="Meaning depends on type: label slug, tag name, milestone slug, issue URL, jira key, requirement ID",
    )


class Test(BaseModel):
    id: str | None = Field(None, description='Public UID (e.g. "@Txxxxx")')
    type: Type | None = None
    title: str | None = None
    emoji: str | None = None
    state: str | None = None
    is_shared: bool | None = None
    assigned_to: str | None = None
    priority: Priority | None = None
    public_title: str | None = None
    clean_title: str | None = None
    self_tags: list[str] | None = None
    sync: bool | None = None
    code: str | None = None
    description: str | None = None
    position: int | None = None
    suite_id: str | None = Field(None, description="Public UID of the parent suite")
    labels: list[LabelAttachment] | None = None


class TestInput(BaseModel):
    title: str
    description: str | None = None
    emoji: str | None = None
    suite_id: str = Field(..., description="Public UID of the parent suite")
    priority: Priority | None = None
    assigned_to: str | None = Field(
        None, description="Email address of a non-readonly project member to assign."
    )
    code: str | None = None
    state: str | None = None
    link: list[LinkAction] | None = Field(
        None, description="Add/remove labels, tags, issues, or jira links"
    )
