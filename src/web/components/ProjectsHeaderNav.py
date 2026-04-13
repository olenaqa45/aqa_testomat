from playwright.sync_api import Page, expect


# AI generated
class HeaderNav:

    def __init__(self, page: Page):
        self.page = page
        self._nav = page.locator("#content-desktop .auth-header-nav")

    def click_dashboard(self):
        self._nav.locator('.auth-header-nav-left-items a[href="/"]').click()

    def click_companies(self):
        self._nav.locator('a[href="/companies"]').click()

    def open_analytics_dropdown(self):
        self._nav.locator("#analytics-dropdown-toggle").click()

    def click_analytics(self):
        self.open_analytics_dropdown()
        self._nav.locator('#analytics-dropdown-menu a[href="/analytics"]').click()

    def click_dashboards(self):
        self.open_analytics_dropdown()
        self._nav.locator('#analytics-dropdown-menu a[href="/analytics/dashboards"]').click()

    def click_docs(self):
        self._nav.locator('a[href="https://docs.testomat.io"]').click()

    def click_changelog(self):
        self._nav.locator('a[href="https://changelog.testomat.io"]').click()

    def click_public_api(self):
        self._nav.locator('a[href="/docs/openapi"]').click()

    def click_create_project(self):
        self._nav.locator('a[href="/projects/new"]').click()

    def click_global_search(self):
        self._nav.locator("#showGlobalSearchBtn").click()

    def is_trial_visible(self):
        expect(self._nav.locator('a[href="/trials"]')).to_be_visible()

    def get_trial_text(self) -> str:
        return self._nav.locator('a[href="/trials"]').inner_text()
