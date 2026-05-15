from typing import Self

from playwright.sync_api import Page, expect


class HeaderNav:
    def __init__(self, page: Page):
        self.page = page
        self._nav = page.locator("#content-desktop .auth-header-nav")

        # Locators
        self.dashboard_link = self._nav.locator('.auth-header-nav-left-items a[href="/"]')
        self.companies_link = self._nav.locator('a[href="/companies"]')
        self.analytics_toggle = self._nav.locator("#analytics-dropdown-toggle")
        self.analytics_link = self._nav.locator('#analytics-dropdown-menu a[href="/analytics"]')
        self.dashboards_link = self._nav.locator('#analytics-dropdown-menu a[href="/analytics/dashboards"]')
        self.docs_link = self._nav.locator('a[href="https://docs.testomat.io"]')
        self.changelog_link = self._nav.locator('a[href="https://changelog.testomat.io"]')
        self.public_api_link = self._nav.locator('a[href="/docs/openapi"]')
        self.create_project_link = self._nav.locator('a[href="/projects/new"]')
        self.global_search_btn = self._nav.locator("#showGlobalSearchBtn")
        self.trial_link = self._nav.locator('a[href="/trials"]')

    def click_dashboard(self) -> Self:
        self.dashboard_link.click()
        return self

    def click_companies(self) -> Self:
        self.companies_link.click()
        return self

    def open_analytics_dropdown(self) -> Self:
        self.analytics_toggle.click()
        return self

    def click_analytics(self) -> Self:
        self.open_analytics_dropdown()
        self.analytics_link.click()
        return self

    def click_dashboards(self) -> Self:
        self.open_analytics_dropdown()
        self.dashboards_link.click()
        return self

    def click_docs(self) -> Self:
        self.docs_link.click()
        return self

    def click_changelog(self) -> Self:
        self.changelog_link.click()
        return self

    def click_public_api(self) -> Self:
        self.public_api_link.click()
        return self

    def click_create_project(self) -> Self:
        self.create_project_link.click()
        return self

    def click_global_search(self) -> Self:
        self.global_search_btn.click()
        return self

    def is_trial_visible(self) -> Self:
        expect(self.trial_link).to_be_visible()
        return self

    def get_trial_text(self) -> str:
        return self.trial_link.inner_text()
