# AQA Testomat

UI test automation framework for [Testomat.io](https://testomat.io) built with Python, Playwright, and pytest.

## Tech Stack

- Python 3.14
- Playwright 1.58
- pytest 9.0
- Faker (test data generation)
- python-dotenv (environment config)
- uv (package manager)
- Ruff (linter & formatter)

## Project Structure

```
aqa_testomat/
├── src/web/
│   ├── app.py                      # App facade — single entry point to all pages
│   ├── pages/
│   │   ├── home_page.py            # Marketing site (testomat.io)
│   │   ├── login_page.py           # Login page
│   │   ├── projects_page.py        # Projects list page
│   │   ├── new_projects_page.py    # New project creation form
│   │   └── project_page.py         # Single project view
│   └── components/
│       ├── sidebar.py              # Navigation sidebar
│       ├── projects_card.py        # Project card component
│       ├── profile_menu.py         # User profile dropdown
│       └── header_nav.py           # Top navigation bar
├── tests/
│   ├── conftest.py                 # Registers fixture plugins
│   ├── fixtures/
│   │   ├── config.py               # Config dataclass & configs fixture
│   │   ├── playwright.py           # Browser, storage states, context, page fixtures
│   │   └── app.py                  # App fixtures (logged_app, free_project_app)
│   ├── web/
│   │   ├── login_page_test.py      # Login page tests (valid/invalid/UI)
│   │   ├── enterprise_plan_tests/
│   │   │   ├── projects_page_test.py    # Enterprise projects page tests
│   │   │   ├── project_creation_test.py # Project creation flow
│   │   │   └── switch_company_test.py   # Company switching tests
│   │   └── free_plan_tests/
│   │       └── free_plan_test.py        # Free plan tests
│   ├── login_and_projects_test.py  # Legacy login & project search tests
│   └── homepage_test.py            # Marketing site tests
├── pyproject.toml                  # Project config, dependencies, pytest & ruff settings
└── .env                            # Environment variables (not committed)
```

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (package manager)
- Git

### Installation

```bash
git clone <repo-url>
cd aqa_testomat

uv sync
uv run playwright install chromium
```

### Environment Variables

Create a `.env` file in the project root:

```
BASE_URL=https://testomat.io
BASE_APP_URL=https://app.testomat.io
EMAIL=your_email
PASSWORD=your_password
```

## Running Tests

```bash
# Run all tests
pytest

# Run by marker
pytest -m smoke
pytest -m regression

# Run a specific file
pytest tests/web/login_page_test.py

# Run a single test
pytest tests/web/login_page_test.py::test_login_invalid

# Run enterprise plan tests
pytest tests/web/enterprise_plan_tests/

# Run free plan tests
pytest tests/web/free_plan_tests/

# Rerun last failed
pytest --lf

# Run failed first, then the rest
pytest --ff

# Stop on first failure
pytest -x

# Run headless
pytest --headless
```

## Test Markers

| Marker       | Description               |
|--------------|---------------------------|
| `smoke`      | Quick critical path tests |
| `regression` | Full regression suite     |

## Architecture

The project follows the **Page Object Model** pattern:

- **Pages** encapsulate page-specific locators and actions
- **Components** represent reusable UI elements (sidebar, nav, cards)
- **App** facade provides a single entry point: `app.login_page.open().should_be_loaded()`
- All page object methods return `Self` for **method chaining**

### Fixtures

Fixtures are split into three files under `tests/fixtures/`:

**config.py** — configuration

| Fixture   | Scope   | Description                              |
|-----------|---------|------------------------------------------|
| `configs` | session | Loads env vars into a `Config` dataclass |

**playwright.py** — browser & auth

| Fixture              | Scope    | Description                                              |
|----------------------|----------|----------------------------------------------------------|
| `browser`            | session  | Launches Chromium                                        |
| `storage_state`      | session  | Logs in once, saves enterprise session to disk           |
| `free_storage_state` | session  | Switches to Free Projects company, saves session to disk |
| `context`            | function | Fresh unauthenticated browser context                    |
| `page`               | function | New page from unauthenticated context                    |

**app.py** — app instances

| Fixture            | Scope    | Description                                 |
|--------------------|----------|---------------------------------------------|
| `app`              | function | `App` instance (unauthenticated)            |
| `logged_app`       | function | `App` instance with enterprise auth session |
| `free_project_app` | function | `App` instance with free plan auth session  |

## Test Reports

On failure, Playwright captures:

- **Traces** → `test-result/traces/`
- **Screenshots** → `test-result/traces/`
- **HTML report** → `test-result/report.html`
