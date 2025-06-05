import pytest
from pages.login_page import LoginPage

# List of valid usernames
valid_usernames = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]

# List of invalid usernames for testing purposes
invalid_usernames = [
    "invalid_user"
]

def login_and_assert(page, base_url, username, password, expected_url=None, error_message=None):
    login_page = LoginPage(page)
    login_page.navigate(base_url)
    login_page.login(username, password)
    if expected_url:
        assert page.url == expected_url
    if error_message:
        assert error_message in page.text_content(".error-message-container")

@pytest.mark.parametrize("username", valid_usernames)
def test_successful_login(page, username, base_url):
    login_and_assert(page, base_url, username, "secret_sauce", expected_url=f"{base_url}/inventory.html")

@pytest.mark.parametrize("username", invalid_usernames)
def test_invalid_username_login(page, username, base_url):
    login_and_assert(page, base_url, username, "secret_sauce", error_message="Epic sadface")

def test_invalid_password_login(page, base_url):
    login_and_assert(page, base_url, "standard_user", "wrong_password", error_message="Epic sadface")

def test_locked_out_user_login(page, base_url):
    login_and_assert(page, base_url, "locked_out_user", "secret_sauce", error_message="Epic sadface")

@pytest.mark.parametrize("username, password", [
    ("", ""),  # Both fields empty
    ("' OR '1'='1", "password"),  # SQL injection attempt in username
    ("standard_user", "' OR '1'='1"),  # SQL injection attempt in password
    ("a" * 500, "secret_sauce"),  # Excessively long username
    ("standard_user", "a" * 500),  # Excessively long password
    ("!@#$%^&*()", "secret_sauce"),  # Special characters in username
    ("standard_user", "!@#$%^&*()"),  # Special characters in password
    (" standard_user ", "secret_sauce"),  # Leading and trailing whitespace in username
    ("standard_user", " secret_sauce "),  # Leading and trailing whitespace in password
])
def test_edge_case_login(page, username, password, base_url):
    login_and_assert(page, base_url, username, password, error_message="Epic sadface")

# Case Sensitivity: Test for case sensitivity in username and password
@pytest.mark.parametrize("username, password", [
    ("Standard_User", "secret_sauce"),  # Case change in username
    ("standard_user", "Secret_Sauce"),  # Case change in password
])
def test_case_sensitivity(page, username, password, base_url):
    login_and_assert(page, base_url, username, password, error_message="Epic sadface")
