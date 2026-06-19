from typing import Self

import allure
from playwright.sync_api import Page, expect

from web.components.projects_card import ProjectCard


class ProjectsPage:
    def __init__(self, page: Page):
        self.page = page
        self._container = page.locator("#content-desktop #container")
        self._header = page.locator("#content-desktop .common-page-header-left")

        # Locators
        self.page_title = self._container.locator(".common-page-header h2")
        self.flash_success = self._container.locator(".common-flash-success")
        self.company_select = self._header.locator("#company_id")
        self.plan_tooltip = self._header.locator(".tooltip-project-plan")
        self.enterprise_plan_label = self._container.get_by_text("Enterprise Plan")
        self.free_plan_label = self._container.get_by_text("Free Plan")
        self.project_names = self._container.locator("#grid li h3")
        self.search_input = self._container.locator('input#search[name="search"]')
        self.project_items = self._container.locator("#grid li").locator("visible=true")
        self.create_btn = self._container.locator('a[href="/projects/new"]')
        self.grid_view_btn = self._container.locator("#grid-view")
        self.table_view_btn = self._container.locator("#table-view")

    @allure.step("Open projects page")
    def open(self) -> Self:
        self.page.goto("/")
        return self

    @allure.step("Verify projects page is loaded")
    def should_be_loaded(self) -> Self:
        expect(self.page_title).to_have_text("Projects")
        return self

    @allure.step("Verify flash message: {text}")
    def flash_message_visible(self, text: str = "Signed in successfully") -> Self:
        expect(self.flash_success.filter(has_text=text)).to_be_visible()
        return self

    @allure.step("Select projects: {projects_name}")
    def select_projects_name(self, projects_name: str) -> Self:
        self.company_select.click()
        self.company_select.select_option(label=projects_name)
        return self

    @allure.step("Hover plan tooltip")
    def hover_plan_tooltip(self) -> Self:
        self.plan_tooltip.hover(timeout=5000)
        return self

    @allure.step("Verify enterprise plan is visible: {plan_name}")
    def enterprise_plan_is_visible(self, plan_name: str) -> Self:
        expect(self.plan_tooltip.filter(has_text=plan_name)).to_be_visible()
        return self

    @allure.step("Get project names")
    def get_project_names(self) -> list[str]:
        return self.project_names.all_inner_texts()

    @allure.step("Search project: {name}")
    def search_project(self, name: str) -> Self:
        self.search_input.fill(name)
        return self

    @allure.step("Verify {expected} projects visible")
    def count_of_project_visible(self, expected: int) -> Self:
        expect(self.project_items).to_have_count(expected)
        return self

    @allure.step("Get project card: {name}")
    def get_project_card(self, name: str) -> ProjectCard:
        return ProjectCard(self.page, name)

    @allure.step("Click create project")
    def click_create(self) -> Self:
        self.create_btn.click()
        return self

    @allure.step("Switch to grid view")
    def switch_to_grid_view(self) -> Self:
        self.grid_view_btn.click()
        return self

    @allure.step("Switch to table view")
    def switch_to_table_view(self) -> Self:
        self.table_view_btn.click()
        return self
