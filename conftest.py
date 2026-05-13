import pytest
from playwright.sync_api import sync_playwright, expect
import os
from datetime import datetime


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.set_default_timeout(10000)

        yield page

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to inspect test result after execution.
    """
    outcome = yield
    report = outcome.get_result()

    # Only capture screenshot for actual test call failures
    if report.when == "call" and report.failed:

        # Get the Playwright page fixture
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            page.screenshot(path=file_path, full_page=True)
