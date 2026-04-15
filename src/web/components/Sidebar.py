from os import link
from typing import Self

from playwright.sync_api import Page, expect


class Sidebar:
    def __init__(self, page: Page):
        self.page = page
        self._container = page.locator(".mainnav-menu")

        # Locators
        self.logo_link = self._container.locator("a.logo-full")
        self.close_btn = self._container.locator("button.btn-close")
        self.open_btn = page.locator("button.btn-open")

        self.tests_link = self._container.get_by_role("link", name="Tests")
        self.requirements_link = self._container.get_by_role("link", name="Requirements")
        self.runs_link = self._container.get_by_role("link", name="Runs")
        self.plans_link = self._container.get_by_role("link", name="Plans")
        self.steps_link = self._container.get_by_role("link", name="Steps")
        self.pulse_link = self._container.get_by_role("link", name="Pulse")
        self.imports_link = self._container.get_by_role("link", name="Imports")
        self.analytics_link = self._container.get_by_role("link", name="Analytics")
        self.branches_link = self._container.get_by_role("link", name="Branches")
        self.settings_link = self._container.get_by_role("link", name="Settings")

        self.help_link = self._container.get_by_role("link", name="Help")
        self.projects_link = self._container.get_by_role("link", name="Projects")
        self.user_profile_link = self._container.get_by_role("link", name="Олена")

    def open(self) -> Self:
        self.open_btn.click(force=True)
        expect(self.page.locator(".mainnav-menu-expanded")).to_be_visible()
        return self

    def is_loaded(self) -> Self:
        expect(self.tests_link).to_be_visible()
        expect(self.requirements_link).to_be_visible()
        expect(self.runs_link).to_be_visible()
        expect(self.plans_link).to_be_visible()
        expect(self.steps_link).to_be_visible()
        expect(self.pulse_link).to_be_visible()
        expect(self.imports_link).to_be_visible()
        expect(self.analytics_link).to_be_visible()
        expect(self.branches_link).to_be_visible()
        expect(self.settings_link).to_be_visible()
        expect(self.help_link).to_be_visible()
        expect(self.projects_link).to_be_visible()
        return self

    def click_logo(self) -> Self:
        self.logo_link.click()
        return self
