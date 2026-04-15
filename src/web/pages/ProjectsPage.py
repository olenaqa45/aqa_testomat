from playwright.sync_api import Page, expect

from web.components.ProjectsCard import ProjectCard


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
        self.project_items = self._container.locator("#grid li")
        self.create_btn = self._container.locator('a[href="/projects/new"]')
        self.grid_view_btn = self._container.locator("#grid-view")
        self.table_view_btn = self._container.locator("#table-view")

    def is_loaded(self):
        expect(self.page_title).to_have_text("Projects")

    def flash_message_visible(self, text: str = "Signed in successfully"):
        expect(self.flash_success.filter(has_text=text)).to_be_visible()

    def select_projects_name(self, projects_name: str):
        self.company_select.click()
        self.company_select.select_option(label=projects_name)

    def enterprise_plan_is_visible(self, plan_name: str):
        expect(self.plan_tooltip.filter(has_text=plan_name)).to_be_visible()

    def get_project_names(self):
        return self.project_names.all_inner_texts()

    def search_project(self, name: str):
        self.search_input.fill(name)

    def count_of_project_visible(self, expected: int):
        expect(self.project_items).to_have_count(expected)

    def get_project_card(self, name: str) -> ProjectCard:
        return ProjectCard(self.page, name)

    def click_create(self):
        self.create_btn.click()

    def switch_to_grid_view(self):
        self.grid_view_btn.click()

    def switch_to_table_view(self):
        self.table_view_btn.click()
