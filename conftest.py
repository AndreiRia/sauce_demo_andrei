from collections.abc import Iterator

import pytest
from config.settings import settings
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance) -> Iterator[Browser]:
    browser_type = getattr(playwright_instance, settings.browser_type)
    browser = browser_type.launch(headless=settings.headless, slowMo=settings.slow_mo)
    yield browser
    browser.close()

@pytest.fixture
def context(browser) -> Iterator[BrowserContext]:
    context = browser.new_context(
        base_url=settings.base_url,
        viewport ={"width": 1920, "height": 1080}
    )
    context.set_default_timeout(settings.timeout)
    yield context
    context.close()

@pytest.fixture
def page(context) -> Iterator[Page]:
    page = context.new_page()
    yield page
    page.close()






