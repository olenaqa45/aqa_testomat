from typing import Self

import allure
from playwright.sync_api import Page, expect


class ProjectCard:
    def __init__(self, page: Page, name: str):
        self.page = page
        self._card = page.locator(f'#content-desktop #grid li a[title="{name}"]')

        # Locators
        self.test_count = self._card.locator("p")
        self.badge = self._card.locator(".common-badge")

    @allure.step("Click project card")
    def click(self) -> Self:
        self._card.click()
        return self

    @allure.step("Get test count text")
    def get_test_count_text(self) -> str:
        return self.test_count.inner_text()

    @allure.step("Get badge text")
    def get_badge(self) -> str:
        return self.badge.inner_text()

    @allure.step("Verify project card is visible")
    def is_visible(self) -> Self:
        expect(self._card).to_be_visible()
        return self

    @allure.step("Get project card name")
    def get_name(self) -> str:
        return self._card.get_attribute("title")

    @allure.step("Focus project card")
    def focus(self) -> Self:
        self._card.scroll_into_view_if_needed()
        self._card.hover()
        return self
