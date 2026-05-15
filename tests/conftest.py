import pytest

pytest_plugins = [
    "tests.fixtures.config",
    "tests.fixtures.playwright",
    "tests.fixtures.app",
    "tests.fixtures.api",
]


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
