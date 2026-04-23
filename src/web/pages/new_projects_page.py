from typing import Self

from playwright.sync_api import Page, expect

from web.pages.project_page import ProjectPage


class NewProjectsPage:
    def __init__(self, page: Page):
        self.page = page
        self._container = page.locator("#content-desktop")
        self._form = self._container.locator("form#new_project")

        # Locators
        self.page_title = self._container.locator(".common-page-header h2")
        self.classical_btn = self._form.locator("#classical")
        self.bdd_btn = self._form.locator("#bdd")
        self.project_title_input = self._form.locator("#project_title")
        self.demo_btn = self._form.locator("#demo-btn")
        self.create_btn = self._form.locator('#project-create-btn input[type="submit"]')
        self.create_demo_btn = self._container.locator('form[action="/projects/create_demo"] input[type="submit"]')
        self.how_to_start_link = self._container.locator("a", has_text="How to start?")

    def open(self) -> Self:
        self.page.goto("/projects/new")
        return self

    def should_be_loaded(self) -> Self:
        expect(self.page_title).to_have_text("New Project")
        expect(self._form).to_be_visible()
        expect(self.classical_btn).to_be_visible()
        expect(self.bdd_btn).to_be_visible()
        expect(self.project_title_input).to_be_visible()
        expect(self.demo_btn).to_be_visible()
        expect(self.create_btn).to_be_visible()
        return self

    def select_classical(self) -> Self:
        self.classical_btn.click()
        return self

    def select_bdd(self) -> Self:
        self.bdd_btn.click()
        return self

    def fill_project_title(self, title: str) -> Self:
        self.project_title_input.fill(title)
        return self

    def toggle_demo_data(self) -> Self:
        self.demo_btn.click()
        return self

    def select_demo_project(self, name: str) -> Self:
        self._container.locator("#demo-form button", has_text=name).click()
        return self

    def click_create(self) -> ProjectPage:
        self.create_btn.click()
        return ProjectPage(self.page)

    def click_create_demo(self) -> Self:
        self.create_demo_btn.click()
        return self

    def click_how_to_start(self) -> Self:
        self.how_to_start_link.click()
        return self
