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
│   ├── conftest.py                 # Fixtures: browser, auth, app
│   ├── web/
│   │   ├── login_page_test.py      # Login page tests (valid/invalid/UI)
│   │   ├── projects_page_test.py   # Projects page tests
│   │   └── project_creation_test.py # Project creation flow
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

| Marker       | Description                  |
|--------------|------------------------------|
| `smoke`      | Quick critical path tests    |
| `regression` | Full regression suite        |

## Architecture

The project follows the **Page Object Model** pattern:

- **Pages** encapsulate page-specific locators and actions
- **Components** represent reusable UI elements (sidebar, nav, cards)
- **App** facade provides a single entry point: `app.login_page.open().should_be_loaded()`
- All page object methods return `Self` for **method chaining**

### Fixtures

| Fixture              | Scope    | Description                                      |
|----------------------|----------|--------------------------------------------------|
| `configs`            | session  | Loads env vars into a `Config` dataclass          |
| `browser`            | session  | Launches Chromium                                 |
| `storage_state`      | session  | Authenticates once, saves session to disk          |
| `context`            | function | Fresh unauthenticated browser context              |
| `page`               | function | New page from unauthenticated context              |
| `app`                | function | `App` instance (unauthenticated)                   |
| `authenticated_app`  | function | `App` instance with saved auth session             |

## Test Reports

On failure, Playwright captures:
- **Traces** → `test-result/traces/`
- **Screenshots** → `test-result/traces/`
- **HTML report** → `test-result/report.html`
