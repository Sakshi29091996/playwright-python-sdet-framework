import json
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def config():
    with open("config/config.json") as f:
        return json.load(f)

@pytest.fixture
def page(config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config["headless"])
        context = browser.new_context()
        page = context.new_page()
        page.goto(config["base_url"])
        yield page
        browser.close()
