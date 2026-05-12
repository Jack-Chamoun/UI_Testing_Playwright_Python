import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.set_default_timeout(10000)

        yield page

        browser.close()