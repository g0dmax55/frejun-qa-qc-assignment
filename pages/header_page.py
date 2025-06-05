# pages/header_page.py

class HeaderPage:
    def __init__(self, page):
        self.page = page

    def click_menu_button(self):
        # Simulate clicking the menu button to reveal the logout option
        self.page.click('#react-burger-menu-btn')

    def logout(self):
        self.click_menu_button()
        # Click the logout button
        self.page.click('#logout_sidebar_link')

