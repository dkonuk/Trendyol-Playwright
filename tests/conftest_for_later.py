import pytest
import json
from playwright.sync_api import sync_playwright
from os import path

#Read config based on enviroment
def read_config(env="dev"):
    config_path = path.join(path.dirname(path.abspath(__file__)),
                            f"../config/{env}.json")
    with open(config_path) as config_file:
        return json.load(config_file)


# Browser fixture
@pytest.fixture(scope="session")
def browser_type(playwright):
    config = read_config()
    browser_name = config.get("browser", "chromium")

    if browser_name.lower() == "chromium":
        return playwright.chromium
    elif browser_name.lower() == "firefox":
        return playwright.firefox
    elif browser_name.lower() == "webkit":
        return playwright.webkit
    else:
        return playwright.chromium

@pytest.fixture
def browser(browser_type):
    browser = browser_type.launch(headless=False,
    slow_mo = 100
    )
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir="videos/"
    )
    page = context.new_page()
    yield page
    context.close()