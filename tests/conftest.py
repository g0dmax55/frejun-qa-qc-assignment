import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage  # Ensure this import is available

# Fixture for initializing Playwright session, shared across the entire test session
@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

# Fixture for launching a browser instance, shared across the entire test session
@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)  # Set to True to run in headless mode
    yield browser
    browser.close()

# Fixture for creating a new page in the browser context for each test function
@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

# Fixture for creating a new page in the browser context for each test function
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

# Fixture to obtain the base URL from pytest configuration for easy reference
@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini('base_url')

# Fixture to set up the page by navigating to the base URL and performing login
@pytest.fixture(scope="function")
def setup_page(page, base_url):
    # Instantiate and use the LoginPage
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    # Ensure successful navigation to inventory page
    assert "inventory.html" in page.url
    
    yield page

# Fixture for accessing the inventory page functionality after login
@pytest.fixture
def inventory_page(setup_page):
    # setup_page already logs in and navigates to the inventory page
    inventory_page = InventoryPage(setup_page)
    yield inventory_page

# Fixture for accessing the checkout page functionality
@pytest.fixture
def checkout_page(setup_page):
    # Instantiate the CheckoutPage using the page from setup_page
    checkout_page = CheckoutPage(setup_page)
    yield checkout_page
