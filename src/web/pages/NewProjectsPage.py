from typing import Self

from playwright.sync_api import Page, expect

from web.pages.NewProject import NewProject


class NewProjectsPage:
    def __init__(self, page: Page):
        self.page = page
        self._container = page.locator("#content-desktop")
        self._form = self._container.locator("form#new_project")

    def open(self) -> Self:
        self.page.goto("/projects/new")
        return self

    def is_loaded(self) -> Self:
        expect(self._container.locator(".common-page-header h2")).to_have_text("New Project")
        expect(self._form).to_be_visible()
        expect(self._form.locator("#classical")).to_be_visible()
        expect(self._form.locator("#bdd")).to_be_visible()
        expect(self._form.locator("#project_title")).to_be_visible()
        expect(self._form.locator("#demo-btn")).to_be_visible()
        expect(self._form.locator("#project-create-btn")).to_be_visible()
        return self

    def select_classical(self) -> Self:
        self._form.locator("#classical").click()
        return self

    def select_bdd(self) -> Self:
        self._form.locator("#bdd").click()
        return self

    def fill_project_title(self, title: str) -> Self:
        self._form.locator("#project_title").fill(title)
        return self

    def toggle_demo_data(self) -> Self:
        self._form.locator("#demo-btn").click()
        return self

    def select_demo_project(self, name: str) -> Self:
        self._container.locator("#demo-form button", has_text=name).click()
        return self

    def click_create(self) -> Self:
        self._form.locator('#project-create-btn input[type="submit"]').click()
        return NewProject(self.page)

    def click_create_demo(self) -> Self:
        self._container.locator('form[action="/projects/create_demo"] input[type="submit"]').click()
        return self

    def click_how_to_start(self) -> Self:
        self._container.locator("a", has_text="How to start?").click()
        return self
