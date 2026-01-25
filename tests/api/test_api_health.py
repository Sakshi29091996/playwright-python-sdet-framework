import pytest
from playwright.sync_api import APIRequestContext, sync_playwright

def test_api_health():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get("https://api.github.com")

        assert response.status == 200
