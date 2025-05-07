import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(
        timeout=3000,
        headless=False,
        slow_mo=0)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)  # Set 5 second timeout for all actions
    yield page
    page.close()

