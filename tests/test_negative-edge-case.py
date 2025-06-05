import pytest

@pytest.mark.parametrize("username, password, expected_error", [
    ("invalid_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
    ("", "", "Epic sadface: Username is required"),
    ("<script>alert('XSS')</script>", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "' OR '1'='1", "Epic sadface: Username and password do not match any user in this service")
])
def test_login_negative_cases(setup_page, base_url, username, password, expected_error):
    # Navigate to the login page
    setup_page.goto(base_url)
    
    # Fill in the username and password fields
    setup_page.fill('input[data-test="username"]', username)
    setup_page.fill('input[data-test="password"]', password)
    
    # Attempt to login
    setup_page.click('input[data-test="login-button"]')
    
    # Verify the error message is displayed
    error_message = setup_page.query_selector('h3[data-test="error"]').inner_text()
    assert error_message == expected_error
