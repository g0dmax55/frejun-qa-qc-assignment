# pages/login_page.py

class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill("#user-name", username)  # Fill in the username field
        self.page.fill("#password", password)   # Fill in the password field
        self.page.click("#login-button")        # Click the login button
