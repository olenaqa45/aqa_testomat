from typing import Self

from playwright.sync_api import Page, expect

from web.components.sidebar import Sidebar


class ProjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.side_bar = Sidebar(page)

        # Locators
        self.sticky_header = page.locator(".sticky-header")
        self.nav_menu = page.locator(".mainnav-menu")
        self.first_suite_input = page.locator("[placeholder = 'First Suite']")
        self.suite_btn = page.get_by_role("button", name="Suite")
        self.project_name = page.locator(".sticky-header h2")
        self.close_readme_left_btn = page.locator(".back .third-btn")
        self.close_readme_right_btn = page.locator(".detail-view-header-wrapper .third-btn")
        self.edit_readme_btn = page.locator(".detail-view-header-wrapper .ember-view")

    def should_be_loaded(self) -> Self:
        expect(self.sticky_header).to_be_visible()
        expect(self.nav_menu).to_be_visible()
        expect(self.first_suite_input).to_be_visible()
        expect(self.suite_btn).to_be_visible()
        return self

    def empty_project_name_is(self, expected_project_name: str) -> Self:
        expect(self.project_name).to_have_text(expected_project_name)
        return self

    def close_read_me_left(self) -> Self:
        expect(self.close_readme_left_btn).to_be_visible()
        self.close_readme_left_btn.click()
        return self

    def close_read_me_right(self) -> Self:
        expect(self.close_readme_right_btn).to_be_visible()
        self.close_readme_right_btn.click()
        return self

    def edit_read_me(self) -> Self:
        expect(self.edit_readme_btn).to_be_visible()
        return self
