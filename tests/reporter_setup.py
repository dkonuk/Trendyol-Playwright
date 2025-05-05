import pytest
from playwright.sync_api import Page
import os
from xdist.plugin import worker_id



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if test failed and we're in the call phase
    if report.when == "call" and report.failed:
        # Get page fixture if it exists
        page = None
        for fixture_name in item.fixturenames:
            if fixture_name == "page":
                page = item.funcargs[fixture_name]
                break

        if page and isinstance(page, Page):
            # Create screenshots directory if it doesn't exist
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            #Get test name and add worker ID to filename for xdist compatibility
            worker_id = getattr(item.config, "workerinput", {}).get("workerid", '')
            test_name = f"{worker_id}_{item.nodeid.replace("/", "_").replace(":", "_")}"

            # Take screenshot
            page.screenshot(path=f"{screenshots_dir}/{test_name}.png")
            print(f"Screenshot saved to {screenshots_dir}")


