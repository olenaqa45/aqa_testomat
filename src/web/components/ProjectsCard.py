from enum import Enum

from playwright.sync_api import Page, expect


# AI generated
class ProjectCard:

    def __init__(self, page: Page, name: str):
        self.page = page
        self._card = page.locator(f'#content-desktop #grid li a[title="{name}"]')

    def click(self):
        self._card.click()

    def get_test_count_text(self) -> str:
        return self._card.locator("p").inner_text()

    def get_badge(self) -> str:
        return self._card.locator(".common-badge").inner_text()

    def is_visible(self):
        expect(self._card).to_be_visible()

    def get_name(self) -> str:
        return self._card.get_attribute("title")

    def focus(self):
        self._card.scroll_into_view_if_needed()
        self._card.hover()


class Badges(Enum):
    DEMO = "Demo"
    CLASSICAL = "Classical"
    TEST = "Test"
