from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Generator

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

from utils.test_data import load_test_data

load_dotenv()
ROOT = Path(__file__).parent
SCREENSHOTS = ROOT / "screenshots"
REPORTS = ROOT / "reports"


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://parabank.parasoft.com/parabank").rstrip("/")


@pytest.fixture(scope="session")
def test_data() -> dict[str, Any]:
    return load_test_data()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    return {
        **browser_context_args,
        "base_url": os.getenv("BASE_URL", "https://parabank.parasoft.com/parabank").rstrip("/"),
        "viewport": {"width": 1440, "height": 1000},
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict) -> dict:
    return {
        **browser_type_launch_args,
        "headless": os.getenv("HEADLESS", "false").lower() not in {"0", "false", "no"},
        "slow_mo": int(os.getenv("SLOW_MO", "0")),
    }


@pytest.fixture(autouse=True)
def configure_page(page: Page) -> Generator[None, None, None]:
    page.set_default_timeout(int(os.getenv("DEFAULT_TIMEOUT_MS", "10000")))
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    page = item.funcargs.get("page")
    if page is None:
        return
    path = save_screenshot(page, f"FAILED_{item.name}")
    try:
        from pytest_html import extras
        report.extras = getattr(report, "extras", [])
        report.extras.append(extras.image(str(path)))
    except ImportError:
        pass


def save_screenshot(page: Page, name: str) -> Path:
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    path = SCREENSHOTS / f"{name}.png"
    page.screenshot(path=str(path), full_page=True)
    return path
