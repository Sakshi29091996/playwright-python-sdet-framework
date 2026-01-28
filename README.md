# playwright-python-sdet-framework

Senior SDET-style Playwright + Python automation framework demonstrating Page Object Model (POM), PyTest, config management, and reporting.

---

## Overview

This repository is a small, practical example automation framework using Playwright for Python and PyTest. It demonstrates:

- A simple Page Object Model (POM) structure for UI tests
- Separation of UI and API tests
- Centralized configuration management
- Minimal, reproducible test commands and environment setup

Use it as a learning reference or a lightweight starting point for building larger test suites.

## Features

- Playwright-powered browser automation for UI tests
- PyTest test runner with conventional test layout
- Example API health test
- Example UI login test following POM
- Config stored under `config/config.json`

## Prerequisites

- Python 3.8+
- Git (optional)
- Windows / macOS / Linux

Make sure you have Python available on your PATH and pip installed.

## Installation

1. Create and activate a virtual environment (recommended):

   python -m venv .venv
   .venv\Scripts\Activate.ps1  # PowerShell on Windows

2. Install dependencies:

   pip install -r requirements.txt

3. Install Playwright browsers (required for UI tests):

   python -m playwright install

## Running tests

From the repository root:

- Run the full test suite (UI + API):

  pytest -q

- Run only UI tests:

  pytest tests/ui -q

- Run only API tests:

  pytest tests/api -q

Add `-k` or markers as needed to select specific tests.

If you need more verbosity or reporting, pass additional pytest flags (for example `-vv` or `--maxfail=1`).

## Configuration

Project configuration is stored in `config/config.json`. Tests and page objects read values from this file (for example: base URLs, credentials, timeouts). Update that file to point tests at the correct environment.

## Project structure

- `config/` - JSON configuration used by tests
- `pages/`  - Page Object Model classes for UI pages
- `tests/ui/` - UI test cases
- `tests/api/` - API test cases
- `utils/` - shared helpers and base test classes
- `requirements.txt` - Python dependencies
- `pytest.ini` - pytest configuration

## How to add tests

- UI: Add a new Page class under `pages/` for the page under test, and then create a PyTest test file under `tests/ui/` that uses the page object and fixtures from `utils/`.
- API: Add new test modules under `tests/api/` that use `requests` (or httpx) to call endpoints and assert responses.

## Contribution

Contributions are welcome. Open an issue or a PR with a clear description of the change. Keep tests fast and deterministic where possible.

## License

This repository is provided as an example. No license specified - add one if you plan to reuse or publish this code.

---

Happy testing!
