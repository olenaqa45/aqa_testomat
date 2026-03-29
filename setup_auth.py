from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        channel="chrome"
    )
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://app.testomat.io/users/sign_in")
    input("Залогінься вручну в браузері, потім натисни Enter тут...")
    context.storage_state(path="auth_state.json")
    browser.close()
