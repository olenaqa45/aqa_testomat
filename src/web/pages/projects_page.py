from typing import Self

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
        self.project_names = self._container.locator("#grid li h3")
        self.search_input = self._container.locator('input#search[name="search"]')
        self.project_items = self._container.locator("#grid li").locator("visible=true")
        self.create_btn = self._container.locator('a[href="/projects/new"]')
        self.grid_view_btn = self._container.locator("#grid-view")
        self.table_view_btn = self._container.locator("#table-view")

    def open(self) -> Self:
        self.page.goto("/")
        return self

    def should_be_loaded(self) -> Self:
        expect(self.page_title).to_have_text("Projects")
        return self

    def flash_message_visible(self, text: str = "Signed in successfully") -> Self:
        expect(self.flash_success.filter(has_text=text)).to_be_visible()
        return self

    def select_projects_name(self, projects_name: str) -> Self:
        self.company_select.click()
        self.company_select.select_option(label=projects_name)
        return self

    def enterprise_plan_is_visible(self, plan_name: str) -> Self:
        expect(self.plan_tooltip.filter(has_text=plan_name)).to_be_visible()
        return self

    def get_project_names(self) -> list[str]:
        return self.project_names.all_inner_texts()

    def search_project(self, name: str) -> Self:
        self.search_input.fill(name)
        return self

    def count_of_project_visible(self, expected: int) -> Self:
        expect(self.project_items).to_have_count(expected)
        return self

    def get_project_card(self, name: str) -> ProjectCard:
        return ProjectCard(self.page, name)

    def click_create(self) -> Self:
        self.create_btn.click()
        return self

    def switch_to_grid_view(self) -> Self:
        self.grid_view_btn.click()
        return self

    def switch_to_table_view(self) -> Self:
        self.table_view_btn.click()
        return self
