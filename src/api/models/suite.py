from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from api.models.test import LabelAttachment, LinkAction


class SuiteType(Enum):
    suite = "suite"


class SourceType(Enum):
    jira = "jira"
    confluence = "confluence"
    file = "file"
    text = "text"


class LinkedRequirement(BaseModel):
    id: str | None = Field(None, description="ID (8-char)")
    title: str | None = None
    source_type: SourceType | None = None
    global_: bool | None = Field(
        None,
        alias="global",
        description="True if this is a global (project-lev el) requirement",
    )


class SuiteChildInput(BaseModel):
    title: str
    description: str | None = None
    emoji: str | None = None
    children: list[SuiteChildInput] | None = Field(None, description="Nested child suites (recursive)")


class Suite(BaseModel):
    id: str | None = Field(None, description="Public UID")
    type: SuiteType | None = None
    title: str | None = None
    emoji: str | None = None
    public_title: str | None = None
    is_shared: bool | None = None
    file_type: str | None = Field(None, description="Auto-detected: 'folder' if suite has children, 'file' otherwise")
    test_count: int | None = None
    assigned_to: str | None = None
    clean_title: str | None = None
    tags: list[str] | None = None
    sync: bool | None = None
    description: str | None = None
    file: str | None = Field(None, description="File path associated with this suite")
    parent_id: str | None = Field(None, description="Public UID of the parent suite, or null for root suites")
    labels: list[LabelAttachment] | None = None
    requirements: list[LinkedRequirement] | None = Field(
        None, description="Attached and global requirements for this suite"
    )
    children: list[Suite] | None = Field(
        None, description="Nested child suites (present in tree responses when children exist)"
    )


class SuiteInput(BaseModel):
    title: str
    description: str | None = None
    emoji: str | None = None
    parent_id: str | None = Field(None, description="Public UID of the parent suite")
    file_type: str | None = Field(
        None, description="Auto-detected from children: 'folder' if children provided, 'file' otherwise."
    )
    assigned_to: str | None = Field(None, description="Email address of a non-readonly project member to assign.")
    file: str | None = Field(
        None, description="File path to associate with the suite. Only applicable when file_type is 'file'."
    )
    children: list[SuiteChildInput] | None = Field(None, description="Nested child suites to create recursively.")
    link: list[LinkAction] | None = Field(None, description="Add/remove labels, tags, issues, or jira links")
