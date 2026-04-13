from playwright.sync_api import Page, expect

from web.components.ProjectsCard import ProjectCard


# AI generated
class ProjectsPage:

    def __init__(self, page: Page):
        self.page = page
        self._container = page.locator("#content-desktop #container")
        self._header = page.locator("#content-desktop .common-page-header-left")

    def is_loaded(self):
        expect(self._container.locator(".common-page-header h2")).to_have_text("Projects")

    def flash_message_visible(self, text: str = "Signed in successfully"):
        expect(self._container.locator(".common-flash-success", has_text=text)).to_be_visible()

    def select_projects_name(self, projects_name: str):
        (self._header.locator("#company_id")).click()
        (self._header.locator("#company_id").select_option(label=projects_name))

    def enterprise_plan_is_visible(self, plan_name: str):
        expect(self._header.locator(".tooltip-project-plan", has_text=plan_name)).to_be_visible()

    def get_project_names(self):
        return self._container.locator("#grid li h3").all_inner_texts()

    def search_project(self, name: str):
        self._container.locator('input#search[name="search"]').fill(name)

    def count_of_project_visible(self, expected: int):
        assert self._container.locator("#grid li:visible").count() == expected

    def get_project_card(self, name: str) -> ProjectCard:
        return ProjectCard(self.page, name)

    def click_create(self):
        self._container.locator('a[href="/projects/new"]').click()

    def switch_to_grid_view(self):
        self._container.locator("#grid-view").click()

    def switch_to_table_view(self):
        self._container.locator("#table-view").click()
