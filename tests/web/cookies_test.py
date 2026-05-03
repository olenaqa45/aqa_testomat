import os

import pytest
from playwright.sync_api import Browser, expect

from tests.fixtures.cookie_helper import get_cookie, get_cookies, remove_cookie
from web.app import App


class TestEnterpriseCookies:
    """Verify cookies exist after enterprise login."""

    def test_session_cookie_exists(self, storage_state: str):
        cookie = get_cookie(storage_state, "_backend_session")
        assert cookie is not None

    def test_session_cookie_is_httponly(self, storage_state: str):
        cookie = get_cookie(storage_state, "_backend_session")
        assert cookie["httpOnly"] is True

    def test_company_id_is_set(self, storage_state: str):
        cookie = get_cookie(storage_state, "company_id")
        assert cookie is not None
        assert cookie["value"] != ""

    def test_cookies_have_correct_domain(self, storage_state: str):
        app_cookies = [c for c in get_cookies(storage_state) if c["domain"] == "app.testomat.io"]
        assert len(app_cookies) >= 2


class TestEnterpriseVsFreeCookies:
    """Compare enterprise and free plan cookies."""

    def test_enterprise_has_company_id(self, storage_state: str):
        cookie = get_cookie(storage_state, "company_id")
        assert cookie["value"] != ""

    def test_free_has_empty_company_id(self, free_storage_state: str):
        cookie = get_cookie(free_storage_state, "company_id")
        assert cookie["value"] == ""

    def test_both_have_session_cookie(self, storage_state: str, free_storage_state: str):
        assert get_cookie(storage_state, "_backend_session") is not None
        assert get_cookie(free_storage_state, "_backend_session") is not None

    def test_sessions_are_different(self, storage_state: str, free_storage_state: str):
        enterprise_session = get_cookie(storage_state, "_backend_session")["value"]
        free_session = get_cookie(free_storage_state, "_backend_session")["value"]
        assert enterprise_session != free_session


class TestCookieManipulation:
    """Test that removing cookies affects app behavior."""

    def test_removing_session_cookie_requires_reauth(self, browser: Browser, storage_state: str):
        modified_state = remove_cookie(storage_state, "_backend_session")
        context = browser.new_context(
            base_url=os.getenv("BASE_APP_URL"),
            viewport={"width": 1920, "height": 1080},
            storage_state=modified_state,
        )
        page = context.new_page()
        app = App(page)
        app.projects_page.open()
        expect(app.login_page.page.locator("input[type='email']")).to_be_visible()
        page.close()
        context.close()
        os.unlink(modified_state)
