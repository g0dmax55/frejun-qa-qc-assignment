from pages.inventory_page import InventoryPage
from pages.header_page import HeaderPage

def test_logout_functionality(setup_page):
    # Assume user is already logged in and on the inventory page
    inventory_page = InventoryPage(setup_page)
    
    # Initialize the HeaderPage
    header_page = HeaderPage(setup_page)
    
    # Perform the logout action
    header_page.logout()
    
    # Verify that the user is redirected to the login page
    # Check for the presence of the login form elements
    assert setup_page.is_visible('input[data-test="username"]')  # Check for username input
    assert setup_page.is_visible('input[data-test="password"]')  # Check for password input
    assert setup_page.is_visible('input[data-test="login-button"]')  # Check for login button

